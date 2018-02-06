
%define oname weakrefmethod

Name: python-module-%oname
Version: 1.0.3
Release: alt1.1
Summary: WeakMethod class for storing bound methods using weak references.
Group: Development/Python
License: PSF
Url: http://github.com/twang817/weakrefmethod
Source: %oname-%version.tar.gz
BuildArch: noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
This project is a backport of the WeakMethod class, and tests, for Python 2.6.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial package.
