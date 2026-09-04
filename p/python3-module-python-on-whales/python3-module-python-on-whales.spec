%define _unpackaged_files_terminate_build 1
%define pypi_name python-on-whales
%define mod_name python_on_whales

# requires running docker daemon
%def_without check

Name: python3-module-%pypi_name
Version: 0.81.0
Release: alt1

Summary: A Docker client for Python, designed to be fun and intuitive!
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-on-whales/
Vcs: https://github.com/gabrieldemarmiesse/python-on-whales

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
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install
rm -v %buildroot%_bindir/python-on-whales

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 04 2026 Anton Zhukharev <ancieg@altlinux.org> 0.81.0-alt1
- Packaged for ALT Sisyphus.
