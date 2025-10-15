%define _unpackaged_files_terminate_build 1

%define pypi_name httpx-sse
%define mod_name httpx_sse

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.3
Release: alt1
Summary: Consume Server-Sent Event (SSE) messages with HTTPX
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/httpx-sse/
Vcs:     https://github.com/florimondmanca/httpx-sse
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-httpx
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-sse-starlette
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=''

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 0.4.3-alt1
- 0.4.1 -> 0.4.3.

* Fri Jul 11 2025 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1.

* Tue Aug 06 2024 Alexander Burmatov <thatman@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
