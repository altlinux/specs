Name: gns3-net-converter
Version: 1.3.0
Release: alt1.1

Summary: GNS3 Topology Converter
License: GPLv3
Group: File tools
Url: https://pypi.python.org/pypi/gns3-net-converter
#Url: https://github.com/GNS3/gns3-converter

Buildarch: noarch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: python3-devel python3-module-setuptools
BuildRequires(pre): rpm-build-python3

%description
GNS3 Converter is designed to convert old ini-style GNS3 topologies (<=0.8.7)
to the newer version v1+ JSON format for use in GNS3 v1+

The converter will convert all IOS, Cloud and VirtualBox devices to the new
format. It will also convert all QEMU based devices (QEMU VM, ASA, PIX, JUNOS &
IDS). VPCS nodes will be converted to cloud devices due to lack of information
the 0.8.7 topology files.

For topologies containing snapshots, the snapshots will also be converted to the
new format automatically.

%prep
%setup
sed "s/name='gns3-converter'/name='gns3-net-converter'/" setup.py -i

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/gns3converter
%python3_sitelibdir/gns3_net_converter-*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 04 2016 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux Sisyphus.
