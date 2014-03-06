%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-EtoileSerialize
Version: 0.4.1
Release: alt1.svn20140217
Summary: Perform serialization and deserialization of arbitrary objects
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Frameworks/EtoileSerialize/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileFoundation

%description
This collection of classes is used by CoreObject to perform
serialization and deserialization of arbitrary objects.

So far, serialization and deserialization work for all simple types,
object, selectors and classes. Arrays and structures are believed to
work, however arrays containing structures and vice versa have not been
tested.

%package -n lib%name
Summary: Shared libraries of EtoileSerialize
Group: System/Libraries

%description -n lib%name
This collection of classes is used by CoreObject to perform
serialization and deserialization of arbitrary objects.

So far, serialization and deserialization work for all simple types,
object, selectors and classes. Arrays and structures are believed to
work, however arrays containing structures and vice versa have not been
tested.

This package contains shared libraries of EtoileSerialize.

%package -n lib%name-devel
Summary: Development files of EtoileSerialize
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
This collection of classes is used by CoreObject to perform
serialization and deserialization of arbitrary objects.

So far, serialization and deserialization work for all simple types,
object, selectors and classes. Arrays and structures are believed to
work, however arrays containing structures and vice versa have not been
tested.

This package contains development files of EtoileSerialize.

%package docs
Summary: Documentation for EtoileSerialize
Group: Development/Documentation
BuildArch: noarch

%description docs
This collection of classes is used by CoreObject to perform
serialization and deserialization of arbitrary objects.

So far, serialization and deserialization work for all simple types,
object, selectors and classes. Arrays and structures are believed to
work, however arrays containing structures and vice versa have not been
tested.

This package contains documentation for EtoileSerialize.

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
	PROJECT_NAME=EtoileSerialize

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=EtoileSerialize

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in EtoileSerialize; do
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
%doc NEWS README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/EtoileSerialize.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/EtoileSerialize.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/EtoileSerialize.framework/Headers
%_libdir/GNUstep/Frameworks/EtoileSerialize.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.svn20140217
- Initial build for Sisyphus

