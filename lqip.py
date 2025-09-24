from PIL import Image
import base64
from io import BytesIO

# 입력 이미지 경로
img_path = "./assets/posts/cma/description.jpg"

# 이미지 열기
with Image.open(img_path) as img:
    # 작은 썸네일로 변환 (LQIP 용도)
    img.thumbnail((20, 20))

    # JPEG로 변환 후 메모리에 저장
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=30)
    lqip_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

# data URI 형식으로 반환
lqip_data_uri = f"data:image/jpeg;base64,{lqip_base64}"
# lqip_data_uri[:200]
print(lqip_data_uri)
print(len(lqip_data_uri))
