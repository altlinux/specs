%define oname zake

%def_without check

Name: python3-module-%oname
Version: 0.2.2
Release: alt2
Summary: Testing utilities for the kazoo library
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/yahoo/Zake

# https://github.com/python-zk/kazoo.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-kazoo >= 1.3.1
BuildRequires: python3-module-six
BuildRequires: python3-module-nose
BuildRequires: python3-module-testtools
BuildRequires: python3-module-flake8
%endif

%description
A python package that works to provide a nice set of testing utilities for the
kazoo library.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test
nosetests3

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/%oname/__pycache__/test.*

%changelog
* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 0.2.2-alt2
- Stopped Python2 package build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- Initial build for Sisyphus
