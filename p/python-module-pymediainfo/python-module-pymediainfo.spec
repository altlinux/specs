%define modname pymediainfo

Name: python-module-%modname
Version: 2.2.0
Release: alt1

Summary: A Python wrapper for the mediainfo library
Group: Development/Python
License: MIT
Url: https://pypi.python.org/pypi/%modname
Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: libmediainfo

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
This Python module provides a wrapper around the MediaInfo library.

%package -n python3-module-%modname
Summary: A Python3 wrapper for the mediainfo library
Group: Development/Python3
Requires: libmediainfo

%description -n python3-module-%modname
This Python3 module provides a wrapper around the MediaInfo library.

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
%doc README.rst
%python_sitelibdir_noarch/*.egg-info

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%doc README.rst
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Wed Nov 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- first build for Sisyphus


