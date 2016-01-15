%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-IconKit
Version: 0.2
Release: alt2.git20130801.1
Summary: Provides icon theming and various facilities to create icons at run-time
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/IconKit.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator

Requires: lib%name = %EVR
Requires: gnustep-back

%description
This framework provides icon theming and various facilities to create
icons at run-time by compositing by different elements.
The icon compositing is very useful for the consistency accross a set of
icons (for example, using the same background) and permit to easily
create icon families.
IconKit icon themes are a complement to Camaelon widget themes.

%package -n lib%name
Summary: Shared libraries of IconKit
Group: System/Libraries

%description -n lib%name
This framework provides icon theming and various facilities to create
icons at run-time by compositing by different elements.
The icon compositing is very useful for the consistency accross a set of
icons (for example, using the same background) and permit to easily
create icon families.
IconKit icon themes are a complement to Camaelon widget themes.

This package contains shared libraries of IconKit.

%package -n lib%name-devel
Summary: Development files of IconKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
This framework provides icon theming and various facilities to create
icons at run-time by compositing by different elements.
The icon compositing is very useful for the consistency accross a set of
icons (for example, using the same background) and permit to easily
create icon families.
IconKit icon themes are a complement to Camaelon widget themes.

This package contains development files of IconKit.

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
	PROJECT_NAME=IconKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=IconKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in IconKit; do
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

install -d %buildroot%_libdir/GNUstep/Themes/Icon
ln -s \
	%_libdir/GNUstep/Frameworks/IconKit.framework/Resources/GNUstep.icontheme \
	%buildroot%_libdir/GNUstep/Themes/Icon/

%files
%doc ChangeLog NEWS README TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/IconKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/IconKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/IconKit.framework/Headers
%_libdir/GNUstep/Frameworks/IconKit.framework/Versions/0/Headers

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.git20130801.1
- NMU: Rebuild with libgnutls30.

* Fri Mar 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.git20130801
- Added link for path to icons

* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20130801
- Initial build for Sisyphus

