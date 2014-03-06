%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-AddressBook
Version: 0.1
Release: alt1.svn20120426
Summary: Etoile's AddressBook
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Frameworks/AddressBook/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-Etoile-CoreObject-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-CoreObject

%description
Etoile's AddressBook.

%package -n lib%name
Summary: Shared libraries of AddressBook
Group: System/Libraries

%description -n lib%name
Etoile's AddressBook.

This package contains shared libraries of AddressBook.

%package -n lib%name-devel
Summary: Development files of AddressBook
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Etoile's AddressBook.

This package contains development files of AddressBook.

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
	documentation=no \
	PROJECT_NAME=AddressBook

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=no \
	PROJECT_NAME=AddressBook

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in AddressBook; do
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
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/AddressBook.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/AddressBook.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/AddressBook.framework/Headers
%_libdir/GNUstep/Frameworks/AddressBook.framework/Versions/0/Headers

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20120426
- Initial build for Sisyphus

