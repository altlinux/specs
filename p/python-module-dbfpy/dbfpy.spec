%define modulename dbfpy

Name: python-module-%modulename
Version: 2.2.5
Release: alt1.1

%setup_python_module %modulename

Summary: Python module for accessing .dbf (xBase) files
License: Public domain
Group: Development/Python
Url: http://dbfpy.sourceforge.net/
Packager: Egor Glukhov <kaman@altlinux.org>
Source: %name-%version.tar
BuildArch: noarch
BuildPreReq: python-module-setuptools
BuildRequires: python-devel

%description
dbfpy can read and write simple DBF-files. The DBF-format
was developed about 30 years ago and was used by a number
of simple database applications (dBase, Foxpro, Clipper, ...).
The basic datatypes numbers, short text, and dates are available.
Many different extensions have been used; dbfpy can read and write
only simple DBF-files.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README CHANGES
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt1.1
- Rebuild with Python-2.7

* Wed Oct 27 2010 Egor Glukhov <kaman@altlinux.org> 2.2.5-alt1
- Initial build for Sisyphus

