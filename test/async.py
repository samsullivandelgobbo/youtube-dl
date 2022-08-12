# import asyncio

# async def count():
#     print("One")
#     print("Two")

# async def main():
#     await asyncio.gather(count(), count(), count())

# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# from hook import download
# import asyncio 
# import time



# def main():
#     print(f" Download started at {time.strftime('%X')}")
#     download(input('input url: '))
#     asyncio.sleep(5)
#     print(f"Download finished at {time.strftime('%X')}")

# main()

from hook import download
import datetime



def main(url):
    print('download started at:', datetime.datetime.now())
    download(url)

url = input('enter URL:')
main(url)