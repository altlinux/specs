%define modname pytest-tap

Name: python-module-%modname
Version: 2.2
Release: alt1

Summary: Test Anything Protocol (TAP) reporting plugin for pytest
Group: Development/Python
License: BSD
Url: http://pypi.python.org/pypi/%modname

# VCS: https://github.com/python-tap/pytest-tap
Source: http://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools python-module-babel

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute python3-module-babel

%description
%modname is a reporting plugin for pytest that outputs Test Anything
Protocol (TAP) data. TAP is a line based test protocol for recording test
data in a standard way.

%package -n python3-module-%modname
Summary: Test Anything Protocol (TAP) reporting plugin for pytest
Group: Development/Python3

%description -n python3-module-%modname
%modname is a reporting plugin for pytest that outputs Test Anything
Protocol (TAP) data. TAP is a line based test protocol for recording test
data in a standard way.

%prep
%setup -n %modname-%version -a0
cp -a %modname-%version py3build

%build
%python_build

pushd py3build
%python3_build
popd

%install
pushd py3build
%python3_install
popd

%python_install


%files
%python_sitelibdir_noarch/pytest_tap/
%python_sitelibdir_noarch/*.egg-info
%doc README* docs/releases.rst

%files -n python3-module-%modname
%python3_sitelibdir_noarch/pytest_tap/
%python3_sitelibdir_noarch/*.egg-info
%doc README* LICENSE

%changelog
* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus



