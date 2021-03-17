Name:   kseg-qt4
Version:    1.0
Release:    alt1
License:    GPLv2
Summary:    QT4 port of KSeg, euclidean geometry exploration tool
Group:      Education
URL:        http://fedorchenko.net/kseg.php
Source:     kseg-1.0_pre2014-06-03.tar.bz2
Source1:    Atan2definition.svg
Patch1: kseg-setFilePath.patch
Patch2: kseg-KSEG_HOME.patch

# Automatically added by buildreq on Wed Mar 17 2021
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libImageMagick6-common libcairo-gobject libgdk-pixbuf libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-xml libstdc++-devel python2-base sh4 zlib-devel
BuildRequires: ImageMagick-tools gcc-c++ libqt4-webkit-devel phonon-devel

%description
KSEG is a tool designed to let you easily visualize dynamic properties
of compass-and-straightedge constructions and to make geometric
exploration as fast and easy as possible.

%prep
%setup -n kseg-1.0_pre2014-06-03
%patch1 -p1
%patch2 -p1

%define _appdir %_datadir/%name

%build
%qmake_qt4
%make_build
for N in 16 32 48 64 128; do
    convert %SOURCE1 -resize $N $N.png
done
cat > %name.desktop <<@@@
[Desktop Entry]
Name=%name
Comment=Euclidean geometry explorer
GenericName=Euclidean geometry
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Qt;Education;Math;
@@@

%install
mkdir -p %buildroot%_appdir/{examples,pics,lang} %buildroot%_bindir
install -p -m755 kseg %buildroot%_bindir/%name
install -p -m644 *.qm *.html %buildroot%_appdir/lang/
install -p -m644 examples/* %buildroot%_appdir/examples/
install -p -m644 pics/*  %buildroot%_appdir/pics/
install -D %name.desktop %buildroot%_desktopdir/%name.destop

for N in 16 32 48 64 128; do
    install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done
install -D %SOURCE1 %buildroot%_iconsdir/hicolor/scalable/apps/%name.png

%files
%doc AUTHORS* README
%_bindir/*
%_appdir/lang
%_appdir/examples
%_appdir/pics
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*



%changelog
* Wed Mar 17 2021 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build for ALT

