%define modname anytree
%def_disable python2
%def_disable check

Name: python-module-%modname
Version: 2.7.3
Release: alt1

Summary: Python Tree Data Structure Library
Group: Development/Python
License: Apache-2.0
Url: https://pypi.python.org/pypi/%modname
# https://github.com/c0fec0de/anytree

Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

%if_enabled python2
BuildRequires: python-devel
BuildRequires: python-module-setuptools
%endif

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
%setup -n %modname-%version %{?_enable_python2:-a0
cp -a %modname-%version py2build}

%build
%python3_build

%if_enabled python2
pushd py2build
%python_build
popd
%endif

%install
%python3_install

%if_enabled python2
pushd py2build
%python_install
popd
%endif

%check
%__python3 setup.py test

%if_enabled python2
pushd py2build
%__python setup.py test
popd
%endif

%if_enabled python2
%files
%python_sitelibdir_noarch/%modname/
%python_sitelibdir_noarch/*.egg-info
%doc README.rst
%endif

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.rst

%changelog
* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- 2.7.3
- disabled python2 build

* Mon Feb 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Sat Feb 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sat Mar 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- first build for Sisyphus



