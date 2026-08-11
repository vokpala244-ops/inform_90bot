import os
from playwright.sync_api import sync_playwright
from PIL import Image
import io

def generate_promo_image():
    """Generate the Paisa Base promotional image from HTML"""
    
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Paisa Base - Maximize Your Earnings</title>
      <script src="https://cdn.tailwindcss.com"></script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
      <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
      <script>
        tailwind.config = {
          theme: {
            extend: {
              fontFamily: {
                sans: ['Poppins', 'sans-serif'],
                heading: ['Montserrat', 'sans-serif'],
              },
              colors: {
                brand: {
                  blue: '#0B2B6B',
                  green: '#00A859',
                  lightGreen: '#00C853',
                  badgeGreen: '#00B050',
                  bgLight: '#EAF6F0',
                }
              }
            }
          }
        }
      </script>
      <style>
        body { margin: 0; padding: 0; background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Poppins', sans-serif; }
        .container { width: 420px; background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.15); }
      </style>
    </head>
    <body>
      <div class="container">
        <!-- Header Logo & Title -->
        <header class="p-6 text-center bg-white">
          <div class="flex items-center justify-center gap-2 mb-4">
            <div class="w-10 h-10 bg-[#00A859] rounded-full flex items-center justify-center text-white font-extrabold text-2xl">
              P
            </div>
            <span class="text-3xl font-extrabold text-[#0B2B6B] tracking-tight">Paisa <span class="text-[#00A859]">base</span></span>
          </div>
          <h1 class="text-2xl font-bold text-[#0B2B6B] uppercase leading-snug tracking-wide">
            Maximize Your Earnings<br>
            <span class="text-[#0B2B6B]">With </span><span class="text-[#00A859]">Paisa Base</span>
          </h1>
        </header>

        <!-- Hero Banner Section -->
        <section class="relative bg-gradient-to-r from-[#0B2B6B] via-blue-900 to-[#00A859] p-8 text-white text-center overflow-hidden">
          <div class="absolute top-3 left-6 text-yellow-400 opacity-80 text-2xl"><i class="fa-solid fa-coins"></i></div>
          <div class="absolute top-12 left-12 text-emerald-300 opacity-70 text-xl"><i class="fa-solid fa-circle-dollar-to-slot"></i></div>
          <div class="absolute bottom-4 left-8 text-yellow-400 opacity-80 text-xl"><i class="fa-solid fa-indian-rupee-sign"></i></div>
          <div class="absolute top-4 right-10 text-white text-3xl transform rotate-45"><i class="fa-solid fa-rocket"></i></div>
          <div class="absolute bottom-6 right-8 text-yellow-400 opacity-80 text-2xl"><i class="fa-solid fa-coins"></i></div>

          <div class="relative z-10 my-2">
            <h2 class="text-5xl font-bold tracking-tight text-white drop-shadow-md">
              4.5%
            </h2>
            <p class="text-2xl font-bold uppercase tracking-wider text-gray-100 mt-1">
              ON INR
            </p>
            <div class="inline-block mt-4 bg-[#00B050] text-white font-bold text-2xl px-8 py-3 rounded-full shadow-lg border-2 border-white/20">
              USDT 108
            </div>
          </div>
        </section>

        <!-- Middle Features Grid -->
        <section class="p-6 bg-white grid grid-cols-3 gap-4 border-b border-gray-100 text-center">
          <div class="flex flex-col items-center">
            <div class="w-16 h-16 rounded-full bg-blue-50 flex items-center justify-center text-[#0B2B6B] text-3xl mb-2 shadow-sm">
              <i class="fa-solid fa-stopwatch-20"></i>
            </div>
            <h3 class="font-bold text-[#0B2B6B] text-sm uppercase leading-tight">
              Fast<br>Sales
            </h3>
          </div>
          <div class="flex flex-col items-center">
            <div class="w-16 h-16 rounded-full bg-blue-50 flex items-center justify-center text-[#0B2B6B] text-3xl mb-2 shadow-sm">
              <i class="fa-solid fa-mobile-screen-button"></i>
            </div>
            <h3 class="font-bold text-[#0B2B6B] text-sm uppercase leading-tight">
              Set Your<br>Own Limit
            </h3>
          </div>
          <div class="flex flex-col items-center">
            <div class="w-16 h-16 rounded-full bg-blue-50 flex items-center justify-center text-[#0B2B6B] text-3xl mb-2 shadow-sm">
              <i class="fa-solid fa-headset"></i>
            </div>
            <h3 class="font-bold text-[#0B2B6B] text-sm uppercase leading-tight">
              24/7<br>Customer<br>Care
            </h3>
          </div>
        </section>

        <!-- Bottom Promo Cards -->
        <section class="p-4 grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-50">
          <div class="bg-[#00A859] rounded-xl p-4 text-white flex items-center justify-between shadow-md relative overflow-hidden">
            <div class="z-10">
              <p class="font-bold text-lg uppercase leading-tight">
                24/7<br>Customer<br>Care
              </p>
            </div>
            <div class="text-5xl opacity-90 text-white z-10">
              <i class="fa-solid fa-chart-line"></i>
            </div>
            <div class="absolute -right-4 -bottom-4 w-20 h-20 bg-white/10 rounded-full"></div>
          </div>
          <div class="bg-emerald-100 border border-emerald-200 rounded-xl p-4 text-[#0B2B6B] flex items-center justify-between shadow-md relative overflow-hidden">
            <div class="z-10">
              <div class="flex items-center gap-2 mb-1">
                <i class="fa-solid fa-chart-pie text-[#00A859] text-2xl"></i>
                <i class="fa-solid fa-user-group text-[#0B2B6B] text-xl"></i>
              </div>
              <span class="inline-block bg-[#0B2B6B] text-white text-xs px-2 py-0.5 rounded font-bold uppercase">
                Verified Support
              </span>
            </div>
            <div class="w-8 h-8 bg-[#0B2B6B] text-white rounded-full flex items-center justify-center font-bold text-sm">
              <i class="fa-solid fa-check"></i>
            </div>
          </div>
        </section>
      </div>
    </body>
    </html>
    '''
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 420, 'height': 800})
        page.set_content(html_content)
        page.wait_for_timeout(2000)  # Wait for fonts to load
        
        # Take screenshot
        screenshot = page.screenshot(full_page=True)
        browser.close()
        
        # Save the image
        with open('paisa_base_promo.png', 'wb') as f:
            f.write(screenshot)
        
        print("✅ Promotional image generated successfully!")

if __name__ == "__main__":
    generate_promo_image()
