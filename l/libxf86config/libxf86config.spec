Name: libxf86config
Version: 1.0
Release: alt2

Summary: A library for reading and writing xorg configuration files
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Vladislav Zavjalov <slazav@altlinux.org>
Obsoletes: libxorgconfig
Provides:  libxorgconfig = 1.6.5-alt1
BuildRequires: libX11-devel

Source: %name-%version.tar

%package devel
Summary: Development tools for programs which will use the libxf86config library
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libxorgconfig-devel
Provides:  libxorgconfig-devel = 1.6.5-alt1

%package devel-static
Summary: Static libxf86config library
Group: Development/C
Requires: %name-devel = %version-%release
Obsoletes: libxorgconfig-devel-static
Provides:  libxorgconfig-devel-static = 1.6.5-alt1

%description
This package contains a shared library for reading and writing xorg
configuration files.

%description devel
This package contains files necessary for developing programs
which use libxf86config library for reading and writing xorg
configuration files.

%description devel-static
This package contains static library necessary for developing
statically linked programs which use libxf86config library for
reading and writing xorg configuration files.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a


%changelog
* Thu Oct 21 2010 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- rebuild for soname set-versions

* Tue Nov 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- initial build: move libxf86config library from xorg-server
  (libxorgconfig subpackage) into separate package

