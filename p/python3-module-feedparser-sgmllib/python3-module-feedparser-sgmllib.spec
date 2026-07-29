%def_disable snapshot
%define modname feedparser-sgmllib
%define pypi_name feedparser_sgmllib
%def_disable check

Name: python3-module-%modname
Version: 1.0.0
Release: alt1

Summary: SGML library for feedparser
Group: Development/Python3
License: PSF-2.0
Url: https://github.com/python-syndication/feedparser-sgmllib

Vcs: https://github.com/python-syndication/feedparser-sgmllib.git

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.10 python3(wheel) python3(poetry-core)
%{?_with_doc:BuildRequires: python3-module-sphinx python3-module-requests}
%{?_enable_check:BuildRequires: python3(pytest) python3-module-requests}

%if_disabled snapshot
Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/feedparser/sgmllib/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 29 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

