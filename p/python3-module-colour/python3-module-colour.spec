%define modname colour
%def_enable check

Name: python3-module-%modname
Version: 0.1.5
Release: alt3

Summary: Python module to convert and manipulate various color representations
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%modname

Vcs: https://github.com/vaab/colour
Source: https://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz
Patch: %name-0.1.5-alt-setup.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-nose python3-module-nosexcover}

%description
This Python module defines several color formats that can be converted to
one or another.

%prep
%setup -n %modname-%version
%patch -b .orig
rm -r %modname.egg-info

%build
%python3_build

%install
%python3_install

%check
nosetests-3

%files
%python3_sitelibdir_noarch/%modname.py
%python3_sitelibdir_noarch/__pycache__/%{modname}*
%doc README.rst LICENSE CHANGELOG.rst
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Tue Jan 25 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt3
- ported from deprecated d2to1 to setuptools
- enabled %%check

* Sat Jul 24 2021 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt2
- python3-only build

* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- first build for Sisyphus


