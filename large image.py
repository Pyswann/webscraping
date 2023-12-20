from httpx import get

prompt = "ROAD+BIKE"
key = "41320776-6c345e491b33a7a50487246cd"
image_type = "photo"
api_url = f"https://pixabay.com/api/?key={key}&q={prompt}"

limage = []
i = 0
res = get(api_url).json()
urls = res.get('hits')

for url in urls:
    img_url = url.get('largeImageURL')
    r = get(img_url)
    with open(f"images/{i}.jpg", "wb") as img:
        img.write(r.content)
        i += 1



