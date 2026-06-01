%def_enable check

%define sover 1

Name: qrtr
Version: 1.2
Release: alt1

Summary: Userspace reference for net/qrtr in the Linux kernel
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/linux-msm/qrtr

Vcs: https://github.com/linux-msm/qrtr.git

Source: https://github.com/linux-msm/qrtr/archive/v%version/%name-%version.tar.gz

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
%meson
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n lib%name
%_bindir/%name-cfg
%_bindir/%name-lookup
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_includedir/lib%name.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Mon Jun 01 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- first build for Sisyphus

