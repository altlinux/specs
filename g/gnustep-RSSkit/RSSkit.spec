%set_verify_elf_method unresolved=strict

Name: gnustep-RSSkit
Version: 0.4.0
Release: alt4.1
Summary: Simple library for reading the different types of RSS file formats
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/grr/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: doxygen gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

%package -n lib%name
Summary: Shared libraries of RSSKit
Group: System/Libraries

%description -n lib%name
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

This package contains shared libraries of RSSKit.

%package -n lib%name-devel
Summary: Development files of RSSKit
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

This package contains development files of RSSKit.

%package -n lib%name-devel-docs
Summary: Documentation for RSSKit
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

This package contains development documentation for RSSKit.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes

doxygen doxygen
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in RSSKit; do
	lib=$(ls lib$i.so.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/0/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/0/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$i
done
popd

%files
%doc AUTHORS INTRO README TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files -n lib%name-devel-docs
%doc Documentation/html/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt4.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt4
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Rebuilt with new gnustep-gui

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

