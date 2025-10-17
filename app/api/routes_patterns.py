from fastapi import APIRouter, UploadFile
from app.modules.ingest import TextIngestor
from app.modules.extractor import PatternExtractor
from app.modules.storage import PatternStorage

router = APIRouter()
storage = PatternStorage()

@router.post("/extract/")
async def extract_patterns(file: UploadFile):
    text = (await file.read()).decode()
    tokens = TextIngestor().tokenize(text)
    patterns = PatternExtractor(min_support=2).extract(tokens)
    storage.store(patterns)
    return {"patterns_extracted": len(patterns), "top": storage.get_top(5)}
