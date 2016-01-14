%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-SourceCodeKit
Version: 0.1
Release: alt4.git20140207.1
Summary: Etoile's SourceCodeKit
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/SourceCodeKit.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gcc-c++ gnustep-Etoile-DocGenerator

Requires: gnustep-back gnustep-Etoile-EtoileFoundation

%description
Etoile's SourceCodeKit.

%package -n lib%name
Summary: Shared libraries of SourceCodeKit
Group: System/Libraries

%description -n lib%name
Etoile's SourceCodeKit.

This package contains shared libraries of SourceCodeKit.

%package -n lib%name-devel
Summary: Development files of SourceCodeKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Etoile's SourceCodeKit.

This package contains development files of SourceCodeKit.

%package docs
Summary: Documentation for SourceCodeKit
Group: Development/Documentation
BuildArch: noarch

%description docs
Etoile's SourceCodeKit.

This package contains documentation for SourceCodeKit.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=SourceCodeKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=SourceCodeKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in SourceCodeKit; do
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

install -d %buildroot%_docdir/GNUstep/SourceCodeKit
cp -fRP Documentation/* %buildroot%_docdir/GNUstep/SourceCodeKit/

%files
%doc TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/SourceCodeKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/SourceCodeKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/SourceCodeKit.framework/Headers
%_libdir/GNUstep/Frameworks/SourceCodeKit.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt4.git20140207.1
- NMU: Rebuild with libgnutls30.

* Tue Apr 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4.git20140207
- Rebuilt with llvm 3.4

* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.git20140207
- Added documentation

* Wed Mar 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.git20140207
- Added missing headers

* Wed Mar 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140207
- Initial build for Sisyphus

