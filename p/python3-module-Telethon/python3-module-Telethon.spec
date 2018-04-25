%define  modulename Telethon

Name:    python3-module-%modulename
Version: 0.18.3
Release: alt1

Summary: Pure Python 3 Telegram client library

License: MIT
Group:   Development/Python3
URL:     https://github.com/LonamiWebs/Telethon

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/LonamiWebs/Telethon/archive/v%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
Telethon is Telegram client implementation in Python 3
which uses the latest available API of Telegram.

%prep
%setup -n %modulename-%version

%build
python3 setup.py gen tl errors
%python3_build

%install
%python3_install

# generated
test -r %buildroot%python3_sitelibdir/telethon/tl/all_tlobjects.py
test -r %buildroot%python3_sitelibdir/telethon/errors/rpc_error_list.py

%files
%python3_sitelibdir/telethon/
%python3_sitelibdir/telethon_generator/
%python3_sitelibdir/*.egg-info/

%changelog
* Wed Apr 25 2018 Vitaly Lipatov <lav@altlinux.ru> 0.18.3-alt1
- new version 0.18.3 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.15.5-alt2
- enable generate files

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.15.5-alt1
- Initial build for Sisyphus
