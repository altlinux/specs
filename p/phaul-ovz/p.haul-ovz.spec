%define _libexecdir /usr/libexec
%define oname phaul
%def_without check

Name:    %oname-ovz
Version: 0.1.95
Release: alt2

Summary: Process HAULer -- a tool to live-migrate containers and processes
License: LGPL-2.1
Group: System/Configuration/Other
URL: https://src.openvz.org/
Vcs: https://src.openvz.org/scm/ovz/p.haul.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
Requires: crtools-ovz >= 3.15.4.16
Conflicts: %oname

ExclusiveArch: x86_64

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname
%add_python3_req_skip pycriu
%add_python3_req_skip pycriu.rpc_pb2

%description
Process HAULer -- a tool to live-migrate containers and processes.

%prep
%setup -n %name-%version
%patch -p1
find . -name '*.py' -o -name p.haul-wrap | xargs sed -i \
        -e '1s|^#!/usr/bin/env python$|#!/usr/bin/python3|' \
        -e '1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
        %nil

%build
%python3_build

%install
%__python3 setup.py install --skip-build --root %buildroot --install-scripts %_libexecdir/%oname
# Remove egg-info, module is necessary for phaul only:
# rm -rf %buildroot%python3_sitelibdir_noarch/*.egg-info
install -d %buildroot%_sbindir
install -pD -m755 p.haul-ssh p.haul-wrap %buildroot%_sbindir
ln -s %_libexecdir/%oname/p.haul %buildroot%_sbindir/p.haul
ln -s %_libexecdir/%oname/p.haul-service %buildroot%_sbindir/p.haul-service
chmod a+rx %buildroot%python3_sitelibdir_noarch/%oname/shell/{phaul_client,phaul_service}.py
mv %buildroot%_usr/{lib,%_lib}

%if_with check
%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd test
popd
%endif

%files
%doc COPYING README.md
%_libexecdir/%oname
%_sbindir/*
%python3_sitelibdir/*

%changelog
* Sun Dec 11 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.95-alt2
- use pycriu module from crtools-ovz

* Sat Nov 19 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.95-alt1
- 0.1.95

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.1.93.1-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue Jun 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.93.1-alt1
- 0.1.93.1

* Wed May 25 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.93-alt1
- 0.1.93

* Thu May 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.86-alt1
- 0.1.86

* Wed Apr 27 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.85-alt1
- 0.1.85

* Wed Sep 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.1.84-alt1
- 0.1.84

* Mon Mar 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.1.79-alt1
- 0.1.79

* Mon Jan 11 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.1.78-alt1
- 0.1.78
- fix libvzctl scripts path

* Tue Dec 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.1.77-alt1
- 0.1.77

* Mon Nov 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.1.75-alt1
- initial build for ALT

