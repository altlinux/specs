%define modname orderedset
%def_enable check

Name: python3-module-%modname
Version: 2.0.3
Release: alt1

Summary: An Ordered Set implementation in Cython
Group: Development/Python3
License: BSD-3-Clause and MIT
Url: https://pypi.org/project/%modname

#VCS: https://github.com/simonpercivall/orderedset
Source: https://pypi.io/packages/source/o/%modname/%modname-%version.tar.gz


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython python3-module-setuptools python3-module-unittest2

%description
An Ordered Set implementation in Cython. Based on Raymond Hettinger's
OrderedSet recipe.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 setup.py test

%files
%python3_sitelibdir/*
%doc README* HISTORY*

%changelog
* Tue Jul 28 2020 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- first build for Sisyphus



