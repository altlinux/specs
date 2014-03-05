%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-UnitKit
Version: 1.3
Release: alt2.git20140301
Summary: Minimalistic unit testing framework
License: Apache License v2
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/UnitKit.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator

Requires: lib%name = %EVR
Requires: gnustep-back

%description
UnitKit is a minimalistic unit testing framework that supports Mac OS X,
iOS and GNUstep.

The framework is less than 2000 loc, and built around two classes
UKRunner and UKTestHandler, plus some test macros, and an empty protocol
UKTest to mark test classes.

The UnitKit core features are:

- Test assertion macros
- easy to write and read
- without useless arguments
- not too many ones
- extensible (implement a UKTestHandler subclass or category)
- No test case class, just adopt UKTest protocol
- No special methods -setUp and -tearDown, just implement -init and and
  -dealloc
- Class test methods in addition to instance ones
- Run loop integration for asynchronous testing
- Uncaught exception reporting
- Delegate methods to signal a test suite will start or just ended
- Tested class choice based on a regex
- Verbose and quiet ouput
- Optional ukrun tool to run test suites packaged in test bundles
- Xcode 3 and higher test suite templates

%package -n lib%name
Summary: Shared libraries of UnitKit
Group: System/Libraries

%description -n lib%name
UnitKit is a minimalistic unit testing framework that supports Mac OS X,
iOS and GNUstep.

The framework is less than 2000 loc, and built around two classes
UKRunner and UKTestHandler, plus some test macros, and an empty protocol
UKTest to mark test classes.

This package contains shared libraries of UnitKit.

%package -n lib%name-devel
Summary: Development files of UnitKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
UnitKit is a minimalistic unit testing framework that supports Mac OS X,
iOS and GNUstep.

The framework is less than 2000 loc, and built around two classes
UKRunner and UKTestHandler, plus some test macros, and an empty protocol
UKTest to mark test classes.

This package contains development files of UnitKit.

%package tests
Summary: Test framework and test bundle of UnitKit
Group: Development/Objective-C
Requires: %name = %EVR
Requires: lib%name-tests = %EVR

%description tests
UnitKit is a minimalistic unit testing framework that supports Mac OS X,
iOS and GNUstep.

The framework is less than 2000 loc, and built around two classes
UKRunner and UKTestHandler, plus some test macros, and an empty protocol
UKTest to mark test classes.

This package contains test framework and test bundle of UnitKit.

%package -n lib%name-tests
Summary: Shared libraries of test framework and test bundle of UnitKit
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-tests
UnitKit is a minimalistic unit testing framework that supports Mac OS X,
iOS and GNUstep.

The framework is less than 2000 loc, and built around two classes
UKRunner and UKTestHandler, plus some test macros, and an empty protocol
UKTest to mark test classes.

This package contains shared libraries of test framework and test bundle
of UnitKit.

%package -n lib%name-tests-devel
Summary: Development files of test framework and test bundle of UnitKit
Group: Development/Objective-C
Provides: %name-tests-devel = %EVR
Requires: %name-tests = %EVR
Requires: lib%name-tests = %EVR

%description -n lib%name-tests-devel
UnitKit is a minimalistic unit testing framework that supports Mac OS X,
iOS and GNUstep.

The framework is less than 2000 loc, and built around two classes
UKRunner and UKTestHandler, plus some test macros, and an empty protocol
UKTest to mark test classes.

This package contains development files of test framework and test
bundle of UnitKit.

%package docs
Summary: Documentation for UnitKit
Group: Development/Documentation
BuildArch: noarch

%description docs
UnitKit is a minimalistic unit testing framework that supports Mac OS X,
iOS and GNUstep.

The framework is less than 2000 loc, and built around two classes
UKRunner and UKTestHandler, plus some test macros, and an empty protocol
UKTest to mark test classes.

This package contains documentation for UnitKit.

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
	test=yes \
	testsource=yes \
	AUXILIARY_CPPFLAGS="-I$PWD/TestSource" \
	documentation=yes \
	PROJECT_NAME=UnitKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	test=yes \
	testsource=yes \
	PROJECT_NAME=UnitKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/UnitKit.framework/UnitKit.framework

pushd %buildroot%_libdir
for j in TestFramework UnitKit; do
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

install -d %buildroot%_docdir/GNUstep/UnitKit
cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%doc NEWS.md NOTICE README.md TODO.md
%_bindir/*
%_libdir/GNUstep/Frameworks/UnitKit.framework
%exclude %_libdir/GNUstep/Frameworks/UnitKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/UnitKit.framework/Versions/1/Headers

%files -n lib%name
%_libdir/libUnitKit.so.*

%files -n lib%name-devel
%_includedir/UnitKit
%_libdir/libUnitKit.so
%_libdir/GNUstep/Frameworks/UnitKit.framework/Headers
%_libdir/GNUstep/Frameworks/UnitKit.framework/Versions/1/Headers

%files tests
%_libdir/GNUstep/Bundles/TestBundle.bundle
%_libdir/GNUstep/Bundles/TestUnitKit.bundle
%_libdir/GNUstep/Frameworks/TestFramework.framework
%exclude %_libdir/GNUstep/Frameworks/TestFramework.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/TestFramework.framework/Versions/0/Headers

%files -n lib%name-tests
%_libdir/libTestFramework.so.*

%files -n lib%name-tests-devel
%_includedir/TestBundle
%_includedir/TestFramework
%_libdir/libTestFramework.so
%_libdir/GNUstep/Frameworks/TestFramework.framework/Headers
%_libdir/GNUstep/Frameworks/TestFramework.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Wed Mar 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2.git20140301
- Added documentation

* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140301
- Initial build for Sisyphus

