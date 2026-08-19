%define _unpackaged_files_terminate_build 1
%define pypi_name uncalled-for
%define mod_name uncalled_for

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Async dependency injection for Python functions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/uncalled-for/
Vcs: https://github.com/chrisguidry/uncalled-for

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
# 'codespell' is provided by 'codespell' package, not 'python3-module-codespell'
%add_pyproject_deps_check_filter codespell
BuildRequires: codespell
%add_pyproject_deps_check_filter loq
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Async dependency injection for Python functions.

Declare what your function needs as parameter defaults. They show up resolved
when the function runs. No ceremony, no container, no configuration.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 19 2026 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- Packaged for ALT Sisyphus.
