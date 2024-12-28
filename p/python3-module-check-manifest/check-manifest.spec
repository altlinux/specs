%define _unpackaged_files_terminate_build 1

%define pypi_name check-manifest
%define mod_name check_manifest

%def_with check

Name: python3-module-%pypi_name
Version: 0.50
Release: alt1
Summary: Check MANIFEST.in in a Python source package for completeness
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/check-manifest/
Vcs: https://github.com/mgedmin/check-manifest
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
Conflicts: python-module-%pypi_name
Obsoletes: python-module-%pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: %_bindir/git
%endif

%description
Are you a Python developer?
Have you uploaded packages to the Python Package Index?
Have you accidentally uploaded broken packages with some files missing?
If so, check-manifest is for you.

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
%pyproject_run_pytest -ra

%files
%doc README.*
%_bindir/check-manifest
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 0.50-alt1
- 0.37 -> 0.50.

* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.37-alt2
- Drop python2 support.

* Fri Sep 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.37-alt1
- Updated to upstream version 0.37.

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.36-alt1
- Initial build for ALT.
