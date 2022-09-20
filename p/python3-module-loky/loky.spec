%define _unpackaged_files_terminate_build 1
%define pypi_name loky

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: A robust implementation of concurrent.futures.ProcessPoolExecutor
License: BSD
Group: Development/Python3
# Source-git: https://github.com/joblib/loky.git
Url: https://pypi.org/project/loky

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# deps
BuildRequires: python3(cloudpickle)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

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
%tox_check_pyproject -- -vra

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Sep 20 2022 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
