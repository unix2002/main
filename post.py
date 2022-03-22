import os

print("Wat is de titel")
title = input()
print("Hoeveelste post is dit?")
nummer = input()
print("h1 dan h2")
h1 = input()
h2 = input()

os.system("echo '<html>' >> post" + nummer + ".html")
os.system("echo '<title>"+ title + "</title>' >> post" + nummer + ".html")
os.system("echo '	<link rel=\"stylesheet\" href=\"../blingBling.css\"></link>' >> post" + nummer + ".html")
os.system("echo '	<head>' >> post" + nummer + ".html")
os.system("echo '		<div id=\"shadowBox\">' >> post" + nummer + ".html")
os.system("echo '		<h1 class=\"rainbow\" align=\"center\">"+ h1 + "</h1>' >> post" + nummer + ".html")
os.system("echo '		</div>' >> post" + nummer + ".html")
os.system("echo '	</head>' >> post" + nummer + ".html")
os.system("echo '	<body>' >> post" + nummer + ".html")
os.system("echo '		<ul id=\"ul\">' >> post" + nummer + ".html")
os.system("echo '  			<li id=\"li\"><a class=\"rainbow\" href=\"../index.html\">Home</a></li>' >> post" + nummer + ".html")
os.system("echo '			<li id=\"li\"><a class=\"rainbow\" href=\"../posts.html\">Posts</a></li>' >> post" + nummer + ".html")
os.system("echo '			<li id=\"li\"><a class=\"rainbow\" href=\"../contact.html\">Contact</a></li>' >> post" + nummer + ".html")
os.system("echo '  			<li id=\"li\"><a class=\"rainbow\" href=\"../info.html\">Info</a></li>' >> post" + nummer + ".html")
os.system("echo '			<li id=\"li\"><a font-color=\"white\" >aangemaakt op ..</a></li>' >> post" + nummer + ".html")
os.system("echo '		</ul>	' >> post" + nummer + ".html")
os.system("echo '		<div class=\"center\">' >> post" + nummer + ".html")
os.system("echo '			<h2>"+ h2 + "</h2>' >> post" + nummer + ".html")
os.system("echo '			<p>	' >> post" + nummer + ".html")

for i in range(200):
    zin = input()
    if zin == "stop":
        break 
    else:
        os.system("echo             '"+ zin + " <br>' >> post" + nummer + ".html")

os.system("echo '			</p>' >> post" + nummer + ".html")
os.system("echo '		</div>' >> post" + nummer + ".html")
os.system("echo '	</body>' >> post" + nummer + ".html")
os.system("echo '</html>' >> post" + nummer + ".html")
