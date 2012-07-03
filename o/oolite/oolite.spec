Name: oolite
Version: 1.74.2
Release: alt2

Summary: A cross-platform, user-modifiable three-dimensional space trading and combat game.
License: GPL
Group: Games/Arcade
Packager: Denis Pynkin <dans@altlinux.ru>

Url: http://developer.berlios.de/projects/oolite-linux/
Source: %name-%version.tar.gz
Source1:	oolite.desktop

Patch: %name-%version-%release.patch

BuildRequires: gnustep-base-devel gnustep-make-devel libobjc gcc-objc
BuildRequires: libSDL-devel libSDL_mixer-devel libSDL_image-devel
BuildRequires: libpng-devel libgif-devel libtiff-devel
BuildRequires: libX11-devel libgmp-devel libffcall
BuildRequires: libespeak-devel

Requires: gnustep-base

%description
Fly from planet to planet, buying and selling goods, shooting pirates 
or committing acts of piracy. There's no goal other than perhaps to achieve 
the rank of ELITE.

%prep
%setup
%patch -p1

cd deps/Cross-platform-deps/SpiderMonkey/js/src
ln -s ../xcode/jsautocfg.h

%build
GNUSTEP_SH_EXPORT_ALL_VARIABLES="yes"
. /usr/share/GNUstep/Makefiles/GNUstep.sh

# Based on <http://www.aegidian.org/bb/viewtopic.php?t=4595>
pushd .
	cd deps/Cross-platform-deps/SpiderMonkey/js/src/fdlibm
	make -f Makefile.ref
	cd ..
	make -j 1 -f Makefile.ref
popd
mv deps/Cross-platform-deps/SpiderMonkey/js/src/Linux_All_DBG.OBJ deps/Cross-platform-deps/SpiderMonkey/js/src/Linux_All_OPT.OBJ
pushd .
	cd deps/Cross-platform-deps/SpiderMonkey/js/src/Linux_All_OPT.OBJ
	mv libjs.so oldlibjs.so
popd

make -e debug=no

%install
install -d %buildroot%_libexecdir/GNUstep/System/Applications/oolite.app/Contents
install -d %buildroot%_libexecdir/GNUstep/System/Applications/oolite.app/Resources
install -m 755 oolite.app/oolite* %buildroot%_libexecdir/GNUstep/System/Applications/oolite.app/
install -m 644 oolite.app/Resources/Info-gnustep.plist %buildroot%_libexecdir/GNUstep/System/Applications/oolite.app/Resources
cp -p -r Resources/* %buildroot%_libexecdir/GNUstep/System/Applications/oolite.app/Resources/
mkdir -p %buildroot%_datadir/applications
cp %SOURCE1 %buildroot%_datadir/applications

rm -f %buildroot%_libexecdir/GNUstep/System/Applications/oolite.app/Resources/Config/gpu-settings.plist

%clean

%files
%defattr (-, root, root)
%_libexecdir/GNUstep/System/Applications/oolite.app/
%_datadir/applications/oolite.desktop
%doc README.txt Doc/*

%changelog
* Wed Apr 27 2011 Denis Pynkin <dans@altlinux.ru> 1.74.2-alt2
- Removed libmesa-devel

* Sat Jan 22 2011 Denis Pynkin <dans@altlinux.ru> 1.74.2-alt1.1
- rebuild

* Sun Dec 05 2010 Denis Pynkin <dans@altlinux.ru> 1.74.2-alt1
- New version
- added libespeak-devel in BuildReq
- remove System/Applications/oolite.app/Resources/Config/gpu-settings.plist
  due segmentation fault on nvidia gpu

* Thu Dec 31 2009 Denis Pynkin <dans@altlinux.ru> 1.73.4-alt1
- Initial build for Sisyphus. Based on Will Stephenson's work.
