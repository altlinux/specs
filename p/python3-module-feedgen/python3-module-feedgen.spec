%define pypi_name feedgen
# network required
%def_disable check

Name: python3-module-feedgen
Version: 1.0.0
Release: alt1

Summary: Feed Generator (ATOM, RSS, Podcasts)
Group: Development/Python3
License: LGPL-3.0-or-later or BSD-2-Clause
Url: https://pypi.org/project/feedgen/

Vcs: https://lkiesow.github.io/python-feedgen.git

Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 python3(wheel) python3(setuptools)

%description
This module can be used to generate web feeds in both ATOM and RSS
format. It has support for extensions. Included is for example an
extension to produce Podcasts.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 -m unittest

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc docs/html/*

%changelog
* Tue Dec 26 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Mar 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus

