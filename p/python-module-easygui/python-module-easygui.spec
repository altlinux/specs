%define modname easygui

Name: python-module-%modname
Version: 0.98.1
Release: alt1

Summary: Python3 module for GUI programming
Group: Development/Python
License: 3-clause BSD
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/e/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
EasyGUI is a Python module for very simple, very easy GUI programming in Python.
EasyGUI is different from other GUI libraries in that EasyGUI is NOT
event-driven. Instead, all GUI interactions are invoked by simple
function calls.


%package -n python3-module-%modname
Summary: Python3 module for GUI programming
Group: Development/Python3

%description -n python3-module-%modname
EasyGUI is a Python module for very simple, very easy GUI programming in Python.
EasyGUI is different from other GUI libraries in that EasyGUI is NOT
event-driven. Instead, all GUI interactions are invoked by simple
function calls.

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
%python_sitelibdir_noarch/%modname/*
%doc README.txt
%python_sitelibdir_noarch/*.egg-info

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%doc README.txt
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.98.1-alt1
- first build for Sisyphus


