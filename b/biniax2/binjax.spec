Name:		biniax2
Version:	1.30
Release:	alt2
License:	ZLib
Group:		Games/Puzzles
Summary:	Colour block logic game with original gameplay
Source:		http://mordred.dir.bg/biniax/%name-%version-fullsrc.tar.gz
Source2:	http://mordred.dir.bg/biniax/about2.html
URL:		http://biniax.com
Packager:	Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Sun May 31 2009
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel lynx
Requires:	%name-data

%description
How to play Biniax :
   The gaming field is a 5x7 grid filled partially with pairs of elements. Every pair consists of two different elements combined of four possible.
   You control the box with an element inside. You can move around the field on empty spaces. You can also remove pairs of elements, if you have the same element as the one of the pair. When you remove the pair your element becomes the other one element of the pair and the score is increased;
   The gaming field scrolls down slowly (increasing the speed with your progress) and your goal is to stay as long as possible on the field. Remember, that if you can not take the pair in front of you, the scrolling will move your block down!

%package data
License:	ZLib
Summary:	Data files for %name
BuildArch:	noarch
Group:		Games/Puzzles

%description	data
Data files for %name

%prep
%setup -q -c -n %name-%version
%make
cat > %name.sh <<@@@
#!/bin/sh
test -d "\$HOME/.%name" || {
  rm -rf "\$HOME/.%name"
  mkdir -p "\$HOME/.%name"
  ln -s %_gamesdatadir/%name/data "\$HOME/.%name/data"
}
cd "\$HOME/.%name"
exec %name.bin
@@@

cat > %name.desktop <<@@@
[Desktop Entry]
Categories=Game;BlocksGame;
Type=Application
Exec=%name
Icon=%name
Terminal=false
Name=Biniax-2
GenericName=Colour logic game
@@@

lynx -nonumbers -dump -width=120 %SOURCE2 | sed -n '/Appendix/,$p' > LICENSE
rm data/Thumbs.db

%install
install -D %name %buildroot%_gamesbindir/%name.bin
install -D -m755 %name.sh %buildroot%_gamesbindir/%name
install -D data/graphics/element3.png %buildroot%_liconsdir/%name.png
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_gamesdatadir/%name
cp -r data %buildroot%_gamesdatadir/%name/data

%files
%doc LICENSE 
%_gamesbindir/*
%_liconsdir/*
%_desktopdir/*
%dir %_gamesdatadir/%name

%files data
%_gamesdatadir/%name/*

%changelog
* Wed Jun 03 2009 Fr. Br. George <george@altlinux.ru> 1.30-alt2
- Repocop fixes

* Sun May 31 2009 Fr. Br. George <george@altlinux.ru> 1.30-alt1
- Initial buildfrom scratch

