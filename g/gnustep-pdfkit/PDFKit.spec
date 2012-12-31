Name: gnustep-pdfkit
Version: 0.9.2
Release: alt3
Summary: A Framework for accessing and rendering PDF content
License: GPLv2 only
Group: File tools
Url: http://wiki.gnustep.org/index.php/PDFKit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: gcc-c++ libfreetype-devel gcc-objc gnustep-make-devel
BuildPreReq: gnustep-base-devel libgnustep-objc2-devel gnustep-gui-devel

Source: %name-%version.tar

%description
Kit for displaying PDFs in a View, based on xpdf.

%package -n lib%name
Summary: Shared libraries of PDFKit
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
Kit for displaying PDFs in a View, based on xpdf.

This package contains shared libraries of PDFKit.

%package -n lib%name-devel
Summary: Development files of PDFKit
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
Kit for displaying PDFs in a View, based on xpdf.

This package contains development files of PDFKit.

%prep
%setup

%build
export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
%add_optflags %optflags_shared
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-freetype2-library=%prefix \
	--with-freetype2-includes=%_includedir/freetype2 \
	--with-installation-domain=SYSTEM

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2'
 
%install
%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/PDFKit.framework/Versions/Current/$i ./
	ln -s %_libdir/$i \
		GNUstep/Frameworks/PDFKit.framework/Versions/Current/
done
popd

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/Versions/0/libPDFKit.so \
	%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/Versions/0/PDFKit \
	%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/libPDFKit.so \
	%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/PDFKit
pushd %buildroot%_libdir
for i in libPDFKit.so.*.*; do
	ln -s %_libdir/$i \
		%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/Versions/0/libPDFKit.so
	ln -s %_libdir/$i \
		%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/Versions/0/PDFKit
	ln -s %_libdir/$i \
		%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/libPDFKit.so
	ln -s %_libdir/$i \
		%buildroot%_libdir/GNUstep/Frameworks/PDFKit.framework/PDFKit
done
popd

%files
%doc Documentation/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/PDFKit.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/PDFKit.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/PDFKit.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/PDFKit.framework/Headers

%changelog
* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3
- Don't required devel packages for runtime packages

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2
- Moved shared libraries into %_libdir

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus

