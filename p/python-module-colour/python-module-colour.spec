%define modname colour

Name: python-module-%modname
Version: 0.1.5
Release: alt1

Summary: Python module to convert and manipulate various color representations
Group: Development/Python
License: BSD
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools python-module-d2to1

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute python3-module-d2to1

%description
This Python module defines several color formats that can be converted to
one or another.

%package -n python3-module-%modname
Summary: Python3 module to convert and manipulate various color representations
Group: Development/Python3

%description -n python3-module-%modname
This Python3 module defines several color formats that can be converted
to one or another.

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

%files
%python_sitelibdir_noarch/%modname.py*
%doc README.rst
%python_sitelibdir_noarch/*.egg-info

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname.py
%python3_sitelibdir_noarch/__pycache__/%{modname}*
%doc README.rst LICENSE CHANGELOG.rst
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- first build for Sisyphus


