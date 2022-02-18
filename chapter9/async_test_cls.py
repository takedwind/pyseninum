from asyncio import sleep
from chapter9.async_logs import logs


class Base:

    async_driver = None

    async def get(self, url: str = r'http://127.0.0.1/zentao/user-login.html'):
        await self.async_driver.get(url)


class LoginPage(Base):

    async def login(self, username: str = 'admin', password: str = 'admin123456'):
        await self.async_driver.send_keys('id', 'account', text=username)
        await self.async_driver.send_keys('name', 'password', text=password)
        await self.async_driver.click('id', 'submit')


class MainPage(LoginPage):

    async def search(self, text: str = '1'):
        await self.async_driver.send_keys('id', 'searchInput', text=text)
        await self.async_driver.click('id', 'searchGo')

    async def logout(self):
        await self.async_driver.click('class', 'user-name')
        await self.async_driver.click('xpath', '//a[text()="退出"]')


class AsyncTestLogin(MainPage):

    @logs
    async def test_login(self, *args):
        await self.get()
        await sleep(1)
        await self.login(*args)
        await sleep(1)
        assert await self.async_driver.find_element('xpath', '//span[@class="user-name"]')
        await self.logout()
        await sleep(1)


class AsyncTestMain(MainPage):

    @logs
    async def test_search(self, text: str = '1'):
        await self.get()
        await sleep(1)
        await self.login()
        await sleep(1)
        await self.search(text)
        await sleep(1)
        assert await self.async_driver.text('xpath', '//span[@class="label label-id"]') == text
        await self.logout()
        await sleep(1)
