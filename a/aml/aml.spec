%def_enable check

Name: aml
Version: 0.3.0
Release: alt1

Summary: Another Main Loop Library
License: ISC
Group: System/Libraries
Url: https://github.com/any1/aml

Vcs: https://github.com/any1/aml.git
Source: https://github.com/any1/aml/archive/v%version/%name-%version.tar.gz

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

%description -n lib%name-devel
This package contains header files required to develop
%name-based software.

%prep
%setup

%build
%meson \
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Thu May 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus

