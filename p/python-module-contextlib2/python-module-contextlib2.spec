%define modulename contextlib2

Name: python-module-contextlib2
Version: 0.4.0
Release: alt1

Summary: Backports and enhancements for the contextlib module

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/c/%modulename/%modulename-%version.tar

%setup_python_module %modulename

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 08 2013
# optimized out: python-base python-devel python-module-distribute python-module-peak python-module-zope python-modules python-modules-compiler python-modules-email
BuildRequires: python-module-mwlib python-module-paste

%description
contextlib2 is a backport of the standard library's contextlib
module to earlier Python versions.

It also serves as a real world proving ground for possible
future enhancements to the standard library version.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename.*
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus
