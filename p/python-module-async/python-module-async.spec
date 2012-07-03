Name: python-module-async
Version: 0.6.1
Release: alt1.1.1

Summary: Contains the async project data

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/GitPython/

Source: %name-%version.tar

%setup_python_module async

# Automatically added by buildreq on Fri Oct 08 2010
BuildRequires: python-devel zlib-devel

BuildRequires: python-module-setuptools

%description
Contains the async project data.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- initial build for ALTLinux Sisyphus

