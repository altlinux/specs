%set_verify_elf_method unresolved=strict

Name: gnustep-opal
Version: r35426
Release: alt2.git20120819
Summary: Vector drawing library with an API similar to Quartz 2D
License: LGPLv2.1+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-opal.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-corebase-devel libcairo-devel
BuildPreReq: liblcms-devel libjpeg-devel libtiff-devel

Requires: lib%name = %version-%release

%description
Opal is a vector drawing library with an API similar to
Quartz 2D. Opal is built on top of Cairo.

Opal is also a gemstone consisting of amorphous hydrated
silicon dioxide (SiO2 . nH2O) which is sometimes included
in the quartz group of minerals.

%package -n lib%name
Summary: Shared libraries of GNUstep's Opal
Group: System/Libraries

%description -n lib%name
Opal is a vector drawing library with an API similar to
Quartz 2D. Opal is built on top of Cairo.

Opal is also a gemstone consisting of amorphous hydrated
silicon dioxide (SiO2 . nH2O) which is sometimes included
in the quartz group of minerals.

This package contains shared libraries of Opal.

%package -n lib%name-devel
Summary: Development files of GNUstep's Opal
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Conflicts: libopal-devel

%description -n lib%name-devel
Opal is a vector drawing library with an API similar to
Quartz 2D. Opal is built on top of Cairo.

Opal is also a gemstone consisting of amorphous hydrated
silicon dioxide (SiO2 . nH2O) which is sometimes included
in the quartz group of minerals.

This package contains development files of Opal.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lX11 -lgnustep-base -lobjc2 -lm'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog README TODO
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r35426-alt2.git20120819
- Added explicit conflicts with libopal-devel

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r35426-alt1.git20120819
- Initial build for Sisyphus

