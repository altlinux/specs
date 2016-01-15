%set_verify_elf_method unresolved=strict

Name: gnustep-MusicBox
Version: 20030331
Release: alt2.cvs20140130.1
Summary: MusicBox is a music manager based on GNUstep
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: https://savannah.nongnu.org/projects/musicbox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@cvs.savannah.nongnu.org:/sources/musicbox co musicbox
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libogg-devel libvorbis-devel libSDL-devel
BuildPreReq: libSDL_sound-devel gnustep-cddb.bundle-devel
BuildPreReq: gnustep-ShengGuang-devel

Requires: lib%name = %EVR
Requires: gnustep-back
Requires: gnustep-cddb.bundle
Requires: gnustep-ShengGuang
Requires: cdparanoia
Requires: vorbis-tools
Requires: gnustep-Mixer

%description
MusicBox is a music manager based on GNUstep. It contains two parts: the
underneath audio control as ShengGuang library, and the user interface
as MusicBox.

%package -n lib%name
Summary: Shared libraries of MusicBox
Group: System/Libraries

%description -n lib%name
MusicBox is a music manager based on GNUstep. It contains two parts: the
underneath audio control as ShengGuang library, and the user interface
as MusicBox.

This package contains shared libraries of MusicBox.

%package -n lib%name-devel
Summary: Development files of MusicBox
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
MusicBox is a music manager based on GNUstep. It contains two parts: the
underneath audio control as ShengGuang library, and the user interface
as MusicBox.

This package contains development files of MusicBox.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-I$PWD/Mixer" \
	MUSICBOX_LIBRARY=$PWD/MusicBox/MusicBox/obj
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

pushd %buildroot%_libdir
for j in MusicBox; do
	cp GNUstep/Libraries/*.so* ./
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Libraries/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Libraries/$i
		done
	done
done
popd

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/MusicBox.app/MusicBox \
	%buildroot%_bindir/
install -d %buildroot%_includedir
ln -s %_libdir/GNUstep/Headers/MusicBox %buildroot%_includedir/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog FAQ README TODO USAGE
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Headers

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 20030331-alt2.cvs20140130.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20030331-alt2.cvs20140130
- Built with clang
- Added menu file (thnx kostyalamer@)

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20030331-alt1.cvs20140130
- Initial build for Sisyphus

