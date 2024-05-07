from scrape import scrape

def main():
    try:
        scrape(561, "normal")
    except:
        try:
            scrape(561, "special")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()