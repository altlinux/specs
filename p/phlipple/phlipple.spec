Name: phlipple
Version: 0.8.5
Release: alt1
Summary: Reduce a 3D shape to a single square
Group: Games/Puzzles
License: GPLv3
Source: %name-%version.tar.gz
Url: http://sourceforge.net/projects/phlipple/

# Automatically added by buildreq on Mon Nov 07 2011
# optimized out: fontconfig libGL-devel libGLU-devel libSDL-devel libogg-devel pkg-config
BuildRequires: ImageMagick-tools libSDL_image-devel libSDL_mixer-devel libglew-devel libvorbis-devel

%description
Phlipple is a unique puzzle game. The goal of every level is to reduce
a 3D shape to a single square. Elimination of squares is done by
flipping edges around just like in a cardboard box.

It starts off relatively easy to teach the basics just to later on serve
hours of brain tickling fun. It's a great way to train memory as well as
orientation in 3D.

%prep
%setup
for N in 16 24 32 48 128; do convert extra/%name.png $N.png; done

%build
%configure
%make_build

%install
make install DESTDIR=%buildroot
for N in 16 24 32 48 128; do
	install -D $N.png %buildroot%_iconsdir/${N}x${N}/apps/%name.png
done

%files
%doc %_defaultdocdir/%name/*
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_pixmapsdir/*
%_iconsdir/*/apps/*

%changelog
* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 0.8.5-alt1
- Autobuild version bump to 0.8.5

* Tue Nov 08 2011 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Autobuild version bump to 0.8.2

* Tue Nov 08 2011 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Initial build from scratch

