%define modname feedgen
# network required
%def_disable check

Name: python3-module-feedgen
Version: 0.9.0
Release: alt1

Summary: Feed Generator (ATOM, RSS, Podcasts)
Group: Development/Python3
License: LGPL-3.0-or-later or BSD-2-Clause
Url: https://pypi.org/project/feedgen/

Vcs: https://lkiesow.github.io/python-feedgen.git

Source: https://pypi.io/packages/source/f/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 python3-devel

%description
This module can be used to generate web feeds in both ATOM and RSS
format. It has support for extensions. Included is for example an
extension to produce Podcasts.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir_noarch/*
%doc docs/html/*

%changelog
* Thu Mar 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus

