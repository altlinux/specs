%def_enable snapshot
%define pypi_name typogrify

%def_enable check

Name: python3-module-%pypi_name
Version: 2.0.7
Release: alt3

Summary: Filters to enhance web typography
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%pypi_name

%if_disabled snapshot
Source: https://pypi.io/packages/source/t/%pypi_name/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/mintchaos/typogrify
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

Requires: python3-module-smartypants >= 1.8.3

# Installing Jinja or Django is only required if you
# intend to use the optional template filters that are
# included for those frameworks.
%filter_from_requires /^python3(django/d
%filter_from_requires /^python3(jinja/d

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(poetry-core)
%{?_enable_check:BuildRequires: python3(pytest) python3(smartypants)}

%description
Typogrify provides a set of custom filters that automatically apply
various transformations to plain text in order to yield
typographically-improved HTML. While often used in conjunction with Jinja
and Django template systems, the filters can be used in any environment.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
py.test-3 --doctest-modules typogrify/filters.py typogrify/packages/titlecase/tests.py

%files
%python3_sitelibdir_noarch/%pypi_name
#%%exclude %python3_sitelibdir_noarch/%pypi_name/packages/titlecase/tests.py
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Wed Aug 30 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt3
- updated to 2.0.7-27-g053a8b8
- ported to %%pyproject macros
- enabled %%check
- excluded tests from %%files (ALT #47400)

* Fri Oct 01 2021 Ivan A. Melnikov <iv@altlinux.org> 2.0.7-alt2
- get rid of django and jinja dependencies (closes: #41042)

* Fri Mar 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- first build for Sisyphus




