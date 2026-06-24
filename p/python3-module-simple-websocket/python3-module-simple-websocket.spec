%define _unpackaged_files_terminate_build 1
%define pypi_name simple-websocket
%define mod_name simple_websocket

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Simple WebSocket server and client for Python.
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/simple-websocket
VCS:     https://github.com/miguelgrinberg/simple-websocket

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-wsproto
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Simple WebSocket server and client for Python.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Simple WebSocket server and client for Python.

This package contains documentation for %pypi_name.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%make -C docs html SPHINXBUILD=sphinx-build-3

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not test_client'

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%files docs
%doc docs/_build/html/*
%doc examples

%changelog
* Thu Jun 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- 1.0.0 -> 1.1.0

* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
