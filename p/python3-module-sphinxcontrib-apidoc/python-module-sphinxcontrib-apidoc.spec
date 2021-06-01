%define  oname sphinxcontrib-apidoc

Name:    python3-module-%oname
Version: 0.3.0
Release: alt2

Summary: A Sphinx extension for running sphinx-apidoc on each build

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-apidoc
# https://github.com/sphinx-contrib/apidoc

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

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
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/sphinxcontrib/apidoc/*
%python3_sitelibdir/*.egg-info

%changelog
* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt2
- Drop python2 support.

* Fri Nov 09 2018 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
