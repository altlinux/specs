
Name: blocks
Version: 0.1.4
Release: alt2.3

Summary: Conversion tools to enable bcache or LVM on existing block devices
License: GPLv3
Group: System/Kernel and hardware
Url: https://github.com/g2p/blocks
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
Requires: python3-module-maintboot

%py3_requires augeas parted


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
* Mon May 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt2.3
- fixed requires

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Oct 11 2014 Terechkov Evgenii <evg@altlinux.org> 0.1.4-alt2
- Drop maintboot requires


* Sat Oct 11 2014 Terechkov Evgenii <evg@altlinux.org> 0.1.4-alt1
- Initial build for ALT Linux Sisyphus
