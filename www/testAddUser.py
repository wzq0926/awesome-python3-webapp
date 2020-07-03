import asyncio
import orm
import random
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop,user='www-data',password='www-data',db='awesome')
    u =User(name='test',email='test%s@example.com' % random.randint(0,10000000),passwd='abc123456',image='about:blank')
    await u.save()

#要运行协程，需要使用事件循环
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [test(loop)]
	loop.run_until_complete(asyncio.wait(tasks))
	print('test Finish')
	# loop.close() 用了wait，不需要close了