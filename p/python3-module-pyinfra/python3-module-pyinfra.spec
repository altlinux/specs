%define _unpackaged_files_terminate_build 1
%define pypi_name pyinfra
%define mod_name pyinfra

%def_with check

Name: python3-module-%pypi_name
Version: 3.7
Release: alt1

Summary: pyinfra automates/provisions/manages/deploys infrastructure
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyinfra/
Vcs: https://github.com/pyinfra-dev/pyinfra

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
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# from 'dev' depgroup with excessive dependencies
BuildRequires: python3-module-freezegun
%endif

%description
pyinfra turns Python code into shell commands and runs them on your
servers. Execute ad-hoc commands and write declarative operations.
Target SSH servers, local machine and Docker containers. Fast and
scales from one server to thousands. Think ansible but Python instead
of YAML, and a lot faster.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/pyinfra_cli/
%_bindir/pyinfra

%changelog
* Sat Mar 14 2026 Anton Zhukharev <ancieg@altlinux.org> 3.7-alt1
- Updated to 3.7.

* Thu Jan 15 2026 Anton Zhukharev <ancieg@altlinux.org> 3.6-alt1
- Packaged for ALT Sisyphus.
