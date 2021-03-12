%define modname typogrify

Name: python3-module-%modname
Version: 2.0.7
Release: alt1

Summary: Filters to enhance web typography
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%modname

Vcs: https://github.com/mintchaos/typogrify
Source: https://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: python3-module-smartypants >= 1.8.3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Typogrify provides a set of custom filters that automatically apply
various transformations to plain text in order to yield
typographically-improved HTML. While often used in conjunction with Jinja
and Django template systems, the filters can be used in any environment.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/*
%doc README*

%changelog
* Fri Mar 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- first build for Sisyphus




