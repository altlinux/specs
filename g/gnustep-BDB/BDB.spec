%set_verify_elf_method unresolved=strict

Name: gnustep-BDB
Version: 0.2.1
Release: alt2
Summary:  Berkeley DB Wrapper (BDB)
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://fortytwo.sourceforge.net/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: config.properties

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Encore-devel libdb4.8-devel

Requires: lib%name = %EVR
Requires: gnustep-Encore
Requires: gnustep-back

%description
BDB is a set of classes implementing an interface to
Berkeley DB for the GNUstep and Mac OS X environment written in
Objective-C language. It is based on the C API of
Berkeley DB and offers an object oriented interface which relies on
classes and mechanisms offered by the Foundation library.

In its present state BDB just offers a reduced set of functionality of
Berkeley DB.

%package -n lib%name
Summary: Shared libraries of BDB
Group: System/Libraries

%description -n lib%name
BDB is a set of classes implementing an interface to
Berkeley DB for the GNUstep and Mac OS X environment written in
Objective-C language. It is based on the C API of
Berkeley DB and offers an object oriented interface which relies on
classes and mechanisms offered by the Foundation library.

This package contains shared libraries of BDB.

%package -n lib%name-devel
Summary: Development files of BDB
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
BDB is a set of classes implementing an interface to
Berkeley DB for the GNUstep and Mac OS X environment written in
Objective-C language. It is based on the C API of
Berkeley DB and offers an object oriented interface which relies on
classes and mechanisms offered by the Foundation library.

This package contains development files of BDB.

%prep
%setup

install -m644 %SOURCE1 ./
%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|" config.properties

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -I%_includedir/Encore' \
	CONFIG_SYSTEM_LIBS='-lEncore -lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for j in BDB; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

install -d %buildroot%_localstatedir/GNUstep

%files
%doc ANNOUNCEMENT README TODO ChangeLog doc/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/BDB.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/BDB.framework/Headers
%dir %_localstatedir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/BDB.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/BDB.framework/Headers

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

