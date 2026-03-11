Name:    magic-wormhole
Version: 0.18.0
Release: alt1

Summary: get things from one computer to another, safely

License: MIT
Group:   Development/Python3
URL:     https://github.com/warner/magic-wormhole

# Source-url: https://github.com/warner/magic-wormhole/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires(pre): rpm-build-intro >= 2.1.1

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-versioneer

BuildArch: noarch

# do not provide internal modules
AutoProv:yes,nopython3

%py3_use spake2 >= 0.8
%py3_use pynacl
%py3_use attrs >= 19.2.0
# twisted
# autobahn
%py3_use automat
%py3_use cryptography
%py3_use tqdm >= 4.13.0
%py3_use click
%py3_use humanize
%py3_use txtorcon >= 18.0.2
%py3_use zipstream-ng
%add_python3_req_skip iterableio


%description
Get things from one computer to another, safely.

This package provides a library and a command-line tool named wormhole,
which makes it possible to get arbitrary-sized files and directories
(or short pieces of text) from one computer to another.
The two endpoints are identified by using identical "wormhole codes":
in general, the sending machine generates and displays the code,
which must then be typed into the receiving machine.

The codes are short and human-pronounceable,
using a phonetically-distinct wordlist.
The receiving side offers tab-completion on the codewords,
so usually only a few characters must be typed.
Wormhole codes are single-use and do not need to be memorized.

%prep
%setup


%build
%pyproject_build

%install
%pyproject_install
rm -rv %buildroot%python3_sitelibdir/wormhole/test/
# TODO
rm -v %buildroot/usr/wormhole_complete.*

%files
%_bindir/wormhole
#_bindir/wormhole-server
%python3_sitelibdir/wormhole/
%python3_sitelibdir/*.*-info

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.18.0-alt1
- new version 0.18.0
- drop zipstream-ng version requirement (1.5.0 available in repo)
- skip iterable_io dependency (not yet packaged)

* Sat Apr 06 2024 Vitaly Lipatov <lav@altlinux.ru> 0.14.0-alt1
- new version 0.14.0 (with rpmrb script)

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt2
- Fixed FTBFS.

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 0.11.2-alt1
- new version 0.11.2 (with rpmrb script)
- update requirements

* Tue Jul 03 2018 Vitaly Lipatov <lav@altlinux.ru> 0.10.5-alt1
- new version 0.10.5 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.3-alt1
- Initial build for ALT Sisyphus
