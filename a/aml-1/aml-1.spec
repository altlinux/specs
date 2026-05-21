%def_enable snapshot
%def_enable check

%define _name aml
%define sover 1
%define api_ver 1

Name: %_name-%api_ver
Version: 1.0.0
Release: alt1

Summary: Another Main Loop Library
License: ISC
Group: System/Libraries
Url: https://github.com/any1/aml

Vcs: https://github.com/any1/aml.git

%if_disabled snapshot
Source: https://github.com/any1/aml/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
%summary

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
This package contains shared Andri's Main Loop library.

%package -n lib%name-devel
Summary: lib%name development files
Group: Development/C
Requires: lib%name = %EVR
Conflicts: lib%_name-devel < %version

%description -n lib%name-devel
This package contains header files required to develop
%name-based software.

%prep
%setup -n %_name-%version

%build
%meson
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n lib%name
%_libdir/lib%_name.so.%{sover}*

%files -n lib%name-devel
%_includedir/%_name%api_ver/
%_libdir/lib%_name.so
%_pkgconfigdir/%_name%api_ver.pc

%changelog
* Thu May 21 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- v1.0.0-3-gce4b82d (ALT #58915)

* Fri Nov 29 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1.1
- spec: fixed typo

* Thu May 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus

