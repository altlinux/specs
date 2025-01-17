%define _unpackaged_files_terminate_build 1
%define pypi_name pyrate-limiter
%define mod_name pyrate_limiter

%def_with check

Name:    python3-module-%pypi_name
Version: 3.7.0
Release: alt1

Summary:   The request rate limiter using Leaky-bucket Algorithm
License:   MIT
Group:     Development/Python3
Url:       https://github.com/vutran1710/PyrateLimiter
Vcs:       https://github.com/vutran1710/PyrateLimiter.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pytest-asyncio
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 01 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 3.7.0-alt1
  - Initial build for ALT.
