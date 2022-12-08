%def_with check

Name:    vcmmd
Version: 8.0.71
Release: alt1

Summary: Virtuozzo containers memory management daemon
License: GPL-2.0-or-later
Group:   System/Configuration/Other

URL:     https://src.openvz.org/
Vcs:     https://src.openvz.org/scm/ovz/vcmmd.git

Source:  %name-%version.tar
Patch:   %name-%version.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: lib%name
BuildRequires: systemd
BuildRequires: gcc-c++

%if_with check
BuildRequires: /proc
BuildRequires: python3-module-mock python3-module-pytest python3-module-psutil
%endif

%description
Virtuozzo containers memory management daemon

%prep
%setup -n %name-%version
%patch -p1

%build
%__python3 setup.py build --executable="/usr/bin/python3"

%install
# Local setup.py fails to parse "--root=path" option, only "--root path" variant:
%__python3 setup.py install --skip-build --root %buildroot --install-scripts %_sbindir
mv %buildroot/usr/lib %buildroot/usr/lib64
mkdir %buildroot%_sysconfdir/vz/vcmmd.d/

%if_with check
%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd tests
%__python3 test_util_misc.py
popd
%endif

%files
%doc COPYING
%_sbindir/*
%python3_sitelibdir/*
%_unitdir/%name.service
%_sysconfdir/vz/vcmmd.d/
%config(noreplace) %_sysconfdir/dbus-1/system.d/com.virtuozzo.vcmmd.conf
%config(noreplace) %_sysconfdir/vz/*.conf
%config(noreplace) %_sysconfdir/logrotate.d/*
%config %_tmpfilesdir/vcmmd-tmpfiles.conf

%changelog
* Thu Dec 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 8.0.71-alt1
- 8.0.71
- change license

* Wed Oct 26 2022 Andrew A. Vasilyev <andy@altlinux.org> 8.0.68-alt1
- 8.0.68

* Fri Mar 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 8.0.5-alt1
- 8.0.5

* Wed Mar 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 8.0.3-alt1
- 8.0.3

* Mon Sep 28 2020 Andrew A. Vasilyev <andy@altlinux.org> 8.0.1-alt4
- merge dist-vz7-u15 branch

* Mon Aug 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 8.0.1-alt3
- reduce difference with upstream branch dist-vz7-u15
- add %%check in spec file

* Sat May 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 8.0.1-alt2
- update copyright information (cherry-pick 34deb3f7)

* Wed Feb 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 8.0.1-alt1
- merge from 8.0.1

* Mon Nov 11 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt4
- cleanup spec

* Mon Nov 11 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt3
- change /var/run to /run

* Thu Oct 31 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt2
- convert to python3

* Mon Sep 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt1
- initial import for ALT
