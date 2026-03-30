%define _unpackaged_files_terminate_build 1
%define pypi_name loky

%def_with check

Name: python3-module-%pypi_name
Version: 3.5.6
Release: alt1.1
Summary: A robust implementation of concurrent.futures.ProcessPoolExecutor
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/loky
Vcs: https://github.com/joblib/loky
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# required by loky/backend/context.py:_count_physical_cores_linux
Requires: /proc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-cloudpickle
BuildRequires: python3-module-packaging
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pytest
BuildRequires: /proc
%endif

# filter MS Windows related deps
%filter_from_requires /python3(msvcrt\(\..*\)\?)/d
%filter_from_requires /python3(_winapi\(\..*\)\?)/d
%filter_from_requires /python3(multiprocessing\.popen_spawn_win32\(\..*\)\?)/d

%description
Provides a robust, cross-platform and cross-version implementation of the
ProcessPoolExecutor class of concurrent.futures

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --skip-high-memory -ra

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.5.6-alt1.1
- Demodernized packaging.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 3.5.6-alt1
- 3.5.5 -> 3.5.6.

* Thu May 29 2025 Stanislav Levin <slev@altlinux.org> 3.5.5-alt1
- 3.5.1 -> 3.5.5.

* Wed Mar 19 2025 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.5.0 -> 3.5.1.

* Mon Mar 17 2025 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.4.1 -> 3.5.0.

* Thu Mar 21 2024 Stanislav Levin <slev@altlinux.org> 3.4.1-alt2
- Fixed FTBFS (Python 3.12).

* Thu Aug 10 2023 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.3.0 -> 3.4.1.

* Tue Sep 20 2022 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
