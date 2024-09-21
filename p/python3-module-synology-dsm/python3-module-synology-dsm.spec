%define _unpackaged_files_terminate_build 1
%def_without check

Name: python3-module-synology-dsm
Version: 2.5.2
Release: alt1
Summary: Asynchronous Python API for Synology DSM
License: MIT
Group: Development/Python3
Url: https://github.com/mib1185/py-synologydsm-api
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-async-timeout
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
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
%pyproject_run_pytest

%files
%python3_sitelibdir/synology_dsm
%python3_sitelibdir/%{pyproject_distinfo py_synologydsm_api}
%exclude %_bindir/synologydsm-api

%changelog
* Sun Sep 08 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.2-alt1
- Updated to version 2.5.2.

* Fri Apr 19 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.2-alt1
- Updated to version 2.4.2.

* Sat Feb 10 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.3.0-alt1
- Initial build for ALT.
