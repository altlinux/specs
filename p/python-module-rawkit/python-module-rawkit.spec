%define modname rawkit

Name: python-module-%modname
Version: 0.6.0
Release: alt1

Summary: CTypes based LibRaw bindings
Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/r/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: libraw

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
rawkit (pronounced `rocket`) is a ctypes-based LibRaw_ binding for Python
inspired by the Wand_ API.

%package -n python3-module-%modname
Summary: CTypes based LibRaw bindings
Group: Development/Python3

%description -n python3-module-%modname
rawkit (pronounced `rocket`) is a ctypes-based LibRaw_ binding for Python
inspired by the Wand_ API.

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
%python_sitelibdir_noarch/libraw
%python_sitelibdir_noarch/%modname/
%python_sitelibdir_noarch/*.egg-info
%doc README.rst

%files -n python3-module-%modname
%python3_sitelibdir_noarch/libraw/
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.rst


%changelog
* Mon Jul 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus


