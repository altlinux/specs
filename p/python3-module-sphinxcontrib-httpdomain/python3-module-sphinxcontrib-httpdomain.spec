%define mname sphinxcontrib
%define pypi_name sphinxcontrib-httpdomain

%def_without check

Name:    python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: Documenting RESTful HTTP APIs
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/sphinx-contrib/httpdomain

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-tox
BuildRequires: python3-module-wheel
BuildRequires: python3-module-uv-build

BuildArch: noarch

Source: %name-%version.tar

%py3_provides %mname.httpdomain
%py3_requires %mname sphinx

%description
This contrib extension, sphinxcontrib.httpdomain, provides Sphinx domains for
describing HTTP APIs and WebSocket connections.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/sphinxcontrib_httpdomain*

%changelog
* Tue Nov 10 2026 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus.
