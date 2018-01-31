%define modname tap.py

Name: python-module-tappy
Version: 2.2
Release: alt1

Summary: Test Anything Protocol (TAP) tools
Group: Development/Python
License: BSD
Url: http://pypi.python.org/pypi/%modname

# VCS: https://github.com/python-tap/tappy
Source: http://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools python-module-babel

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
for f in %buildroot%_bindir/*; do mv "$f" "$f"-3; done
popd

%python_install

%files
%_bindir/tap
%_bindir/tappy
%python_sitelibdir_noarch/tap/
%python_sitelibdir_noarch/*.egg-info
%doc README.md

%files -n python3-module-tappy
%_bindir/tap-3
%_bindir/tappy-3
%python3_sitelibdir_noarch/tap
%python3_sitelibdir_noarch/*.egg-info
%doc README.md LICENSE

%changelog
* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus



