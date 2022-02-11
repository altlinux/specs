%define _unpackaged_files_terminate_build 1

Name:     ipmctl
Version:  02.00.00.3885
Release:  alt1

Summary:  ipmctl is a utility for configuring and managing Intel Optane Persistent Memory modules (PMem)
License:  BSD-3-Clause
Group:    System/Configuration/Hardware
Url:      https://github.com/intel/ipmctl

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++
BuildRequires: libndctl-devel
BuildRequires: libsystemd-devel
BuildRequires: asciidoc-a2x

%description
ipmctl is a utility for configuring and managing Intel Optane Persistent
Memory modules (PMem).

It supports functionality to:
- Discover PMems on the platform.
- Provision the platform memory configuration.
- View and update the firmware on PMems.
- Configure data-at-rest security on PMems.
- Track health and performance of PMems.
- Debug and troubleshoot PMems.

%package -n libipmctl
Summary: Library for Intel DCPMM management
Group: System/Libraries

%description -n libipmctl
%summary

%package -n libipmctl-devel
Summary: Development packages for libipmctl
Group: Development/C++

%description -n libipmctl-devel
%summary

%prep
%setup

%build
#    -DCMAKE_INSTALL_PREFIX=/ \
#    -DLINUX_PRODUCT_NAME=%{name} \
#    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
#    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
#    -DCMAKE_INSTALL_BINDIR=%{_bindir} \
#    -DCMAKE_INSTALL_MANDIR=%{_mandir} \
#    -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir} \
%cmake \
    -DBUILDNUM=%version \
    -DRELEASE=ON \
    -DPYTHON_EXECUTABLE=%__python3 \
    -DCMAKE_INSTALL_DATAROOTDIR=%_datadir \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_logdir/ipmctl
rm -f %buildroot%_defaultdocdir/ipmctl/*

%files
%doc README.md
%_bindir/ipmctl
%_man1dir/ipmctl*

%files -n libipmctl
%doc output/release/ipmctl_default.conf
%_libdir/libipmctl.so.*
%config(noreplace) %_datadir/ipmctl/ipmctl.conf
%dir %_logdir/ipmctl
%config(noreplace) %_logrotatedir/ipmctl

%files -n libipmctl-devel
%_libdir/libipmctl.so
%_includedir/*.h
%_pkgconfigdir/libipmctl.pc

%changelog
* Fri Feb 11 2022 Andrey Cherepanov <cas@altlinux.org> 02.00.00.3885-alt1
- Initial build for Sisyphus.
