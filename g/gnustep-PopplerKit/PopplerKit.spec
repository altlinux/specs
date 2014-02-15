%set_verify_elf_method unresolved=strict

Name: gnustep-PopplerKit
Version: 0.0.20051227svn
Release: alt3
Summary: GNUstep framework for rendering PDF content
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/jessie/libpopplerkit-dev
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gcc-c++
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libpoppler-devel fontconfig-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
PopplerKit is a GNUstep framework for accessing and rendering PDF
content. It is based on the poppler library.

Its features are:

- Render PDF content.
- Extract text from a PDF document.
- Access a PDF document's outline.
- Search in PDF documents.

%package -n lib%name
Summary: Shared libraries of PopplerKit
Group: System/Libraries

%description -n lib%name
PopplerKit is a GNUstep framework for accessing and rendering PDF
content. It is based on the poppler library.

This package contains shared libraries of PopplerKit.

%package -n lib%name-devel
Summary: Development files of PopplerKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
PopplerKit is a GNUstep framework for accessing and rendering PDF
content. It is based on the poppler library.

This package contains development files of PopplerKit.

%prep
%setup

for i in $(find ./ -name '*.cc'); do
	file=$(echo $i |sed 's|\.cc|.c|')
	mv $i $file
done

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-DPOPPLER_0_20 -DPOPPLER_0_5 -I%_includedir/poppler'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in PopplerKit; do
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

%files
%doc docs/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/PopplerKit.framework/Versions/1.0/Headers
%exclude %_libdir/GNUstep/Frameworks/PopplerKit.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/PopplerKit.framework/Versions/1.0/Headers
%_libdir/GNUstep/Frameworks/PopplerKit.framework/Headers

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.20051227svn-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.20051227svn-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.20051227svn-alt1
- Initial build for Sisyphus

