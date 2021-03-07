%define modname sphinx-autodoc-typehints
%def_disable check

Name: python3-module-%modname
Version: 1.11.1
Release: alt1

Summary: Type hints (PEP 484) support for the Sphinx autodoc extension
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/agronholm/sphinx-autodoc-typehints.git
Source: https://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-sphobjinv}

%description
This Sphinx extension allows to use Python 3 annotations for
documenting acceptable argument types and return value types of
functions.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*


%changelog
* Sun Mar 07 2021 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- first build for Sisyphus




