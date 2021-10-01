%define modname typogrify

Name: python3-module-%modname
Version: 2.0.7
Release: alt2

Summary: Filters to enhance web typography
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%modname

Vcs: https://github.com/mintchaos/typogrify
Source: https://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: python3-module-smartypants >= 1.8.3

# Installing Jinja or Django is only required if you
# intend to use the optional template filters that are
# included for those frameworks.
%filter_from_requires /^python3(django/d
%filter_from_requires /^python3(jinja/d

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
* Fri Oct 01 2021 Ivan A. Melnikov <iv@altlinux.org> 2.0.7-alt2
- get rid of django and jinja dependencies (closes: #41042)

* Fri Mar 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- first build for Sisyphus




