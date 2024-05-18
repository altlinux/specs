%define  oname sphinxcontrib-apidoc

%def_with check

Name:    python3-module-%oname
Version: 0.5.0
Release: alt1

Summary: A Sphinx extension for running sphinx-apidoc on each build

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-apidoc
VCS:     https://github.com/sphinx-contrib/apidoc

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-tests
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
sphinx-apidoc is a tool for automatic generation of Sphinx sources that,
using the autodoc extension, documents a whole package in the style of
other automatic API documentation tools. sphinx-apidoc does not actually build
documentation - rather it simply generates it.
As a result, it must be run before sphinx-build.

%prep
%setup

%build
export PBR_VERSION="%version"
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/sphinxcontrib/apidoc/*
%python3_sitelibdir/sphinxcontrib_apidoc-%version.dist-info

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Build new version.

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt2
- Drop python2 support.

* Fri Nov 09 2018 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
