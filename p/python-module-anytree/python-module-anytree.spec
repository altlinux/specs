%define modname anytree
%def_disable check

Name: python-module-%modname
Version: 2.4.3
Release: alt1

Summary: Python Tree Data Structure Library
Group: Development/Python
License: Apache-2.0
Url: https://pypi.python.org/pypi/%modname
# https://github.com/c0fec0de/anytree

Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
Python module to manipulate tree data structures

%package -n python3-module-%modname
Summary: Python Tree Data Structure Library
Group: Development/Python3

%description -n python3-module-%modname
Python3 module to manipulate tree data structures

%prep
%setup -n %modname-%version -a0
cp -a %modname-%version py3build

%build
%python_build

pushd py3build
%python3_build
popd

%install
%python_install

pushd py3build
%python3_install
popd

%check
%__python setup.py test

pushd py3build
%__python3 setup.py test
popd

%files
%python_sitelibdir_noarch/%modname/
%python_sitelibdir_noarch/*.egg-info
%doc README.rst

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.rst

%changelog
* Sat Mar 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- first build for Sisyphus



