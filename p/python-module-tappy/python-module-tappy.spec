%define modname tap.py
%def_enable python2

Name: python-module-tappy
Version: 2.6.2
Release: alt1

Summary: Test Anything Protocol (TAP) tools
Group: Development/Python
License: BSD
Url: http://pypi.python.org/pypi/%modname

# VCS: https://github.com/python-tap/tappy
Source: http://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

%if_enabled python2
BuildRequires: python-devel
BuildRequires: python-module-setuptools python-module-babel
%endif

BuildRequires: python3-devel rpm-build-python3 python3-module-babel
BuildRequires: python3-module-distribute

%description
tappy python module provides a set of tools for working with the Test
Anything Protocol (TAP), a line based test protocol for recording test
data in a standard way.

%package -n python3-module-tappy
Summary: Test Anything Protocol (TAP) tools
Group: Development/Python3

%description -n python3-module-tappy
tappy python3 module provides a set of tools for working with the Test
Anything Protocol (TAP), a line based test protocol for recording test
data in a standard way.

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
%{?_enable_python2:for f in %buildroot%_bindir/*; do mv "$f" "$f"-3; done}

%if_enabled python2
pushd py2build
%python_install
popd
%endif

%if_enabled python2
%files
%_bindir/tap
%_bindir/tappy
%python_sitelibdir_noarch/tap/
%python_sitelibdir_noarch/*.egg-info
%doc README.md
%endif

%files -n python3-module-tappy
%if_enabled python2
%_bindir/tap-3
%_bindir/tappy-3
%else
%_bindir/tap
%_bindir/tappy
%endif
%python3_sitelibdir_noarch/tap
%python3_sitelibdir_noarch/*.egg-info
%doc README.md LICENSE

%changelog
* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2
- made python2 build optional

* Mon Oct 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- 2.4

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus



