%define modname colour

Name: python3-module-%modname
Version: 0.1.5
Release: alt2

Summary: Python module to convert and manipulate various color representations
Group: Development/Python3
License: BSD-2-Clause
Url: https://pypi.python.org/pypi/%modname

Vcs: https://github.com/vaab/colour
Source: https://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz
# d2to1
Source1: %name-eggs.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
This Python module defines several color formats that can be converted to
one or another.

%prep
%setup -n %modname-%version -a1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname.py
%python3_sitelibdir_noarch/__pycache__/%{modname}*
%doc README.rst LICENSE CHANGELOG.rst
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Sat Jul 24 2021 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt2
- python3-only build

* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- first build for Sisyphus


