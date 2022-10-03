%define pypi_name yapsy
%define modname Yapsy
%def_enable check

Name: python3-module-%pypi_name
Version: 1.12.2
Release: alt1

Summary: A small Python plugin system library
Group: Development/Python3
License: BSD-2-Clause and CC-BY-SA-3.0 and ISC
Url: http://yapsy.sourceforge.net/

Source: https://pypi.io/packages/source/Y/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Yapsy is a small library implementing the core mechanisms needed to build
a plugin system into a wider application.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 runtests.py

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%modname-%version-*.egg-info
%doc README* CHANGELOG* LICENSE*

%changelog
* Mon Oct 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- first build for Sisyphus




