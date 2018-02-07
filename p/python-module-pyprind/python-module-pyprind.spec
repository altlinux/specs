%define modname pyprind
%define Modname PyPrind

Name: python-module-%modname
Version: 2.11.2
Release: alt1

Summary: Python Progress Bar and Percent Indicator Utility
Group: Development/Python
License: 3-clause BSD
Url: http://pypi.python.org/pypi/%Modname
Source: http://pypi.io/packages/source/P/%Modname/%Modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
`SortedContainers`_ is an Apache2 licensed `sorted collections library`_,
written in pure-Python, and fast as C-extensions.

%package -n python3-module-%modname
Summary: Python Progress Bar and Percent Indicator Utility
Group: Development/Python3

%description -n python3-module-%modname
`SortedContainers`_ is an Apache2 licensed `sorted collections library`_,
written in pure-Python, and fast as C-extensions.

%prep
%setup -n %Modname-%version -a0
cp -a %Modname-%version py3build

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
%doc README.md LICENSE


%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.md LICENSE


%changelog
* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.11.2-alt1
- 2.11.2

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.11.1-alt1
- first build for Sisyphus


