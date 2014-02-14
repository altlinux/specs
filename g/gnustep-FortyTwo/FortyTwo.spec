%set_verify_elf_method unresolved=strict

Name: gnustep-FortyTwo
Version: 0.2.0
Release: alt3
Summary: Generic, native graph management system for GNUstep and Cocoa
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://fortytwo.sourceforge.net/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: config.properties

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Encore-devel gnustep-BDB-devel

Requires: lib%name = %EVR
Requires: gnustep-BDB
Requires: gnustep-Encore
Requires: gnustep-back

%description
FT is a generic, native graph management system for GNUstep and Cocoa
and is written in Objective-C. With FT you can persistently manage
graphs consisting of nodes and edges. Each node may provide so-called
services. Such a service may be e.g. a dictionary services, which all
nodes provide at present. This service allows the storage of any data in
a node and is based on keys which uniquely identify content within a
dictionary.

%package -n lib%name
Summary: Shared libraries of FortyTwo
Group: System/Libraries

%description -n lib%name
FT is a generic, native graph management system for GNUstep and Cocoa
and is written in Objective-C. With FT you can persistently manage
graphs consisting of nodes and edges. Each node may provide so-called
services. Such a service may be e.g. a dictionary services, which all
nodes provide at present. This service allows the storage of any data in
a node and is based on keys which uniquely identify content within a
dictionary.

This package contains shared libraries of FortyTwo.

%package -n lib%name-devel
Summary: Development files of FortyTwo
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
FT is a generic, native graph management system for GNUstep and Cocoa
and is written in Objective-C. With FT you can persistently manage
graphs consisting of nodes and edges. Each node may provide so-called
services. Such a service may be e.g. a dictionary services, which all
nodes provide at present. This service allows the storage of any data in
a node and is based on keys which uniquely identify content within a
dictionary.

This package contains development files of FortyTwo.

%package docs
Summary: Documentation for FortyTwo
Group: Documentation
BuildArch: noarch

%description docs
FT is a generic, native graph management system for GNUstep and Cocoa
and is written in Objective-C. With FT you can persistently manage
graphs consisting of nodes and edges. Each node may provide so-called
services. Such a service may be e.g. a dictionary services, which all
nodes provide at present. This service allows the storage of any data in
a node and is based on keys which uniquely identify content within a
dictionary.

This package contains documentation for FortyTwo.

%prep
%setup

install -m644 %SOURCE1 .

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%_includedir/Encore' \
	CONFIG_SYSTEM_LIBS='-lBDB -lEncore -lgnustep-base -lobjc2'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in FT; do
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
%doc ANNOUNCEMENT ChangeLog README TODO
%dir %_localstatedir/GNUstep
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/FT.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/FT.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/FT.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/FT.framework/Headers

%files docs
%doc documentation/*

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

