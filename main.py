from scrape import scrape

def main():
    try:
        scrape(2)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()