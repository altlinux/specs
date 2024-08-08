%define pypi_name sanic

%ifarch ppc64le aarch64
# The tests take too long
%def_without check
%else
%def_with check
%endif

Name:    python3-module-%pypi_name
Version: 24.6.0
Release: alt2

Summary: Accelerate your web app development | Build fast, run fast
License: MIT
Group:   Development/Python3
URL:     https://github.com/sanic-org/sanic

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sanic-routing
BuildRequires: python3-module-sanic-testing
BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-aioquic
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-anyio
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pytest-benchmark
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Sanic is a Python 3.8+ web server and web framework that's written to go fast.
It allows the usage of the async/await syntax added in Python 3.5, which makes
your code non-blocking and speedy.
Sanic is also ASGI compliant, so you can deploy it with an alternative ASGI
webserver.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_websocket_route_with_subprotocols and not test_keep_alive_client_timeout"

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 08 2024 Alexander Burmatov <thatman@altlinux.org> 24.6.0-alt2
- Enable tests.

* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 24.6.0-alt1
- Initial build for Sisyphus.
