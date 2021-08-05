%define modname rawkit
%def_enable check

Name: python3-module-%modname
Version: 0.6.0
Release: alt2

Summary: CTypes based LibRaw bindings
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/r/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: libraw

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-mock}

%description
rawkit (pronounced `rocket`) is a ctypes-based LibRaw_ binding for Python 3
inspired by the Wand_ API.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir_noarch/libraw/
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.rst


%changelog
* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt2
- python3-only build

* Mon Jul 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus


