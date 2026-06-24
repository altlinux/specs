%define _unpackaged_files_terminate_build 1
%define pypi_name python-socketio
%define mod_name socketio
%define distinfo_name python_socketio

%def_with check

Name:    python3-module-%pypi_name
Version: 5.16.3
Release: alt1

Summary: Python Socket.IO server and client
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/python-socketio
VCS:     https://github.com/miguelgrinberg/python-socketio

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-furo
BuildRequires: python3-module-accessible-pygments

%if_with check
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-bidict
BuildRequires: python3-module-python-engineio
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-simple-websocket
BuildRequires: python3-module-websocket-client
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-valkey
BuildRequires: python3-module-pytest-asyncio
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Python implementation of the Socket.IO realtime client and server.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Python implementation of the Socket.IO realtime client and server.

This package contains documentation for %pypi_name.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build
%make -C docs html SPHINXBUILD=sphinx-build-3

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %distinfo_name}

%files docs
%doc docs/_build/html/*
%doc examples

%changelog
* Thu Jun 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.16.3-alt1
- 5.11.0 -> 5.16.3

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 5.11.0-alt1.1
- Demodernized packaging.

* Thu Feb 01 2024 Andrey Limachko <liannnix@altlinux.org> 5.11.0-alt1
- 5.11.0

* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 5.10.0-alt1
- Initial build for Sisyphus
