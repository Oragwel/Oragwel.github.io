from PIL import Image, ImageDraw
import os

OUT = "/home/tidings/Desktop/Oragwel.github.io/assets/img/portfolio"
os.makedirs(OUT, exist_ok=True)

W, H = 800, 500

PROJECTS = [
    ("restaurant",   "#1A1A2E", "#E07B39", "Restaurant Management System",   "Next.js 15  •  Laravel 11  •  KDS  •  POS  •  PWA"),
    ("school",       "#0D3B2E", "#2ECC71", "Smart School Management System",  "Node.js  •  PostgreSQL  •  CBC-Compliant  •  NEMIS"),
    ("rental",       "#1A1A2E", "#007ACC", "Rental Management System",        "React 19  •  Express.js  •  Prisma  •  M-Pesa"),
    ("construction", "#1C1C1C", "#F39C12", "Construction Management System",  "Next.js 14  •  Prisma  •  PostgreSQL  •  Tailwind"),
    ("fuel",         "#0A1628", "#E74C3C", "Fuel Management System",          "React  •  Drizzle ORM  •  Supabase  •  Recharts"),
    ("smartsupport", "#0D0D2B", "#9B59B6", "SmartSupport — AI Platform",      "Python  •  Agentic AI  •  NLP  •  Multilingual"),
    ("aviation",     "#050A1A", "#3498DB", "Intelligent Aviation Ecosystem",  "Python  •  Machine Learning  •  IoT  •  Pricing Engine"),
    ("arena",        "#1A0A2E", "#E91E8C", "Arena Rental Mobile App",         "Flutter  •  Dart  •  Auth  •  Dark/Light Theme"),
    ("najah",        "#0A2010", "#27AE60", "Najah Children's Home CMS",       "Node.js  •  Supabase  •  Cloudinary  •  Live"),
    ("garissa",      "#1A1000", "#C8A84B", "Garissa County Digital Platform", "Web Development  •  Graphic Design  •  Government"),
]

def make_card(filename, bg, accent, title, stack):
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    # Top accent bar
    d.rectangle([0, 0, W, 8], fill=accent)
    # Bottom accent bar
    d.rectangle([0, H-8, W, H], fill=accent)

    # Grid lines (subtle)
    for x in range(0, W, 80):
        d.line([(x, 0), (x, H)], fill=(255,255,255,15), width=1)
    for y in range(0, H, 80):
        d.line([(0, y), (W, y)], fill=(255,255,255,15), width=1)

    # Accent circle decoration
    d.ellipse([W-180, H-180, W+80, H+80], outline=accent, width=2)
    d.ellipse([W-140, H-140, W+40, H+40], outline=accent, width=1)

    # "TIDINGS TECHNOLOGIES" label
    label = "TIDINGS TECHNOLOGIES"
    d.rectangle([40, 40, 40 + len(label)*8 + 20, 70], fill=accent)
    d.text((50, 47), label, fill=bg)

    # Title
    # Break long titles across lines
    words = title.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if len(test) > 28:
            lines.append(cur)
            cur = w
        else:
            cur = test
    if cur:
        lines.append(cur)

    y = 120
    for line in lines:
        d.text((50, y), line, fill="white")
        y += 48

    # Accent underline
    d.rectangle([50, y + 10, 50 + 60, y + 14], fill=accent)

    # Stack text
    d.text((50, y + 30), stack, fill=accent)

    # Corner dot pattern
    for i in range(4):
        for j in range(3):
            cx, cy = 680 + i*25, 80 + j*25
            d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=accent)

    img.save(os.path.join(OUT, f"{filename}.png"))
    print(f"Generated: {filename}.png")

for args in PROJECTS:
    make_card(*args)

print("Done.")
