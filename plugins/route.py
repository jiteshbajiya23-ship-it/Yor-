from aiohttp import web

routes = web.RouteTableDef()

# Render health check + UptimeRobot ke liye.
# allow_head=True => HEAD request bhi 200 return karegi (UptimeRobot free HEAD use karta hai).

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.Response(text="Xiao Bhai Donghua FileStore Bot is running 🐉", status=200)


@routes.get("/health", allow_head=True)
async def health_route_handler(request):
    return web.json_response({"status": "ok"})


@routes.get("/ping", allow_head=True)
async def ping_route_handler(request):
    return web.Response(text="pong", status=200)
