%def_disable snapshot
%define api_ver 1.0

%def_disable python
%def_enable check

Name: libimobiledevice-glue
Version: 1.3.2
Release: alt1

Summary: libimobiledevice common library
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://www.libimobiledevice.org

Vcs: https://github.com/libimobiledevice/libimobiledevice-glue.git

%if_disabled snapshot
Source: https://github.com/libimobiledevice/libimobiledevice-glue/releases/download/%version/%name-%version.tar.bz2
%else
Source: %name-%version.tar
%endif

%define plist_ver 2.7.0

BuildRequires: pkgconfig(libplist-2.0) >= %plist_ver

%description
Library with common code used by the libraries and tools around the
libimobiledevice project.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides files for development using %name.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static
%nil
%make_build

%install
%makeinstall_std

%check
%make -k check VERBOSE=1

%files
%_libdir/%name-%api_ver.so.*
%doc NEWS README*

%files devel
%_includedir/%name
%_libdir/%name-%api_ver.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jun 16 2025 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- first build for Sisyphus

