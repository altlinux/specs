%define modulename ulib

Name: python3-module-%modulename
Version: 0.21
Release: alt1.1

Summary: ulib: Useful python library

Group: Development/Python
License: GPLv3+
Url: https://pypi.python.org/pypi/ulib

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mdevaev/ulib.git
Source: %name-%version.tar

BuildArch: noarch

#setup_python3_module %modulename

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%description
Useful python3 library.

%prep
%setup
# needs astroid
rm -f ulib/tools/lintfix.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.21-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.21-alt1
- build 0.21

* Fri Dec 13 2013 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- build 0.10, python3 only

* Sat Oct 19 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Linux Sisyphus

* Mon Oct 07 2013 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
