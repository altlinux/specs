%set_verify_elf_method unresolved=strict

Name: gnustep-gsgd
Version: r31302
Release: alt2.git20100910
Summary: Objc interface to libgd library
License: LGPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-gsgd.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel libgd2-devel

%description
gsgd is an Objc interface to libgd library. libgd is a library to create
PNG and Jpeg images.

%package -n lib%name
Summary: Shared libraries of Objc interface to libgd library
Group: System/Libraries

%description -n lib%name
gsgd is an Objc interface to libgd library. libgd is a library to create
PNG and Jpeg images.

This package contains shared libraries of gsgd.

%package -n lib%name-devel
Summary: Shared libraries of Objc interface to libgd library
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
gsgd is an Objc interface to libgd library. libgd is a library to create
PNG and Jpeg images.

This package contains development files of gsgd.

%prep
%setup

%build
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-installation-domain=SYSTEM

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%doc ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri Jan 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31302-alt2.git20100910
- Rebuilt with libgd2 instead of libgd

* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31302-alt1.git20100910
- Initial build for Sisyphus

