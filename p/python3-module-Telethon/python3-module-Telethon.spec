%define  modulename Telethon

Name:    python3-module-%modulename
Version: 0.15.5
Release: alt1

Summary: Pure Python 3 Telegram client library

License: MIT
Group:   Development/Python3
URL:     https://github.com/LonamiWebs/Telethon

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

# Source-url: https://github.com/LonamiWebs/Telethon/archive/v%version.tar.gz
Source:  %modulename-%version.tar

%description
Telethon is Telegram client implementation in Python 3
which uses the latest available API of Telegram.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/telethon/
%python3_sitelibdir/telethon_generator/
%python3_sitelibdir/*.egg-info/

%changelog
* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.15.5-alt1
- Initial build for Sisyphus
