%define _unpackaged_files_terminate_build 1
%define pypi_name bidict

# TODO: Make tests work
%def_without check

Name:    python3-module-%pypi_name
Version: 0.22.1
Release: alt1

Summary: The bidirectional mapping library for Python
License: MPL-2.0
Group:   Development/Python3
URL:     https://bidict.readthedocs.io
VCS:     https://github.com/jab/bidict

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

%description
The bidirectional mapping library for Python.
Features:
- Depended on by Google, Venmo, CERN, Baidu, Tencent, and teams across
  the world since 2009.
- Familiar, Pythonic APIs that are carefully designed for safety,
  simplicity, flexibility, and ergonomics.
- Lightweight, with no runtime dependencies outside Python standard
  library.
- Implemented in concise, well-factored, fully type-hinted Python code
  that is optimized for running efficiently as well as for long-term
  maintenance and stability (as well as joy).
- Extensively documented.
- 100%% test coverage running continuously across all supported Python
  versions.

%prep
%setup -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst docs
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 20 2023 Andrey Limachko <liannnix@altlinux.org> 0.22.1-alt1
- Initial build for Sisyphus
