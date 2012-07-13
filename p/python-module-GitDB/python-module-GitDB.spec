Name: python-module-GitDB
Version: 0.5.4
Release: alt1

Summary: IO of git-style object databases

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/GitPython/

Source: %name-%version.tar

%setup_python_module gitdb

# Automatically added by buildreq on Fri Oct 08 2010
BuildRequires: python-devel

BuildRequires: python-module-setuptools

%description
IO of git-style object databases.

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
* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALTLinux Sisyphus

