Name:    magic-wormhole
Version: 0.10.3
Release: alt1

Summary: get things from one computer to another, safely

License: MIT
Group:   Development/Python3
URL:     https://github.com/warner/magic-wormhole

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-dev

BuildRequires(pre): rpm-build-intro >= 2.1.1

BuildArch: noarch

# do not provide internal modules
AutoProv:yes,nopython3

%py3_use txtorcon >= 0.19.3
%py3_use spake2 >= 0.7
%py3_use attrs >= 16.3.0
%py3_use tqdm >= 4.13.0
%py3_use click >= 6.7
%py3_use humanize
%py3_use ipaddress
%py3_use automat
%py3_use hkdf

%py3_use service-identity
#          "twisted[tls] >= 17.5.0", # 17.5.0 adds failAfterFailures=
#         "autobahn[twisted] >= 0.14.1",


# Source-url: https://github.com/warner/magic-wormhole/archive/%version.tar.gz
Source: %name-%version.tar

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
%python3_build

%install
%python3_install

%files
%_bindir/wormhole
%_bindir/wormhole-server
%python3_sitelibdir/wormhole/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.3-alt1
- Initial build for ALT Sisyphus
