%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-EtoileText
Version: 0.1
Release: alt1.git20131205.1
Summary: EtoileText framework
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/EtoileText.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-Etoile-CoreObject-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-SourceCodeKit-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-CoreObject
Requires: gnustep-Etoile-EtoileFoundation gnustep-Etoile-SourceCodeKit

%description
EtoileText framework.

%package -n lib%name
Summary: Shared libraries of EtoileText framework
Group: System/Libraries

%description -n lib%name
EtoileText framework.

This package contains shared libraries of EtoileText framework.

%package -n lib%name-devel
Summary: Development files of EtoileText framework
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
EtoileText framework.

This package contains development files of EtoileText framework.

%package docs
Summary: Documentation for EtoileText framework
Group: Development/Documentation
BuildArch: noarch

%description docs
EtoileText framework.

This package contains documentation for EtoileText framework.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=EtoileText

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=EtoileText

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in EtoileText; do
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

install -d %buildroot%_docdir/GNUstep/EtoileText
cp -fRP Documentation/* %buildroot%_docdir/GNUstep/EtoileText/

%files
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/EtoileText.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/EtoileText.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/EtoileText.framework/Headers
%_libdir/GNUstep/Frameworks/EtoileText.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20131205.1
- NMU: Rebuild with libgnutls30.

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20131205
- Initial build for Sisyphus

