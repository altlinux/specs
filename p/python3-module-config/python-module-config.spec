%define _unpackaged_files_terminate_build 1
BuildRequires: python3-tools
BuildRequires(pre): rpm-build-python3
%define oldname python-module-config
%define packagename python-module-config

Summary: a module for configuring Python programs which aims to offer more power and flexibility than the existing ConfigParser module.
Name: python3-module-config
Version: 0.3.9
Release: alt1
Source0: config-%version.tar.gz
License: GPL
Group: Development/Python
URL: http://www.red-dove.com/python_config.html
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
A module for configuring Python programs which aims to offer more power and flexibility than the existing ConfigParser module. 
Python programs which are designed as a hierarchy of components can use config to configure their various components in a uniform way.

%prep
%setup  -q -n config-%version

%build
2to3-3.3 -w .
2to3-3.3 -w -d .
%python3_build

%install
%python3_install

%files
%doc README.txt LICENSE
%python3_sitelibdir/config.*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/config-*.egg-info

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1
- Initial build for Sisyphus

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.7-alt2.1.1
- python3 copycat import

