%set_verify_elf_method unresolved=strict

Name: gnustep-gsweb
Version: 1.3.0
Release: alt1.svn20110514
Summary: A library which was designed to be compatible with WebObjects 4.x
License: LGPLv2+
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GNUstepWeb
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/gsweb/trunk/
Source: %name-%version.tar
Source1: RCS_ID.h

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gdl2-devel libxml2-devel libpng-devel
BuildPreReq: libwrap-devel

Requires: lib%name = %version-%release

%description
GNUstepWeb is a development framework for web applications written in
Objective-C which is designed to be source-code compatible with
WebObjects 4.5 - a product originally developed by NeXT Inc, whose newer
versions have been released by Apple and are Java-based.

%package -n lib%name
Summary: Shared libraries of GNUstepWeb
Group: System/Libraries

%description -n lib%name
GNUstepWeb is a development framework for web applications written in
Objective-C which is designed to be source-code compatible with
WebObjects 4.5 - a product originally developed by NeXT Inc, whose newer
versions have been released by Apple and are Java-based.

This package contains shared libraries of GNUstepWeb.

%package -n lib%name-devel
Summary: Development files of GNUstepWeb
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
GNUstepWeb is a development framework for web applications written in
Objective-C which is designed to be source-code compatible with
WebObjects 4.5 - a product originally developed by NeXT Inc, whose newer
versions have been released by Apple and are Java-based.

This package contains development files of GNUstepWeb.

%prep
%setup
install -m644 %SOURCE1 ./

%build
export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-installation-domain=SYSTEM

sed -i 'r RCS_ID.h' config.h

%make_build -C GSWeb \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2 -lEOControl -lm'

ldir=$PWD/GSWeb/WebObjects.framework/Versions/1
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS="-L$ldir -lWebObjects -lgnustep-base -lobjc2 -lEOControl -lm"
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in GSWDatabase WOExtensions WOExtensionsGSW WebObjects
do
	lib=$(ls lib$i.so.*.*.*)
	for k in 0 1; do
		for j in lib$i.so*; do
			if [ -e GNUstep/Frameworks/$i.framework/Versions/$k/$lib ]; then
				rm -f $j
				mv GNUstep/Frameworks/$i.framework/Versions/$k/$j ./
				ln -s %_libdir/$lib \
					GNUstep/Frameworks/$i.framework/Versions/$k/$j
			fi
		done
		if [ -e GNUstep/Frameworks/$i.framework/Versions/$k/$lib ]; then
			rm -f GNUstep/Frameworks/$i.framework/Versions/$k/$i
			ln -s %_libdir/$lib \
				GNUstep/Frameworks/$i.framework/Versions/$k/$i
		fi
	done
done
popd

%files
%doc ChangeLog README TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/1/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_datadir/GNUstep
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/1/Headers
%_libdir/GNUstep/Frameworks/*.framework/Headers

%changelog
* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20110514
- Initial build for Sisyphus

