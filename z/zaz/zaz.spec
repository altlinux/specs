Name:		zaz
Version:	1.0.0
Release:	alt1
Group:		Games/Arcade
License:	GPLv3
Source:		http://sunet.dl.sourceforge.net/project/%name/%name-%version.tar.gz
Summary:	A puzzle game where the player has to arrange balls in triplets.
URL:		http://sourceforge.net/projects/zaz
Packager:	Fr. Br. George <george@altlinux.ru>
Requires:	%name-data = %version

# Automatically added by buildreq on Fri Oct 09 2009
BuildRequires: ImageMagick-tools gcc-c++ libGL-devel libSDL-devel libSDL_image-devel libtheora-devel libvorbis-devel

BuildRequires: pkgconfig(ftgl) >= 2.1.3

%description
Zaz ain't Z*** is a puzzle game where the player has to arrange balls in triplets.

%package data
Group:		Games/Arcade
Summary:	Game data files for ZAZ
BuildArch:	noarch

%description data
Zaz ain't Z*** is a puzzle game where the player has to arrange balls in triplets.
This package contains platform-independed data files.

%prep
%setup -q

cat > %name.sh <<@@@
#!/bin/sh
if [ -z "\$LC_ALL" ]
then
  if [ -n "\$LANG" ]; then LC_ALL="\$LANG";
  elif [ -n "\$LC_MESSAGES" ]; then LC_ALL="\$LC_MESSAGES";
  fi
fi
case "\$LC_ALL" in
*_*.*) export LC_ALL="\${LC_ALL%%.*}.UTF-8";;
esac
exec "\$0.bin"
@@@

%build
%configure
%make_build
convert extra/%name.xpm -resize 48x48 x48.xpm

%install
%makeinstall applicationdir=%buildroot%_desktopdir icondir=%buildroot%_iconsdir
install -D x48.xpm %buildroot%_liconsdir/%name.xpm
install -D extra/%name.xpm %buildroot%_iconsdir/hicolor/64x64/apps/%name.xpm
rm -rf %buildroot%prefix/doc %buildroot%_iconsdir/%name.xpm
mv %buildroot%_bindir/%name %buildroot%_bindir/%name.bin
install -m755 %name.sh %buildroot%_bindir/%name
%find_lang %name

%files -f %name.lang
%doc /usr/share/doc/zaz/*
%_bindir/*
%_desktopdir/%name.desktop
%_liconsdir/%name.xpm
%_iconsdir/hicolor/64x64/apps/%name.xpm
%dir %_datadir/%name

%files data
%_datadir/%name/*


%changelog
* Sun Sep 05 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Version up

* Thu Jul 29 2010 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Version up

* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 0.7.0-alt1
- Version up

* Fri Mar 12 2010 Fr. Br. George <george@altlinux.ru> 0.3.3-alt1
- Version up
- Russian translation fixes

* Thu Feb 04 2010 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Version up

* Fri Oct 09 2009 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial build from scratch

