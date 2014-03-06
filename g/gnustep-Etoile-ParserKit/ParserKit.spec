#set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-ParserKit
Version: 0.1
Release: alt1.git20140225
Summary: Etoile's ParserKit
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/ParserKit.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-Languages-devel gnustep-Etoile-UnitKit-devel

Requires: lib%name = %EVR
Requires: gnustep-back
Requires: gnustep-Etoile-Languages gnustep-Etoile-UnitKit

%description
Etoile's ParserKit.

%package -n lib%name
Summary: Shared libraries of ParserKit
Group: System/Libraries

%description -n lib%name
Etoile's ParserKit.

This package contains shared libraries of ParserKit.

%package -n lib%name-devel
Summary: Development files of ParserKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Etoile's ParserKit.

This package contains development files of ParserKit.

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
	PROJECT_NAME=ParserKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=ParserKit

#install -d %buildroot%_libdir/obj/ParserKit.bundle/Resources
#install -m644 obj/ParserKit.bundle/Resources/out.so \
#	%buildroot%_libdir/obj/ParserKit.bundle/Resources/

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in ParserKit; do
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

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%_libdir/GNUstep/Frameworks/ParserKit.framework
%exclude %_libdir/GNUstep/Frameworks/ParserKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/ParserKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/ParserKit.framework/Headers
%_libdir/GNUstep/Frameworks/ParserKit.framework/Versions/0/Headers

# TODO: enable smalltalk (see GNUmakefile)

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140225
- Initial build for Sisyphus

