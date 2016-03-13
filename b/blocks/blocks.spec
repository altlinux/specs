Summary: Conversion tools to enable bcache or LVM on existing block devices
Name: blocks
Version: 0.1.4
Release: alt2.1
License: GPLv3
Group: System/Kernel and hardware
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.org>
Url: https://github.com/g2p/blocks

BuildRequires: rpm-build-python3 python3-module-setuptools

Requires: python3-module-augeas >= 0.4.1
Requires: python3-module-parted >= 3.10

Requires: bcache-tools
Requires: btrfs-progs
Requires: cryptsetup
Requires: dmsetup
Requires: e2fsprogs
Requires: losetup
Requires: lvm2
Requires: nilfs-utils
Requires: reiserfsprogs
Requires: udev
Requires: util-linux
Requires: xfsprogs

BuildArch: noarch

%description
Conversion tools for block devices.

Convert between raw partitions, logical volumes, and bcache devices
without moving data. blocks shuffles blocks and sprouts superblocks.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

install -d %buildroot%_sbindir
mv %buildroot{%_bindir,%_sbindir}/%name

%files
%_sbindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-py*.egg-info
%doc README.md

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Oct 11 2014 Terechkov Evgenii <evg@altlinux.org> 0.1.4-alt2
- Drop maintboot requires


* Sat Oct 11 2014 Terechkov Evgenii <evg@altlinux.org> 0.1.4-alt1
- Initial build for ALT Linux Sisyphus
