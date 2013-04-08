%define modulename pycparser

Name: python-module-pycparser
Version: 2.09.1
Release: alt1

Summary: C parser in Python

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/p/%modulename/%modulename-%version.tar

%setup_python_module %modulename

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 08 2013
# optimized out: python-base python-devel python-module-distribute python-module-peak python-module-zope python-modules python-modules-compiler python-modules-email
BuildRequires: python-module-mwlib python-module-paste

%description
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library.
It parses C code into an AST and can serve as a front-end for C compilers or analysis tools.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 2.09.1-alt1
- initial build for ALT Linux Sisyphus
