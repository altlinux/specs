%def_enable snapshot

%define pypi_name yapsy
%define modname Yapsy
%def_enable check

Name: python3-module-%pypi_name
# yapsy/__init__.py:__version__="2.0.0"
Version: 2.0.0
Release: alt0.5

Summary: A small Python plugin system library
Group: Development/Python3
License: BSD-2-Clause and CC-BY-SA-3.0 and ISC
Url: http://yapsy.sourceforge.net/

%if_disabled snapshot
Source: https://pypi.io/packages/source/Y/%modname/%modname-%version.tar.gz
%else
Source: %modname-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(packaging)}

%description
Yapsy is a small library implementing the core mechanisms needed to build
a plugin system into a wider application.

%prep
%setup -n %modname-%version%{?_enable_snapshot:/package}

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 runtests.py

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%modname-%version.dist-info
%doc README* CHANGELOG* LICENSE*

%changelog
* Tue Oct 17 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt0.5
- updated to 1.12.2-17-g6b487b0 (pre 2.0.0)
- ported to %%pyproject macros

* Mon Oct 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- first build for Sisyphus




