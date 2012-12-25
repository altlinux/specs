
Name: deepsolver
Version: 0.2.5
Release: alt1

Packager: Michael Pozhidaev <msp@altlinux.ru>
License: GPL v2+
URL: http://deepsolver.org/

Summary: The package manager
Group: System/Configuration/Packaging

Source: %name-%version.tar.gz
Source2: ds.conf
Source3: msp.repo
Source4: altlinux-release.provide

BuildRequires: gcc-c++ librpm-devel libcurl-devel zlib-devel
BuildRequires: libminisat-devel >= 2.2.0-alt2

%package -n lib%name
Summary: The dynamically linked library with Deepsolver functions
Group: System/Libraries

%package -n lib%name-devel
Summary: C/C++ development files for lib%name
Group: Development/C
Requires: lib%name 

%package -n lib%name-devel-static
Summary: The static library with Deepsolver functions
Group: Development/C
Requires: lib%name-devel 

%package repo
Summary: The utilities for Deepsolver repository administration
Group: System/Configuration/Packaging
Requires: %name
Requires: lib%name = %version-%release

%description
Deepsolver is a package manipulation tool for GNU/Linux system. It
basically designed for ALT Linux RPM environment but in hope it can be
useful for other distributions or even for other package managers.

Main design goals include flexibility, reliability and small execution
time. The core system for package dependency processing is based on
robust 2-SAT algorithm. The tool aims to be a useful instrument both for
users and system administrators. It also includes features to be
appropriate for ALT Linux package building environment.

%description -n lib%name
Deepsolver is a package manipulation tool for GNU/Linux system. It
basically designed for ALT Linux RPM environment but in hope it can be
useful for other distributions or even for other package managers.

Main design goals include flexibility, reliability and small execution
time. The core system for package dependency processing is based on
robust 2-SAT algorithm. The tool aims to be a useful instrument both for
users and system administrators. It also includes features to be
appropriate for ALT Linux package building environment.

This package contains the dynamically linked library with Deepsolver functions

%description -n lib%name-devel
C/C++ development files for lib%name.

%description -n lib%name-devel-static
The static library with Deepsolver functions.

%description repo
This package contains set of utilities purposed for various tasks of
Deepsolver repository administration. With these utilities you can
create new repository and change set of packages in it. Deepsolver
supports package including/excluding without full reconstruction of
repository index data what significantly reduces time.

%prep
%setup -q
%build
%__libtoolize
%autoreconf
%configure
%make_build

%install
make DESTDIR=%buildroot install 

%__rm -f %buildroot%_libdir/lib%name.la

%__install -d -m 755 %buildroot%_sysconfdir/%name
%__install -d -m 755 %buildroot%_sysconfdir/%name/conf.d
%__install -pD -m 644 %SOURCE2 %buildroot%_sysconfdir/%name/
%__install -pD -m 644 %SOURCE3 %buildroot%_sysconfdir/%name/conf.d/
%__install -pD -m 644 %SOURCE4 %buildroot%_sysconfdir/%name/conf.d/
%__subst s/i586/%_arch/ %buildroot%_sysconfdir/%name/conf.d/msp.repo


%__install -d -m 755 %buildroot%_localstatedir/%name

%files
%doc AUTHORS COPYING NEWS README ChangeLog doc/ru/user-manual/user-manual.pdf
%_bindir/ds-conf
%_bindir/ds-install
%_bindir/ds-remove
%_bindir/ds-update
%config(noreplace) %_sysconfdir/%name
%_localstatedir/%name

%files -n lib%name
%_libdir/lib%name-*.so*

%files -n lib%name-devel
%_libdir/lib%name.so

%files -n lib%name-devel-static
%_libdir/lib%name.a

%files repo
%_bindir/ds-repo
%_bindir/ds-patch
%_bindir/ds-provides

%changelog
* Wed Dec 26 2012 Michael Pozhidaev <msp@altlinux.ru> 0.2.5-alt1
- New version

* Tue Oct 16 2012 Michael Pozhidaev <msp@altlinux.ru> 0.1.1-alt1
- New version (ds-patch utility now has --add-list and --del-list command line options)

* Fri Sep 28 2012 Michael Pozhidaev <msp@altlinux.ru> 0.1.0-alt1
-Initial package 

