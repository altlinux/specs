Name: earth3d
Version: 1.0.5
Release: alt3.1

Summary: A program that visualizes the earth in realtime in a 3D view
License: GPL
Group: Graphics
#Group: Sciences/Geosciences

Url: http://www.earth3d.org
Source: earth3d_client-%version-src.tar.bz2
Patch0: earth3d_client-1.0.4-alt-makefile.patch
Patch1: earth3d_client-1.0.5-alt-gcc43.patch
Patch2: earth3d-1.0.5-alt-DSO.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Jan 08 2006
BuildRequires: fontconfig freetype2 gcc-c++ libpng-devel libqt3-devel libqt3-settings libstdc++-devel qt3-designer zlib-devel

%description
Earth3D is a program that visualizes the earth in realtime in a
3D view. It uses data from NASA, USGS, the CIA and the city of
Osnabruck.  I would like to thank these organisations to allow
me to use their data! The program is available as binary for
Linux, MacOS X and Windows under the GPL license. The program's
features are:

* viewing the earth as a whole
* zooming in until countries, cities and even single houses
  become visible (in areas where the necessary map resolution is
  available)
* embedding external data like current earthquake positions,
  cloud data or GPS points

You can also get some maps mirrored locally to speed up access:
http://venus.schunter.etc.tu-bs.de/~gunia/earthdata.zip
(~1.1->1.9Gb; doesn't include Landsat7 100m/pixel data)

PS: packaged experiencing frustration of Google Earth ;)

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p2
echo "#include <gltest.h>" >gltestwidget.h

%build
unset QTDIR || : ; . /etc/profile.d/qt3dir.sh ; QTDIR=`echo $QTDIR | sed -e 's,/$,,'` ; PATH=$PATH:$QTDIR/bin
qmake earth3d.pro
%make

%install
install -pD -m755 %name   %buildroot%_bindir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc README
%doc %_man1dir/*
%_bindir/*

# TODO: 
# - figure out Group: weirdness (sisyphus_check barfs
#   on perfectly present in GROUPS one)

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt3.1
- Fixed build

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.5-alt3
- fix build

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 1.0.5-alt2
- fixed build with gcc 4.3

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5

* Tue Mar 07 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt2
- fixed build with --as-needed; 
  thanks Dmitry Levin (ldv@) for rm -f /dev/brake

* Wed Feb 08 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- built for Sisyphus
- thanks Yuri Sedunov <aris@> for build fix suggestion

* Sun Jan 08 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt0.M30.1
- built for M30

* Sun Jan 08 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- built for ALT Linux

