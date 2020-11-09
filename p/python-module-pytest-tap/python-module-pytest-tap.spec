%define modname pytest-tap
%def_enable python2

Name: python-module-%modname
Version: 3.2
Release: alt1

Summary: Test Anything Protocol (TAP) reporting plugin for pytest
Group: Development/Python
License: BSD-2-Clause
Url: http://pypi.python.org/pypi/%modname

# VCS: https://github.com/python-tap/pytest-tap
Source: http://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3-module-babel

%{?_enable_python2:
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-babel}

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
%setup -n %modname-%version %{?_enable_python2:-a0
cp -a %modname-%version py2build}

%build
%python3_build

%{?_enable_python2:pushd py2build
%python_build
popd}

%install

%python3_install

%{?_enable_python2:pushd py2build
%python_install
popd}

%if_enabled python2
%files
%python_sitelibdir_noarch/pytest_tap/
%python_sitelibdir_noarch/*.egg-info
%doc README* docs/releases.rst
%endif

%files -n python3-module-%modname
%python3_sitelibdir_noarch/pytest_tap/
%python3_sitelibdir_noarch/*.egg-info
%doc README* LICENSE

%changelog
* Mon Nov 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt1
- 3.2

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1
- made python2 module optional
- fixed License tag

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus



