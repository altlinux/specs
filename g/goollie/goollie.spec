Name: goollie
Version: 20091222
Release: alt2.1
License: GNU
Summary: Ollie the Oligocheata is a worm on a mission
Group: Games/Arcade
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Url: http://www.tweeler.com/index.php?PAGE=goollie_linux
Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Dec 23 2009
BuildRequires: cmake gcc-c++ libGL-devel libImageMagick-devel libSDL_mixer-devel libX11-devel libtuxcap-devel python-devel xorg-xf86vidmodeproto-devel zlib-devel

Provides: python%__python_version(Pycap)

%description
Ollie the Oligocheata is a worm on a mission

%prep
%setup -q -n %name-%version

%__subst "s|/usr/share/games/goollie|%_datadir/%name|g" src/main.cpp

%build
%cmake
%make_build -C BUILD

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%python_sitelibdir/%name

cp BUILD/src/GoOllie %buildroot/usr/bin/
cp -R data/* %buildroot%_datadir/%name/
cp -R src/*.py %buildroot%python_sitelibdir/%name/

#Menu and icons
mkdir -p %buildroot%_niconsdir
install -m644 data/extraResources/Logos/icon.png %buildroot%_niconsdir/%name.png
mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/%name.desktop  <<EOF
[Desktop Entry]
Name=Go Ollie
Comment=%summary
Comment[ru]=Миссия червяка Олли
Exec=%name
Icon=%name
Type=Application
Terminal=false
Categories=Qt;Game;ArcadeGame;
EOF

cat > %name  <<EOF
#!/bin/sh
dir=$(pwd)
cd %python_sitelibdir/%name;
GoOllie
cd $dir
EOF

install -p -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/*
%_datadir/applications/%name.desktop
%_niconsdir/*
%_datadir/%name
%python_sitelibdir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20091222-alt2.1
- Rebuild with Python-2.7

* Fri Dec 25 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 20091222-alt2
- Fix (ALT #22611)

* Tue Dec 22 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 20091222-alt1
- Build for ALT

