%define _unpackaged_files_terminate_build 1
%define oname lia-web

%def_with check

Name: python3-module-%oname
Version: 0.2.3
Release: alt2

Summary: A universal web framework adapter for Python that lets you write code once and use it across multiple web frameworks
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lia-web/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-quart
BuildRequires: python3-module-httpx
BuildRequires: python3-module-litestar
BuildRequires: python3-module-chalice
BuildRequires: python3-module-python-multipart
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-aiohttp-tests
BuildRequires: python3-module-sanic
BuildRequires: python3-module-sanic-testing
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%py3_provides %oname

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_litestar_adapter"

%files
%doc *.md
%python3_sitelibdir/lia/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.2.3-alt2
- Fix tests.

* Wed Aug 13 2025 Alexander Burmatov <thatman@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus.
