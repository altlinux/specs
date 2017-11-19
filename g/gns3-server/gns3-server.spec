%add_verify_elf_skiplist %python3_sitelibdir/gns3server/compute/docker/resources/bin/busybox
%add_findreq_skiplist %python3_sitelibdir/gns3server/compute/docker/*
%def_with requirements

Name: gns3-server
Version: 2.1.0
Release: alt1

Summary: GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM
License: GPLv3
Group: File tools
Url: https://github.com/GNS3/gns3-server

Buildarch: noarch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires(pre): rpm-build-python3 rpm-build-gir
Requires: cpulimit
Requires: dynamips >= 0.2.11
%if_with requirements
Requires: python3-module-yarl >= 0.11
Requires: python3-module-yarl < 0.12
Requires: python3-module-aiohttp-cors >= 0.5.3
Requires: python3-module-aiohttp-cors < 0.6.0
Requires: python3-module-jinja2 >= 2.7.3 
Requires: python3-module-aiohttp >= 2.2.0
Requires: python3-module-aiohttp <= 2.3.0
Requires: python3-module-jsonschema >= 2.4.0
Requires: python3-module-raven >= 5.23.0
Requires: python3-module-psutil >= 3.0.0
Requires: python3-module-zipstream >= 1.1.4
Requires: python3-module-multidict < 3.2.0
Requires: python3-module-typing > 3.5.3
%endif
Requires: qemu
Requires: wireshark
Requires: iouyap
Requires: ubridge
Requires: vpcs
Conflicts: gns3 < 1.0.0

%description
The GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM.
Clients like the GNS3 GUI controls the server using a HTTP REST API.

%prep
%setup
%if_without requirements
echo '' > requirements.txt
%endif

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS LICENSE README.rst
%_bindir/*
%python3_sitelibdir/gns3server
%python3_sitelibdir/gns3_server-*.egg-info
%exclude %python3_sitelibdir/tests/controller

%changelog
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
