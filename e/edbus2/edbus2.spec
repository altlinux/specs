%define _name edbus
%def_disable static

Name: %{_name}2
Version: 1.7.99.83479
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Enlightenment DBUS access library
License: BSD-like
Group: System/Libraries
Url: http://www.enlightenment.org/

#VCS: git://git.enlightenment.fr/vcs/svn/IN-EFL/edbus.git
Source: http://download.enlightenment.org/releases/%_name-%version.tar.bz2

%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires: libdbus-devel  libevas-devel >= 1.7.5
BuildRequires: libecore-devel >= 1.7.5 libeina-devel >= 1.7.5
BuildRequires: doxygen

%description
EDBus provides a convenience wrapper for EFL applications using DBus.

%package -n lib%name
Summary: Enlightenment DBUS access library
Group: System/Libraries

%description -n lib%name
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.

This package contains shared library required for %name-based software.

%package -n lib%name-devel
Summary: Include files for development with Enlightenment DBUS Library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.

This package contains include files required for development %name-based software.

%package -n lib%name-devel-static
Summary: Static library for development with Enlightenment DBUS Library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.

This package contains static library required for development statically linked
%name-based software.

%prep
%ifdef beta
%setup -n %_name-%version.%beta
%else
%setup -n %_name-%version
%endif

%build
%autoreconf
%configure \
	%{subst_enable static}
%make_build
#%make doc

%install
%make_install DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS COPYING README

%files -n lib%name-devel
%_bindir/%_name-codegen
%_libdir/*.so
%_includedir/%_name-1/
%_pkgconfigdir/%name.pc


%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Feb 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.99.83479-alt1
- new version

* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.99-alt1
- first build for Sisyphus

