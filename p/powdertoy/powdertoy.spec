Name: powdertoy
Version: 80.3
Release: alt1
Summary: Classic 'falling sand' physics sandbox game
Group: Games/Educational
License: GPL
Url: http://powdertoy.co.uk/
#Patch: %name-%version-%release.patch
# GitHub https://github.com/FacialTurd/The-Powder-Toy/downloads
# Source: %name-%version.tar
# find this at homepage, XXX may disappear
Source: powder-%version-src.zip
Obsoletes: powder

BuildRequires: unzip

# Automatically added by buildreq on Tue Aug 16 2011
# optimized out: libX11-devel xorg-xproto-devel
BuildRequires: bzlib-devel libSDL-devel libfftw3-devel liblua5-devel

%description
The Powder Toy is a desktop version of the classic 'falling sand'
physics sandbox game, it simulates air pressure and velocity as well as
heat!

%prep
%setup -c
#patch -p1
# lua5.1 -> lua
ln -s /usr/include includes/lua5.1
# Remove old version message
sed -i 's/old_version = 1/old_version = 0/g' src/main.c

mv Makefile Makefile.upstream

sed -i 's/lua5.1/lua/g' Makefile.upstream
cat > Makefile <<@@@
include Makefile.upstream
SRCS := \$(wildcard \$(SOURCES))
OBJS := \$(SRCS:.c=.o)
BUS=32
OPT64=\$(MFLAGS_SSE3)
OPT32=-m32
CFLAGS+=\$(OFLAGS) -DINTERNAL -DLIN\$(BUS) \$(OPT\$(BUS))

%name:	\$(OBJS)
	\$(CC) \$(OBJS) \$(LFLAGS) -o\$@
@@@

cat > %name.desktop <<@@@
[Desktop Entry]
Name=The Powder Toy
Type=Application
Exec=%name
Icon=%name
Terminal=false
GenericName=Sandbox game
Categories=Game;Simulation;
Comment=%summary
@@@

%build
%ifarch x86_64
%make_build BUS=64 %name
%else
%make_build %name
%endif

%install
# TODO MIME
install -Ds %name %buildroot%_gamesbindir/%name
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D src/Resources/Icon-16.png %buildroot%_miconsdir/%name.png
install -D src/Resources/Icon-32.png %buildroot%_niconsdir/%name.png

%files
%doc README*
%_gamesbindir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 80.3-alt1
- Autobuild version bump to 80.3

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 77.0-alt1
- Autobuild version bump to 77.0

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 74.2-alt1
- Autobuild version bump to 74.2

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 71.3-alt1
- Autobuild version bump to 71.3

* Fri Jan 13 2012 Fr. Br. George <george@altlinux.ru> 70.1-alt1
- Autobuild version bump to 70.1
- Fix docs

* Tue Aug 30 2011 Fr. Br. George <george@altlinux.ru> 57.0-alt1
- Autobuild version bump to 57.0
- Remove new version ad again

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 55.9-alt1
- Autobuild version bump to 55.9

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 51.0-alt1
- Autobuild version bump to 51.0
- Remove new version ad

* Tue Jul 05 2011 Fr. Br. George <george@altlinux.ru> 50.6-alt2
- Added some native optimization

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 50.6-alt1
- Initial build from scratch

