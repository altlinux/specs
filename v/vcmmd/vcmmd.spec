
Name:    vcmmd
Version: 7.0.165
Release: alt3

Summary: Virtuozzo containers memory management daemon
License: LGPL-2.1
Group:   System/Configuration/Other
# git-vsc: https://src.openvz.org/scm/ovz/vcmmd.git
URL:     https://src.openvz.org/

Packager: Andrew A. Vasilyev <andy@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: libvcmmd
BuildRequires: systemd
BuildRequires: gcc-c++

ExclusiveArch: x86_64

Source:  %name-%version.tar
Patch: %name-%version.patch

%description
Virtuozzo containers memory management daemon

%prep
%setup -n %name-%version
%patch -p1

%build
%python3_build

%install
echo "INSTALL: " %python3_install
%python3_install

%files
%doc COPYING
%_bindir/*
%python3_sitelibdir/*
%_libdir/python*/site-packages/*info
%_libdir/python*/site-packages/%name/
%_unitdir/%name.service
%_sysconfdir/vz/vcmmd.d/
%config(noreplace) %_sysconfdir/dbus-1/system.d/com.virtuozzo.vcmmd.conf
%config(noreplace) %_sysconfdir/vz/*.conf
%config(noreplace) %_sysconfdir/logrotate.d/*

%changelog
* Mon Nov 11 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt3
- change /var/run to /run

* Thu Oct 31 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt2
- convert to python3

* Mon Sep 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt1
  - initial import for ALT
