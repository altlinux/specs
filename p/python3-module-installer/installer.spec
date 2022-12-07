%define _unpackaged_files_terminate_build 1
%define pypi_name installer

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: A library for installing Python wheels
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/installer
VCS: https://github.com/pypa/installer.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend
BuildRequires: python3(flit_core)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

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

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/installer/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Dec 07 2022 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.1 -> 0.6.0.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus.
