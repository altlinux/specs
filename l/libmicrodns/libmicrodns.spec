%define _name microdns

%def_disable snapshot
%def_enable examples
%def_enable check

Name: lib%_name
Version: 0.2.0
Release: alt1

Summary: Minimal mDNS resolver (and announcer) library
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/videolabs/libmicrodns

Vcs: https://github.com/videolabs/libmicrodns.git

%if_disabled snapshot
Source: https://github.com/videolabs/libmicrodns/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
This library is still in development, and therefore can still have bugs.
The goal is to have a simple library to listen and create mDNS announces,
without the complexity of larger libraries like *avahi*.
This means that the API is quite low-level and that the code is in C.

%package devel
Summary: %name development package
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_feature check tests} \
    %{subst_enable_meson_feature examples examples}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name.so.*
%doc README*

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_pkgconfigdir/%_name.pc

%changelog
* Mon Dec 29 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus


