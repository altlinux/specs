%define _unpackaged_files_terminate_build 1
%define pypi_name rfc3339-validator
%define mod_name rfc3339_validator

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.4
Release: alt1

Summary: A pure python RFC3339 validator
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/rfc3339-validator
VCS: https://github.com/naimetti/rfc3339-validator
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

# mapping of PyPI name to distro name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter bump2version
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync check pip_reqfile requirements_dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.*
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 14 2023 Anton Vyatkin <toni@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus
