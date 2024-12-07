# RITA API Reference

## Core Endpoints

### Health Check
```http
GET /health

Returns: 
{
    "status": "healthy",
    "version": "0.1.0"
}
```

### Chat

#### Send Message
```http
POST /api/chat

Request:
{
    "message": string,
    "context": [
        {
            "role": "user"|"assistant",
            "content": string
        }
    ]?
}

Response:
{
    "response": string,
    "context": [
        {
            "role": "user"|"assistant",
            "content": string
        }
    ]
}
```

## Vision Endpoints (Optional)

### Image Analysis
```http
POST /api/vision/analyze
Content-Type: multipart/form-data

Request:
- file: image file (jpeg, png)
- prompt: string (optional guidance for analysis)

Response:
{
    "objects": [
        {
            "type": string,
            "confidence": float,
            "location": {
                "x": int,
                "y": int,
                "width": int,
                "height": int
            }
        }
    ],
    "analysis": string
}
```

## Voice Endpoints (Optional)

### Speech-to-Text
```http
POST /api/voice/transcribe
Content-Type: multipart/form-data

Request:
- file: audio file (wav, mp3)
- language: string (optional)

Response:
{
    "text": string,
    "language": string,
    "confidence": float
}
```

## Error Responses

All endpoints may return these errors:

### 400 Bad Request
```json
{
    "detail": "Invalid request format"
}
```

### 404 Not Found
```json
{
    "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
    "detail": "Internal server error"
}
```

## Request Limits

- Maximum file size: 10MB
- Rate limit: 100 requests per minute
- Maximum message length: 4096 tokens
- Supported image formats: JPEG, PNG
- Supported audio formats: WAV, MP3

## Authentication

Currently, the API does not require authentication. Future versions will include authentication mechanisms.

## Examples

### Chat Example
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "How can I repair a broken zipper?",
    "context": []
  }'
```

### Vision Example
```bash
curl -X POST http://localhost:8000/api/vision/analyze \
  -F "file=@broken_zipper.jpg" \
  -F "prompt=Check for zipper damage"
```

### Voice Example
```bash
curl -X POST http://localhost:8000/api/voice/transcribe \
  -F "file=@repair_question.wav" \
  -F "language=en"
```

## Notes

- All timestamps are in ISO 8601 format
- All sizes are in bytes unless specified otherwise
- All probabilities/confidences are between 0.0 and 1.0
- Coordinates are in pixels from top-left corner
