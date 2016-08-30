%add_verify_elf_skiplist %python3_sitelibdir/gns3server/modules/docker/resources/bin/busybox
%add_findreq_skiplist %python3_sitelibdir/gns3server/modules/docker/*

Name: gns3-server
Version: 1.5.2
Release: alt1

Summary: GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM
License: GPLv3
Group: File tools
Url: https://github.com/GNS3/gns3-server

Buildarch: noarch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires(pre): rpm-build-python3
Requires: cpulimit
Requires: dynamips >= 0.2.11
Requires: python3-module-jinja2
Requires: python3-module-aiohttp >= 0.21.5
Requires: python3-module-jsonschema >= 2.4.0
Requires: python3-module-raven >= 5.2.0
Requires: python3-module-psutil >= 3.0.0
Requires: python3-module-docker >= 1.4.0
Requires: qemu
Requires: wireshark
Requires: iouyap
Requires: ubridge
Requires: vpcs
Conflicts: gns3

%description
The GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM.
Clients like the GNS3 GUI controls the server using a HTTP REST API.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS LICENSE README.rst
%_bindir/*
%python3_sitelibdir/gns3server
%python3_sitelibdir/gns3_server-*.egg-info

%changelog
* Tue Aug 30 2016 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- New version 1.5.2

* Thu Aug 04 2016 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux Sisyphus.
