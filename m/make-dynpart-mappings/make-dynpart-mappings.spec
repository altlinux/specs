%define _unpackaged_files_terminate_build 1

Name: make-dynpart-mappings
Version: 10.2.4
Release: alt1
Summary: Android dynamic partition mapping tool
License: GPL-v3
Group: System/Kernel and hardware
Url: https://gitlab.com/flamingradian/make-dynpart-mappings
VCS: https://gitlab.com/flamingradian/make-dynpart-mappings.git

Source0: %name-%version.tar
Source1: %name@.service

BuildRequires(pre): rpm-macros-systemd
BuildRequires: gcc
BuildRequires: pkg-config
BuildRequires: libdevmapper-devel
BuildRequires: libmd-devel
BuildRequires: libblkid-devel

%description
A short program that sets up Android dynamic partitions for use on Linux.
It reads the logical partition metadata from a Android "super" partition and
creates corresponding device-mapper mappings for each logical partition
within it.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_unitdir
install -Dm 0755 make-dynpart-mappings %buildroot%_sbindir/make-dynpart-mappings
install -Dm 0644 %SOURCE1 %buildroot%_unitdir

%files
%_sbindir/make-dynpart-mappings
%_unitdir/make-dynpart-mappings@.service

%changelog
* Tue Jul 07 2026 Vasiliy Doylov <neko@altlinux.org> 10.2.4-alt1
- Initial build for ALT
