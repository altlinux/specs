%define _unpackaged_files_terminate_build 1
%define pypi_name requests-ratelimiter
%define mod_name requests_ratelimiter

%def_without check

Name: python3-module-%pypi_name
Version: 0.9.2
Release: alt1
Summary: Easy rate-limiting for python requests
License: MIT
Group: Development/Python3
Url: https://github.com/JWCook/requests-ratelimiter
Vcs: https://pypi.org/project/requests-ratelimiter/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3-module-pyrate-limiter
BuildRequires: python3(coverage)
BuildRequires: python3-module-pre-commit
BuildRequires: python3(requests)
BuildRequires: python3(furo)
BuildRequires: python3-module-myst-parser
BuildRequires: python3(sphinx)
BuildRequires: python3-module-sphinx-autodoc-typehints
BuildRequires: python3-module-sphinx-copybutton

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-requests-cache
%endif

%py3_provides %pypi_name

%description
This package is a simple wrapper around pyrate-limiter
that adds convenient integration with the requests library.

%prep
%setup
%autopatch -p1
sed -i 's/from requests_ratelimiter import \*/import requests_ratelimiter/' test/test_exports.py
sed -i 's/buffer_ms=50//g' requests_ratelimiter/requests_ratelimiter.py
sed -i 's/, *blocking=True//g' requests_ratelimiter/requests_ratelimiter.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Wed Mar 04 2026 Pavel Shilov <zerospirit@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus.

