%define packagename python-module-config

Summary: a module for configuring Python programs which aims to offer more power and flexibility than the existing ConfigParser module.
Name: %packagename
Version: 0.3.7
Release: alt2.1.1
Source0: config-%version.tar.gz
License: GPL
Group: Development/Python
URL: http://www.red-dove.com/python_config.html
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
A module for configuring Python programs which aims to offer more power and flexibility than the existing ConfigParser module. 
Python programs which are designed as a hierarchy of components can use config to configure their various components in a uniform way.

%prep
%setup  -q -n config-%version

%build
%python_build

%install
%python_install

%files
%doc README.txt LICENSE
%python_sitelibdir/config.*
%python_sitelibdir/config-*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.7-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt2.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.3.7-alt2
- Fixing packaging errors.

* Thu Jul 10 2008 Mikhail Pokidko <pma@altlinux.org> 0.3.7-alt1
- Initial ALT build


