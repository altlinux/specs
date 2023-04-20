%define _unpackaged_files_terminate_build 1
%define pypi_name installer

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1
Summary: A library for installing Python wheels
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/installer
VCS: https://github.com/pypa/installer.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter pytest-xdist
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%pypi_name is a low-level library for installing a Python package from a
wheel distribution. It provides basic functionality and abstractions for
handling wheels and installing packages from wheels.

- Logic for "unpacking" a wheel (i.e. installation).
- Abstractions for various parts of the unpacking process.
- Extensible simple implementations of the abstractions.
- Platform-independent Python script wrapper generation.

%prep
%setup
%autopatch -p1

# don't ship `exe`s
find -type f -name '*.exe' -delete

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.md
%python3_sitelibdir/installer/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Apr 20 2023 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- 0.6.0 -> 0.7.0.

* Wed Dec 07 2022 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.1 -> 0.6.0.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus.
