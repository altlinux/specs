%set_verify_elf_method unresolved=strict

Name: gnustep-ObjectiveLib
Version: 1.0.0
Release: alt1
Summary: A library for Objective-C
License: LGPLv2
Group: Graphical desktop/GNUstep
Url: http://sourceforge.net/projects/objectivelib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gcc-c++ gcc-fortran
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-pbxbuild bzlib-devel doxygen graphviz

%description
ObjectiveLib is a library for Objective-C that provides a full set of
object containers, generic algorithms and binary streams. It provides
the same services to Objective-C programmers that the Standard Template
Library provides to C++ programmers.

%package -n lib%name
Summary: A library for Objective-C
Group: System/Libraries

%description -n lib%name
ObjectiveLib is a library for Objective-C that provides a full set of
object containers, generic algorithms and binary streams. It provides
the same services to Objective-C programmers that the Standard Template
Library provides to C++ programmers.

%package -n lib%name-devel
Summary: Development files of ObjectiveLib
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
ObjectiveLib is a library for Objective-C that provides a full set of
object containers, generic algorithms and binary streams. It provides
the same services to Objective-C programmers that the Standard Template
Library provides to C++ programmers.

This package contains development files of ObjectiveLib.

%package -n lib%name-devel-doc
Summary: Documentation for ObjectiveLib
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
ObjectiveLib is a library for Objective-C that provides a full set of
object containers, generic algorithms and binary streams. It provides
the same services to Objective-C programmers that the Standard Template
Library provides to C++ programmers.

This package contains development documentation for ObjectiveLib.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

rm -f RunTime.h
ln -s %_includedir/objc2/runtime.h RunTime.h

%build
%autoreconf
%configure \
	--enable-static=no \
	--with-xcodebuild=%_bindir/pbxbuild \
	--with-doxygen=%_bindir/doxygen \
	--with-dot=%_bindir/dot \
	--with-fwk-dir=%_libdir/GNUstep/Frameworks \
	--with-doc-dir=%buildroot%_docdir/GNUstep \
	--with-gnustep \
	--with-zlib \
	--with-bzlib \
	--with-threads=posix

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -I%_includedir/objc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	STRIP_PROG=echo
 
%install
install -d %buildroot%_docdir/GNUstep

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/GNUstep

%changelog
* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

