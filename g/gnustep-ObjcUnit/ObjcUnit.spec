%set_verify_elf_method unresolved=strict

Name: gnustep-ObjcUnit
Version: 1.2
Release: alt1
Summary: ObjcUnit framework for GNUstep
License: IBM Public License Version 1.0
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/ObjcUnit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR

%description
ObjcUnit is a unit testing framework for Objective-C originally on Mac
OS X. Its design was copied from JUnit, written by Erich Gamma and Kent
Beck, and then adapted somewhat for Objective-C. Authored by Malte
Tancred and Peter Lindberg and adapted for GNUstep by Ken Causey.

ObjcUnit is currently known to be used by the Zipper program and
FlexiSheet.

%package -n lib%name
Summary: Shared libraries of ObjcUnit
Group: System/Libraries

%description -n lib%name
ObjcUnit is a unit testing framework for Objective-C originally on Mac
OS X. Its design was copied from JUnit, written by Erich Gamma and Kent
Beck, and then adapted somewhat for Objective-C. Authored by Malte
Tancred and Peter Lindberg and adapted for GNUstep by Ken Causey.

This package contains shared libraries of ObjcUnit.

%package -n lib%name-devel
Summary: Development files of ObjcUnit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
ObjcUnit is a unit testing framework for Objective-C originally on Mac
OS X. Its design was copied from JUnit, written by Erich Gamma and Kent
Beck, and then adapted somewhat for Objective-C. Authored by Malte
Tancred and Peter Lindberg and adapted for GNUstep by Ken Causey.

This package contains development files of ObjcUnit.

%package docs
Summary: Documentation for ObjcUnit
Group: Documentation
BuildArch: noarch

%description docs
ObjcUnit is a unit testing framework for Objective-C originally on Mac
OS X. Its design was copied from JUnit, written by Erich Gamma and Kent
Beck, and then adapted somewhat for Objective-C. Authored by Malte
Tancred and Peter Lindberg and adapted for GNUstep by Ken Causey.

This package contains documentation for ObjcUnit.

%prep
%setup

%build
%make_build -C ObjcUnit \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std -C ObjcUnit GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for j in ObjcUnit; do
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
%doc *.rtf
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/ObjcUnit.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/ObjcUnit.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/ObjcUnit.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/ObjcUnit.framework/Headers

%files docs
%doc ObjcUnit/Documentation/*

%changelog
* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

