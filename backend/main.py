#!/usr/bin/env python3
"""
AI Secretary Platform - Main Application Entry Point
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler

from config import config
from api.router import router as api_router
from utils.logger import setup_logger
from tasks.scheduler import setup_scheduler
from utils.data_manager import DataManager

# Setup logger
logger = setup_logger(__name__)

# Initialize scheduler
scheduler = BackgroundScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    # Startup
    logger.info(f"Starting {config.APP_NAME}...")
    DataManager.init_data_dir()
    
    if config.SCHEDULER_ENABLED:
        setup_scheduler(scheduler)
        scheduler.start()
        logger.info("Scheduler started")
    
    logger.info(f"{config.APP_NAME} started successfully")
    
    yield
    
    # Shutdown
    logger.info(f"Shutting down {config.APP_NAME}...")
    if scheduler.running:
        scheduler.shutdown()
    logger.info(f"{config.APP_NAME} shutdown complete")

# Create FastAPI app
app = FastAPI(
    title=config.APP_NAME,
    description="AI Secretary Platform - Intelligent conversation-based service automation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix=config.API_PREFIX)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": config.APP_NAME}

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": config.APP_NAME,
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting {config.APP_NAME} on {config.API_HOST}:{config.API_PORT}")
    logger.info(f"Environment: {config.APP_ENV}")
    logger.info(f"Debug: {config.DEBUG}")
    
    uvicorn.run(
        "main:app",
        host=config.API_HOST,
        port=config.API_PORT,
        reload=config.DEBUG,
        log_level=config.LOG_LEVEL.lower()
    )
