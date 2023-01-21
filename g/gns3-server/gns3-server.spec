# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_disable check

%add_verify_elf_skiplist %python3_sitelibdir/gns3server/compute/docker/resources/bin/busybox
%add_findreq_skiplist %python3_sitelibdir/gns3server/compute/docker/*
%add_python3_req_skip prompt_toolkit.eventloop.base
%add_python3_req_skip prompt_toolkit.interface
%add_python3_req_skip prompt_toolkit.key_binding.input_processor
%add_python3_req_skip prompt_toolkit.terminal.vt100_output

Name: gns3-server
Version: 2.2.35.1
Release: alt1

Summary: GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM
License: GPLv3
Group: File tools
Url: https://github.com/GNS3/gns3-server

Buildarch: noarch

Source: %name-%version.tar

# test_lock_decorator is failed at ALT girar
Patch: drop-test_lock_decorator.patch

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-importlib-resources
BuildRequires(pre): rpm-build-python3 rpm-build-gir
Requires: cpulimit
Requires: dynamips >= 0.2.11
Requires: python3-module-aiofiles >= 22.1.0
Requires: python3-module-aiohttp >= 3.8.3
Requires: python3-module-aiohttp-cors >= 0.7.0
Requires: python3-module-async-timeout >= 3.0.1
Requires: python3-module-jinja2 >= 3.1.2
Requires: python3-module-jsonschema >= 3.2.0
Requires: python3-module-psutil >= 5.9.2
#Requires: python3-module-sentry-sdk >= 1.5.12
Requires: iouyap
Requires: ubridge
Requires: vpcs
Conflicts: gns3 < 1.0.0

%if_disabled check
%else
BuildRequires: /proc
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-aiohttp
BuildRequires: python3-module-aiohttp >= 3.8.3
BuildRequires: python3-module-aiohttp-tests
BuildRequires: python3-module-jsonschema >= 3.2.0
BuildRequires: python3-module-aiofiles >= 22.1.0
BuildRequires: python3-module-psutil >= 5.9.2
BuildRequires: python3-module-jinja2 >= 3.1.2
BuildRequires: python3-module-distro
BuildRequires: python3-module-aiohttp-cors >= 0.7.0
#BuildRequires: python3-module-cpuinfo
%endif

%description
The GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM.
Clients like the GNS3 GUI controls the server using a HTTP REST API.

%prep
%setup
%patch -p1
echo '' > requirements.txt

%build
%pyproject_build

%install
%pyproject_install

%ifnarch %ix86 x86_64
rm tests/controller/gns3vm/test_virtualbox_gns3_vm.py
%endif

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%files
%doc AUTHORS README.rst
%_bindir/*
%python3_sitelibdir/gns3server
%python3_sitelibdir/gns3_server-%version.dist-info/

%changelog
* Thu Dec 22 2022 Anton Midyukov <antohami@altlinux.org> 2.2.35.1-alt1
- new version 2.2.35.1
- switch to use pyproject.toml
- disable check

* Thu Jun 23 2022 Anton Midyukov <antohami@altlinux.org> 2.2.33.1-alt1
- new version 2.2.33.1
- cleanup spec

* Thu Mar 03 2022 Anton Midyukov <antohami@altlinux.org> 2.2.31-alt1
- new version 2.2.31

* Wed Jan 12 2022 Anton Midyukov <antohami@altlinux.org> 2.2.29-alt1
- new version 2.2.29

* Fri Jan 07 2022 Anton Midyukov <antohami@altlinux.org> 2.2.28-alt1
- new version 2.2.28

* Sat Nov 13 2021 Anton Midyukov <antohami@altlinux.org> 2.2.26-alt2
- drop test_lock_decorator

* Tue Nov 09 2021 Anton Midyukov <antohami@altlinux.org> 2.2.26-alt1
- new version 2.2.26
- enable check

* Mon Jul 05 2021 Anton Midyukov <antohami@altlinux.org> 2.2.21-alt1
- new version 2.2.21

* Tue Sep 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.11-alt2
- Updated provides and requires due to prompt_toolkit update.

* Fri Jul 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.11-alt1
- new version 2.2.11

* Thu Jun 04 2020 Anton Midyukov <antohami@altlinux.org> 2.2.9-alt1
- new version 2.2.9

* Sun May 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.8-alt1
- new version 2.2.8

* Sun Apr 12 2020 Anton Midyukov <antohami@altlinux.org> 2.2.7-alt1
- new version 2.2.7

* Tue Jan 14 2020 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt1
- new version 2.2.5

* Fri Nov 08 2019 Anton Midyukov <antohami@altlinux.org> 2.2.2-alt1
- new version 2.2.2

* Thu Oct 03 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt5
- New release 2.2.0

* Tue Sep 03 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt4.rc4
- New release candidate 2.2.0rc4

* Wed Jul 31 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt3.b4
- New beta release 2.2.0b4

* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt2.b2
- New beta release 2.2.0b2

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt1.a4
- New alpha release 2.2.0a4

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 2.1.12-alt1.1
- Update Requires

* Mon Feb 25 2019 Anton Midyukov <antohami@altlinux.org> 2.1.12-alt1
- new version 2.1.12

* Tue Jan 29 2019 Anton Midyukov <antohami@altlinux.org> 2.1.11-alt2
- drop requires python3(typing), not needed for python3 >= 3.5

* Wed Oct 17 2018 Anton Midyukov <antohami@altlinux.org> 2.1.11-alt1
- new version 2.1.11

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 2.1.5-alt1
- new version 2.1.5

* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 2.1.4-alt1
- new version 2.1.4
- disable requires qemu and wireshark

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 24 2018 Anton Midyukov <antohami@altlinux.org> 2.1.3-alt1
- new version 2.1.3

* Sat Nov 18 2017 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Tue May 23 2017 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Mon May 08 2017 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0

* Tue Aug 30 2016 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- New version 1.5.2

* Thu Aug 04 2016 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux Sisyphus.
