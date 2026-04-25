%define pypi_name slowapi

%def_with check

Name:    python3-module-%pypi_name
Version: 0.1.9
Release: alt1

Summary: A rate limiter for Starlette and FastAPI
License: MIT
Group:   Development/Python3
URL:     https://github.com/laurents/slowapi

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-mock
BuildRequires: python3-module-limits
BuildRequires: python3-module-hiro
BuildRequires: python3-module-httpx
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
%pyproject_run_pytest -k "not (test_headers_no_breach or test_headers_breach or test_retry_after or test_exempt_decorator)"

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 20 2026 Alexander Burmatov <thatman@altlinux.org> 0.1.9-alt1
- Initial build for Sisyphus.
