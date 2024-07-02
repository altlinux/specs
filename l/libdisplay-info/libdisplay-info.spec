%def_disable snapshot
%def_enable check

# subprojects/edid-decode.wrap
%define edid_decode_ver c6b859d7f0251e2433fb81bd3f67bd2011c2036c
%def_disable edid_decode_as_subproject

Name: libdisplay-info
Version: 0.2.0
Release: alt1

Summary: EDID and DisplayID library
Group: System/Libraries
License: MIT
Url: https://emersion.pages.freedesktop.org/libdisplay-info/

Vcs: https://gitlab.freedesktop.org/emersion/libdisplay-info.git

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/emersion/%name/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
# https://git.linuxtv.org/edid-decode.git
%{?_enable_edid_decode_as_subproject:Source1: edid-decode-%edid_decode_ver.tar}

Requires: hwdata

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson hwdata-devel edid-decode
# edid-decode required to generate test data
BuildRequires: edid-decode

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
%setup %{?_enable_edid_decode_as_subproject:-a1
mv edid-decode-%edid_decode_ver subprojects/edid-decode}

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
* Fri Jun 21 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Thu May 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

