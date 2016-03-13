Name: pylog2rotate
Version: 1.1.0
Release: alt1.1

Summary: Rotate backups using exponentially-growing periods

Group: File tools
License: GPL
Url: https://github.com/avian2/pylog2rotate

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/avian2/pylog2rotate.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%description
This is a rewrite of the log2rotate tool by Chris Forno.
It provides the same command line interface as the original.

See http://jekor.com/log2rotate

%prep
%setup

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%python3_sitelibdir/__pycache__

%files
%_bindir/log2rotate
%python3_sitelibdir/log2rotate.py
%python3_sitelibdir/%name-%version-*.egg-info

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus
