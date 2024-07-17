%define _unpackaged_files_terminate_build 1
%define pypi_name pip-run

%def_with check

Name: python3-module-%pypi_name
Version: 13.0.0
Release: alt1
Summary: Install packages and run Python with them
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pip-run
VCS: https://github.com/jaraco/pip-run.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage extras dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
pip-run provides on-demand temporary package installation for a single
interpreter run.

%prep
%setup
%autopatch -p1
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
%doc README.rst
%_bindir/pip-run
%python3_sitelibdir/pip-run.py
%python3_sitelibdir/__pycache__/pip-run.*
%python3_sitelibdir/pip_run/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 17 2024 Stanislav Levin <slev@altlinux.org> 13.0.0-alt1
- 12.7.0 -> 13.0.0.

* Tue Jul 16 2024 Stanislav Levin <slev@altlinux.org> 12.7.0-alt1
- 12.6.1 -> 12.7.0.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 12.6.1-alt1
- 12.1.0 -> 12.6.1.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 12.1.0-alt1
- 10.1.1 -> 12.1.0.

* Wed May 24 2023 Stanislav Levin <slev@altlinux.org> 10.1.1-alt1
- 10.0.7 -> 10.1.1.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 10.0.7-alt1
- 10.0.5 -> 10.0.7.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 10.0.5-alt1
- 9.2.0 -> 10.0.5.

* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 9.2.0-alt1
- 8.8.2 -> 9.2.0.

* Mon Nov 21 2022 Stanislav Levin <slev@altlinux.org> 8.8.2-alt1
- 8.8.1 -> 8.8.2.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 8.8.1-alt1
- 8.8.0 -> 8.8.1.

* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 8.8.0-alt1
- Initial build for Sisyphus.
