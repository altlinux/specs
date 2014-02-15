%set_verify_elf_method unresolved=strict

Name: gnustep-libId3
Version: 2006
Release: alt3
Summary: libid3 library
License: LGPLv2.1
Group: System/Libraries
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: zlib-devel gnustep-gui-devel

%description
libid3 library.

%package devel
Summary: Development files of libid3
Group: Development/Objective-C
Requires: %name = %EVR

%description devel
libid3 library.

This package contains development files of libid3.

%prep
%setup -n libid3

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2 -lz'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt3
- Built with clang

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt2
- Rebuilt with new gnustep-gui

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt1
- Initial build for Sisyphus

