%set_verify_elf_method unresolved=strict

Name: gnustep-Cynthiune
Version: 1.0.0
Release: alt1
Summary: First free and romantic music player for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel libid3tag-devel libmad-devel
BuildPreReq: libvorbis-devel libogg-devel libmpcdec-devel
BuildPreReq: libaudiofile-devel libflac-devel libtag-devel libesd-devel
BuildPreReq: libmodplug-devel gcc-c++ libmusicbrainz-devel
BuildPreReq: libalsa-devel libmpc-devel libao-devel

Requires: lib%name = %EVR

%description
Cynthiune is a free software and romantic music player for GNUstep and
MacOSX. For the moment, it looks pretty much like XMMS, Winamp and
similar software. Even though it has far less features than those, the
essential components of a usable and user-friendly program are there in
my opinion.

Cynthiune supports mp3, ogg, mod, xm, wav, au, flac, wma, asf ...

%package -n lib%name
Summary: Shared libraries of GNUstep Cynthiune
Group: System/Libraries

%description -n lib%name
Cynthiune is a free software and romantic music player for GNUstep and
MacOSX. For the moment, it looks pretty much like XMMS, Winamp and
similar software. Even though it has far less features than those, the
essential components of a usable and user-friendly program are there in
my opinion.

Cynthiune supports mp3, ogg, mod, xm, wav, au, flac, wma, asf ...

This package contains shared libraries of GNUstep Cynthiune.

%package -n lib%name-devel
Summary: Development files of GNUstep Cynthiune
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
Cynthiune is a free software and romantic music player for GNUstep and
MacOSX. For the moment, it looks pretty much like XMMS, Winamp and
similar software. Even though it has far less features than those, the
essential components of a usable and user-friendly program are there in
my opinion.

Cynthiune supports mp3, ogg, mod, xm, wav, au, flac, wma, asf ...

This package contains development files of GNUstep Cynthiune.

%prep
%setup

%build
pushd Frameworks/Cynthiune
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	disable-windowsmedia=yes \
	disable-arts=yes \
	AUXILIARY_CPPFLAGS='-O2 -I%_includedir/libmodplug -DGNUSTEP -DMUSEPACK_API_126' \
	CONFIG_SYSTEM_LIBS='-lmad -lvorbisfile -laudiofile -ltag_c -lmpcdec -lmodplug -lFLAC -lesd -lid3tag' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
popd

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	disable-windowsmedia=yes \
	disable-arts=yes \
	AUXILIARY_CPPFLAGS='-O2 -I%_includedir/libmodplug -DGNUSTEP -DMUSEPACK_API_126' \
	CONFIG_SYSTEM_LIBS='-lCynthiune -lmad -lvorbisfile -laudiofile -ltag_c -lmpcdec -lmodplug -lFLAC -lesd -lid3tag' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	disable-windowsmedia=yes \
	disable-arts=yes \
	GNUSTEP_LOCAL_ROOT=%buildroot

pushd %buildroot%_libdir
for i in Cynthiune; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/0/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/0/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$i
done
popd

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog NEWS README TODO
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%changelog
* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt4
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt3
- Added menu files (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Added support of ALSA

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus (without support of AVI files)

