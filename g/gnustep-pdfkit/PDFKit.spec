Name: gnustep-pdfkit
Version: 0.9.3
Release: alt5.1
Summary: A Framework for accessing and rendering PDF content
License: GPLv2 only
Group: File tools
Url: http://wiki.gnustep.org/index.php/PDFKit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
ExcludeArch: aarch64

BuildPreReq: gcc-c++ libfreetype-devel clang-devel gnustep-make-devel
BuildPreReq: gnustep-base-devel libgnustep-objc2-devel gnustep-gui-devel

Source: %name-%version.tar

Requires: gnustep-back

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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%add_optflags %optflags_shared
%remove_optflags -frecord-gcc-switches
export CC=clang
export CXX=clang++
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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

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

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

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
* Mon Feb 04 2019 Ivan A. Melnikov <iv@altlinux.org> 0.9.3-alt5.1
- Fix FTBFS.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt5
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt4
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt3
- Rebuilt with new gnustep-gui

* Thu Oct 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt2
- Applied repocop patch

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Version 0.9.3

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3
- Don't required devel packages for runtime packages

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2
- Moved shared libraries into %_libdir

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus

