%define pypi_name httpx-sse
%define mod_name httpx_sse

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Consume Server-Sent Event (SSE) messages with HTTPX
License: MIT
Group:   Development/Python3
URL:     https://github.com/florimondmanca/httpx-sse

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-httpx
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-sse-starlette
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --cov-fail-under=0

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 06 2024 Alexander Burmatov <thatman@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
