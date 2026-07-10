%define _unpackaged_files_terminate_build 1
%define pypi_name rustypie
%define mod_name rusty

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: Rust-inspired implementations of Result<T, E>, Option<T> and Iter<T> data types for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rustypie/
Vcs: https://github.com/dshein-alt/rusty

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
%pyproject_builddeps_metadata_extra dev
%endif

%description
%summary.

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
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 10 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Packaged for ALT Sisyphus.
