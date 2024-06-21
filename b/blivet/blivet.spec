%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Summary: A python module for system storage configuration
Name: blivet
Group: System/Configuration/Other
Url: https://storageapis.wordpress.com/projects/blivet
Version: 3.6.0
Release: alt2
License: GPLv2+

Source0: http://github.com/storaged-project/blivet/archive/%name-%version.tar.gz
BuildArch: noarch

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%global partedver 1.8.1
%global pypartedver 3.10.4
%global utillinuxver 2.15.1
%global libblockdevver 2.24
%global libbytesizever 0.3
%global pyudevver 0.18


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-devel
BuildRequires: gettext
BuildRequires: systemd

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
#Recommends: libblockdev-btrfs >= %libblockdevver
#Recommends: libblockdev-crypto >= %libblockdevver
#Recommends: libblockdev-dm >= %libblockdevver
#Recommends: libblockdev-fs >= %libblockdevver
#Recommends: libblockdev-kbd >= %libblockdevver
#Recommends: libblockdev-loop >= %libblockdevver
#Recommends: libblockdev-lvm >= %libblockdevver
#Recommends: libblockdev-mdraid >= %libblockdevver
#Recommends: libblockdev-mpath >= %libblockdevver
#Recommends: libblockdev-nvdimm >= %libblockdevver
#Recommends: libblockdev-part >= %libblockdevver
#Recommends: libblockdev-swap >= %libblockdevver
#Recommends: libblockdev-s390 >= %libblockdevver
Requires: util-linux
Requires: lsof
Requires: %name-data = %EVR

%description -n python3-module-%name
The python3-%name is a python3 package for examining and modifying storage
configuration.

%prep
%setup
sed -e "s:/usr/lib/systemd/system:%_unitdir:g" -i setup.py

%build
make PYTHON=%__python3

%install
make PYTHON=%__python3 DESTDIR=%buildroot install

%find_lang %name

%files -n %name-data -f %name.lang
%_sysconfdir/dbus-1/system.d/*
%_datadir/dbus-1/system-services/*
%_libexecdir/*
%_unitdir/*

%files -n python3-module-%name
%doc README.md examples
%python3_sitelibdir/*

%changelog
* Fri Jun 21 2024 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt2
- fix %%_unitdir in %%setup section

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Jun 22 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.4-alt1
- 3.4.4

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- Initial build.

