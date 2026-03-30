%define _unpackaged_files_terminate_build 1
%define pypi_name time-machine
%define mod_name time_machine

# %%python3_set_limited_api is not supported yet

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 3.2.0
Release: alt1.1
Summary: Travel through time in your tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/time-machine
Vcs: https://github.com/adamchainz/time-machine
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-randomly
BuildRequires: python3-module-python-dateutil

BuildRequires: python3-module-tokenize-rt
%endif

%description
%summary.

%add_python_extra cli

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_%mod_name.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1.1
- Demodernized packaging.

* Thu Dec 18 2025 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.1.0 -> 3.2.0.

* Wed Nov 26 2025 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.19.0 -> 3.1.0.

* Wed Sep 03 2025 Stanislav Levin <slev@altlinux.org> 2.19.0-alt1
- 2.17.0 -> 2.19.0.

* Wed Aug 06 2025 Stanislav Levin <slev@altlinux.org> 2.17.0-alt1
- 2.16.0 -> 2.17.0.

* Wed Oct 09 2024 Stanislav Levin <slev@altlinux.org> 2.16.0-alt1
- 2.15.0 -> 2.16.0.

* Wed Sep 25 2024 Stanislav Levin <slev@altlinux.org> 2.15.0-alt1
- 2.14.2 -> 2.15.0.

* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 2.14.2-alt1
- 2.14.1 -> 2.14.2.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 2.14.1-alt1
- 2.14.0 -> 2.14.1.

* Mon Mar 04 2024 Stanislav Levin <slev@altlinux.org> 2.14.0-alt1
- 2.13.0 -> 2.14.0.

* Thu Sep 28 2023 Stanislav Levin <slev@altlinux.org> 2.13.0-alt1
- 2.12.0 -> 2.13.0.

* Tue Aug 15 2023 Stanislav Levin <slev@altlinux.org> 2.12.0-alt1
- 2.11.0 -> 2.12.0.

* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 2.11.0-alt1
- 2.10.0 -> 2.11.0.

* Tue Jun 20 2023 Stanislav Levin <slev@altlinux.org> 2.10.0-alt1
- 2.9.0 -> 2.10.0.

* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus.
