import instaloader
import sys
L = instaloader.Instaloader()
def download_reel(url):
    try:
        shortcode=url.rstript('/').split('/')[-1]
        L.dowmload_post(instaloader.post.from_shortcode(L.context,shortcode),target='downloded_reels') 
        print("Download sucessful !check the 'download_reels' folder.")
    except Exception as e:
        print(f"Failed to download reel: {e}")   
if __name__ =="__main__":
    if len(sys.argv) !=2:
        print("Usage: python proj.py <Instagram reel URL>")
        sys.exit(1)
        reel_url = sys.argv[1]
        download_reel(reel_url)