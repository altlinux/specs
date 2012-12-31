%set_verify_elf_method unresolved=strict

Name: gnustep-webservices
Version: 0.5.9
Release: alt3.git20121208
Summary: WebServices framework for GNUstep
License: LGPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-webservices.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-performance-devel /proc
BuildPreReq: gnustep-performance-devel

%description
The WebServer library contains a collection of classes to be used
for creating client and server 'web service' applications.

%package -n lib%name
Summary: WebServices framework for GNUstep
Group: System/Libraries

%description -n lib%name
The WebServer library contains a collection of classes to be used
for creating client and server 'web service' applications.

This package contains shared libraries of WebServices framework for
GNUstep.

%package -n lib%name-devel
Summary: Development files of WebServices framework for GNUstep
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The WebServer library contains a collection of classes to be used
for creating client and server 'web service' applications.

This package contains development files of WebServices framework for
GNUstep.

%package -n lib%name-devel-doc
Summary: Documentation for WebServices framework for GNUstep
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The WebServer library contains a collection of classes to be used
for creating client and server 'web service' applications.

This package contains development documentation for WebServices
framework for GNUstep.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

cp -fR Examples %buildroot%_docdir/GNUstep/WebServices/

%files -n lib%name
%doc WebServices.gsdoc README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/GNUstep

%changelog
* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt3.git20121208
- Rebuilt with libobjc2 instead of libobjc

* Fri Dec 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt2.git20121208
- Rubilt with updaded glibc

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt1.git20121208
- Initial build for Sisyphus

