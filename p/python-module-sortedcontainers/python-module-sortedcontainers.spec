%define modname sortedcontainers

Name: python-module-%modname
Version: 1.5.9
Release: alt1

Summary: Python SortedContainers module
Group: Development/Python
License: Apache-2.0
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
`SortedContainers`_ is an Apache2 licensed `sorted collections library`_,
written in pure-Python, and fast as C-extensions.

%package -n python3-module-%modname
Summary: Python3 SortedContainers module
Group: Development/Python3

%description -n python3-module-%modname
`SortedContainers`_ is an Apache2 licensed `sorted collections library`_,
written in pure-Python, and fast as C-extensions.

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
%python_sitelibdir_noarch/%modname/
%python_sitelibdir_noarch/*.egg-info
%doc README.rst


%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.rst LICENSE


%changelog
* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.9-alt1
- 1.5.9

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- first build for Sisyphus


