%def_disable snapshot
%def_enable check

Name: libdisplay-info
Version: 0.1.1
Release: alt1

Summary: EDID and DisplayID library
Group: System/Libraries
License: MIT
Url: https://emersion.pages.freedesktop.org/libdisplay-info/

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/emersion/%name/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.freedesktop.org/emersion/libdisplay-info.git
Source: %name-%version.tar
%endif

Requires: hwdata

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson hwdata-devel edid-decode

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%meson
%meson_build
%meson_build gen-test-data

%install
%meson_install

%check
%__meson_test

%files
%_bindir/di-edid-decode
%_libdir/%name.so.*
%doc README.md

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc


%changelog
* Thu May 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

