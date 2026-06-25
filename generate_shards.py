import webdataset as wds
from pathlib import Path

images = list(Path('images').glob('*.png'))

with wds.ShardWriter("Shards/shard-%06d.tar", maxcount=500) as sink:
    for img in images:
        sink.write({'__key__':img.stem, 'png':img.read_bytes()})