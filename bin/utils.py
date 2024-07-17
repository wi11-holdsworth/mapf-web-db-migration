import re
from itertools import groupby
from tqdm import tqdm


BATCH_SIZE = 10000
    

def mathOriginToPixelOrigin(solution_path: str) -> str:
    return re.sub(r'u', 'd', solution_path)


def encodeRLE(solution_path: str) -> str:
    out: str = ""
    for char, g in groupby(solution_path):
        num = len(list(g))
        out += (str(num) if num > 1 else '') + char
    return out


def streamDocs(fromCol, toCol, **kwargs) -> None:
    cursor = fromCol.find({}, batch_size=BATCH_SIZE)
    num_docs: int = fromCol.estimated_document_count({})

    for doc in tqdm(cursor, desc=toCol.name, total=num_docs):
        for attrib, func in kwargs.items():
            try:
                doc[attrib] = func(doc[attrib])
            except:
                pass

        toCol.insert_one(doc)

    cursor.close()
