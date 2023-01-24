%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject_hooks
%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1
Summary: Wrappers to call pyproject.toml-based build backend hooks
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject_hooks
VCS: https://github.com/pypa/pyproject-hooks
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%if %tomli
%py3_requires tomli
%endif

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(flit_core)

%if_with check
# synced to dev-requirements.txt
BuildRequires: python3(pytest)
BuildRequires: python3(testpath)
BuildRequires: python3(setuptools)
%if %tomli
BuildRequires: python3(tomli)
%endif
%endif

%description
This is a low-level library for calling build-backends in pyproject.toml-based
project. It provides the basic functionality to help write tooling that
generates distribution files from Python projects.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
