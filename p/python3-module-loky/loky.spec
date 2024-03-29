%define _unpackaged_files_terminate_build 1
%define pypi_name loky

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.1
Release: alt2
Summary: A robust implementation of concurrent.futures.ProcessPoolExecutor
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/loky
Vcs: https://github.com/joblib/loky
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /proc
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
Provides a robust, cross-platform and cross-version implementation of the
ProcessPoolExecutor class of concurrent.futures

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
* Thu Mar 21 2024 Stanislav Levin <slev@altlinux.org> 3.4.1-alt2
- Fixed FTBFS (Python 3.12).

* Thu Aug 10 2023 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.3.0 -> 3.4.1.

* Tue Sep 20 2022 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
