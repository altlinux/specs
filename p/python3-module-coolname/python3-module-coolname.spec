%define _unpackaged_files_terminate_build 1
%define pypi_name coolname
%define mod_name coolname

%def_with check

Name: python3-module-%pypi_name
Version: 5.0.0
Release: alt1

Summary: Random name and slug generator
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/coolname/
Vcs: https://github.com/alexanderlukanin13/coolname

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%_bindir/coolname
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 19 2026 Anton Zhukharev <ancieg@altlinux.org> 5.0.0-alt1
- Packaged for ALT Sisyphus.
