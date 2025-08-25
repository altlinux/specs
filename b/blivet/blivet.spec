%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Summary: A python module for system storage configuration
Name: blivet
Group: System/Configuration/Other
Url: https://storageapis.wordpress.com/projects/blivet
Version: 3.12.1
Release: alt2
License: GPL-2.0-or-later

Source0: %name-%version.tar
# Contains translations submodule 
Source1: po.tar

BuildArch: noarch

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%global partedver 1.8.1
%global pypartedver 3.10.4
%global utillinuxver 2.15.1
%global libblockdevver 3.3.0
%global libbytesizever 0.3
%global pyudevver 0.18


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-devel pip
BuildRequires: gettext
BuildRequires: systemd

# For tests
BuildRequires: /proc
BuildRequires: python3-module-pyudev >= %pyudevver
BuildRequires: parted >= %partedver
BuildRequires: python3-module-parted >= %pypartedver
BuildRequires: python3-module-selinux
BuildRequires: python3-module-libmount
BuildRequires: python3-module-blockdev
BuildRequires: python3-module-bytesize >= %libbytesizever
BuildRequires: util-linux >= %utillinuxver
BuildRequires: lsof
BuildRequires: libblockdev-plugins
BuildRequires: python3-module-dbus
BuildRequires: python3-module-yaml

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%package -n %name-data
Summary: Data for the %name python module
Group: System/Configuration/Other

%description -n %name-data
The %name-data package provides data files required by the %name
python module.

%package -n python3-module-%name
Summary: A python3 package for examining and modifying storage configuration
Group: Development/Python3

Requires: parted
# Requires: python3-module-selinux
Requires: python3-module-libmount
Requires: python3-module-blockdev >= %libblockdevver
Requires: libblockdev-btrfs >= %libblockdevver
Requires: libblockdev-crypto >= %libblockdevver
Requires: libblockdev-dm >= %libblockdevver
Requires: libblockdev-fs >= %libblockdevver
Requires: libblockdev-loop >= %libblockdevver
Requires: libblockdev-lvm >= %libblockdevver
Requires: libblockdev-mdraid >= %libblockdevver
Requires: libblockdev-mpath >= %libblockdevver
Requires: libblockdev-nvme >= %libblockdevver
Requires: libblockdev-part >= %libblockdevver
Requires: libblockdev-swap >= %libblockdevver

Requires: util-linux
Requires: lsof
Requires: %name-data = %EVR

%description -n python3-module-%name
The python3-%name is a python3 package for examining and modifying storage
configuration.

%prep
%setup -a1

%build
make PYTHON=%__python3

%install
make PYTHON=%__python3 DESTDIR=%buildroot install

%find_lang %name

%check
# Override PATH, so tests will find 'dmsetup' without running from root 
PATH=/usr/sbin:/sbin:$PATH make PYTHON=%__python3 unit-test

%files -n %name-data -f %name.lang
%_sysconfdir/dbus-1/system.d/*
%_datadir/dbus-1/system-services/*
%_libexecdir/*
%_unitdir/*

%files -n python3-module-%name
%doc README.md examples
%python3_sitelibdir/*

%changelog
* Mon Aug 25 2025 Sergey Konev <darisishe@altlinux.org> 3.12.1-alt2
- Proper packaging as gear repo (after switching from srpm)
- Run unit-tests in %check section

* Wed Apr 09 2025 Sergey Konev <darisishe@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Dec 30 2024 Sergey Konev <darisishe@altlinux.org> 3.11.0-alt1
- 3.11.0
- Updated Requires for python module

* Fri Jun 21 2024 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt2
- fix %%_unitdir in %%setup section

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Jun 22 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.4-alt1
- 3.4.4

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- Initial build.

