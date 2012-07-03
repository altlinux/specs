%define rev 3c26ad5
%define origname vdrift-2010-06-30
Name: vdrift
Version: 20100630
Release: alt2.%rev
Summary: VDrift is a cross-platform, open source driving simulation game.
License: GPL
Group: Games/Sports
Url: http://vdrift.net/
Packager: Andrew Clark <andyc@altlinux.org>
Source: http://downloads.sourceforge.net/vdrifti/%origname-src.tar.bz2
Source1: %name.desktop
Source2: %name.png

# Automatically added by buildreq on Sat Jul 09 2011
# optimized out: libGL-devel libGLU-devel libSDL-devel libX11-devel libogg-devel libstdc++-devel pkg-config python-base python-modules python-modules-compiler python-modules-email xorg-xproto-devel
BuildRequires: gcc-c++ libSDL_gfx-devel libSDL_image-devel libbullet-devel libcurl-devel libglew-devel libvorbis-devel scons subversion

Requires: %name-data = %version

%description
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind. The driving physics engine was recently
re-written from scratch but was inspired and owes much to the
Vamos physics engine.

%prep
%setup -q -n %origname
sed -in '/^#include <curl\/types\.h>/d' include/http.h


%build
scons prefix=/usr bindir=/usr/bin release=1

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_gamesdatadir/%name/

install -pD -m 755 %_builddir/%origname/build/%name %buildroot%_bindir/%name

mkdir -p %buildroot%_desktopdir
install -pD -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_liconsdir
install -pD -m 644 %SOURCE2 %buildroot%_liconsdir/%name.png


%files
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/*.png


%changelog
* Sat Jul 9 2011 Andrew Clark <andyc@altlinux.org> 20100630-alt2.3c26ad5
- version update to 20100630-alt2.3c26ad5

* Sat Feb 19 2011 Andrew Clark <andyc@altlinux.org> 20100630-alt1.svn3064
- version update to 20100630-alt1.svn3064

* Fri Aug 6 2010 Andrew Clark <andyc@altlinux.org> 20100630-alt1.svn2840
- version update to 20100630-alt1.svn2840

* Mon Feb 1 2010 Andrew Clark <andyc@altlinux.org> 20090615-alt1.svn2567
- version update to 20090615-alt1.svn2567

* Wed Nov 25 2009 Andrew Clark <andyc@altlinux.org> 20090615-alt1
- initial build for ALT.

