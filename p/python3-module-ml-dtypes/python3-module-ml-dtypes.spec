%define _unpackaged_files_terminate_build 1
%define pypi_name ml-dtypes
%define mod_name ml_dtypes

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1

Summary: A stand-alone implementation of several NumPy dtype extensions used in machine learning
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/ml-dtypes/
Vcs: https://github.com/jax-ml/ml_dtypes

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: %name-%version-third_party-eigen.tar
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: gcc-c++
BuildRequires: libnumpy-py3-devel
%if_with check
%add_pyproject_deps_check_filter pyink
%pyproject_builddeps_metadata_extra dev
BuildRequires: python3-module-numpy-testing
%endif

%description
%summary.

%prep
%setup -a2
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- pytest -vra --import-mode append ml_dtypes/tests

%files
%doc CHANGELOG.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 18 2025 Anton Zhukharev <ancieg@altlinux.org> 0.5.2-alt1
- Packaged for ALT Sisyphus.
