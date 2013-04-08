%define modulename cffi

Name: python-module-cffi
Version: 0.6
Release: alt1

Summary: Foreign Function Interface for Python calling C code

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/c/%modulename/%modulename-%version.tar

%setup_python_module %modulename

BuildRequires: python-dev libffi-devel python-module-distribute

%description
Foreign Function Interface for Python calling C code.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir//_cffi_backend.so
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
