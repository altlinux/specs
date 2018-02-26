Name: tint
Version: 1.0.1
Release: alt3.1

Summary: A photo editor for colour-select effects
License: BSD (revised)
Group: Graphics

Url: http://www.indii.org/software/tint
Source: http://www.indii.org/files/tint/releases/%name-%version.tar.gz
Patch0: tint-1.0.1-alt-imagepath.patch
Patch1: tint-1.0.1-alt-fix-link.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Oct 25 2011 (-bi)
# optimized out: elfutils fontconfig ghostscript-classic libgdk-pixbuf libstdc++-devel python-base python-modules python-modules-compiler python-modules-email texlive-base-bin texlive-latex-base
BuildRequires: boost-devel-headers cvs flex gcc-c++ ghostscript-utils libgomp-devel libwxGTK-devel scons

%description
Welcome to tint, a photo editor for colour-select effects.

It automatically clusters the colours of a photo into groups,
and allows each colour to be switched on or off to create the
desired effect.

tint's newer and more powerful version is called tintii;
you might want to have a look at it too.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
scons

%install
install -pDm755 %name %buildroot%_bindir/%name
install -d %buildroot{%_datadir/%name,%_desktopdir}
cp -a images/ samples/ %buildroot%_datadir/%name/
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Type=Application
Name=Tint
GenericName=Image Tinter
Comment=Photo editor for colour-select effects
Exec=tint
Icon=tint
Terminal=false
Categories=Graphics;2DGraphics;RasterGraphics;GTK;
EOF

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%doc LICENSE.txt README.txt VERSION.txt

%changelog
* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt3.1
- rebuid with Python-2.7

* Tue Oct 25 2011 Michael Shigorin <mike@altlinux.org> 1.0.1-alt3
- tint 1.x is so simple and elegant, I miss it :)
  (needs a patch backport though)

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.0.1-alt2
- applied repocop patch

* Tue Aug 28 2007 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- built for ALT Linux
- added rough sketch of a desktop file
  (borrowed/trimmed-down gimp's one)
- hardwired icon path with a band-aid patch to allow tint be
  run from any directory, not only build one
- buildreq
- NB: successful build requires fixed scons, 0.97-alt1 is broken

