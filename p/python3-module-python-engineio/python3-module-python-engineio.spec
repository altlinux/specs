%define _unpackaged_files_terminate_build 1
%define pypi_name python-engineio
%define mod_name engineio
%define distinfo_name python_engineio

%def_with check

Name:    python3-module-%pypi_name
Version: 4.13.2
Release: alt1

Summary: Python Engine.IO server and client
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/python-engineio
VCS:     https://github.com/miguelgrinberg/python-engineio

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-furo
BuildRequires: python3-module-accessible-pygments

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-simple-websocket
BuildRequires: python3-module-websocket-client
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pytest-asyncio
%endif

%add_findreq_skiplist *gevent_uwsgi.py

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Python implementation of the Engine.IO realtime client and server.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Python implementation of the Engine.IO realtime client and server.

This package contains documentation for %pypi_name.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build
%make -C docs html SPHINXBUILD=sphinx-build-3

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %distinfo_name}

%files docs
%doc docs/_build/html/*
%doc examples

%changelog
* Sun Jun 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.13.2-alt1
- 4.8.0 -> 4.13.2

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.8.0-alt1.1
- Demodernized packaging.

* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 4.8.0-alt1
- Initial build for Sisyphus
