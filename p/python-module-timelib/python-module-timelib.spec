%define modulename timelib

Name: python-module-%modulename
Version: 0.2.1
Release: alt1.1.1

Summary: Parse english textual date descriptions

Group: Development/Python
License: zlib / PHP
Url: http://pypi.python.org/pypi/%modulename

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/t/%modulename/%modulename-%version.tar

%setup_python_module %modulename

%description
timelib is a short wrapper around php's internal timelib module.
It currently only provides a few functions:
 * timelib.strtodatetime
 * timelib.strtotime

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README.txt
%python_sitelibdir/%modulename.so
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
