%define _unpackaged_files_terminate_build 1

%define pypi_name jaraco.logging
%define ns_name jaraco
%define mod_name logging

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.0
Release: alt1

Summary: Support for Python logging facility
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.logging/
Vcs: https://github.com/jaraco/jaraco.logging
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
# requires internet
%add_pyproject_deps_build_filter coherent-licensed
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name.py
%dir %python3_sitelibdir/%ns_name/__pycache__/
%python3_sitelibdir/%ns_name/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jul 01 2025 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.0 -> 3.4.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Jul 24 2024 Anton Vyatkin <toni@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
