%define _unpackaged_files_terminate_build 1
%define sover 1
%def_enable check

Name: libqrtr
Version: 1.2
Release: alt2
Summary: Userspace reference for net/qrtr in the Linux kernel
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/linux-msm/qrtr
VCS: https://github.com/linux-msm/qrtr.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
%summary

%package -n %name%sover
Summary: Userspace reference for net/qrtr in the Linux kernel
Group: System/Libraries
Provides: %name = %EVR

%description -n %name%sover
%summary

%package devel
Summary: Development files for libqrtr
Group: Development/C
Requires: %name%sover = %EVR

%description devel
%summary

%package -n qrtr-tools
Summary: Various qrtr tools
Group: System/Kernel and hardware
Requires: %name%sover = %EVR
Provides: libqrtr = %EVR
Obsoletes: libqrtr < %EVR

%description -n qrtr-tools
%summary

%prep
%setup

%build
%meson -Dqrtr-ns=disabled
%meson_build -v

%install
%meson_install

%check
%__meson_test

%files -n %name%sover
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*

%files devel
%_libdir/%name.so
%_includedir/%name.h
%_pkgconfigdir/qrtr.pc

%files -n qrtr-tools
%_bindir/qrtr-*

%changelog
* Mon Jun 15 2026 Vasiliy Doylov <neko@altlinux.org> 1.2-alt2
- Return hijacked package.

* Tue Apr 14 2026 Vasiliy Doylov <neko@altlinux.org> 1.2-alt1
- Initial package.
