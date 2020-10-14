%set_verify_elf_method unresolved=strict

Name: gnustep-gsgd
Version: r31302
Release: alt5
Summary: Objc interface to libgd library
License: LGPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

# https://github.com/gnustep/gnustep-gsgd.git
Source: %name-%version.tar
Patch1: link-libs.patch

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-base-devel libgd3-devel

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
%patch1 -p1

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-installation-domain=SYSTEM

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%doc ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> r31302-alt5
- Build without libgnustep-objc2-devel.

* Mon Apr 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> r31302-alt4.git20100910.1
- (NMU) rebuilt with new libgd.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31302-alt4.git20100910
- Built with clang

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31302-alt3.git20100910
- Rebuilt with new gnustep-gui

* Fri Jan 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31302-alt2.git20100910
- Rebuilt with libgd2 instead of libgd

* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31302-alt1.git20100910
- Initial build for Sisyphus

