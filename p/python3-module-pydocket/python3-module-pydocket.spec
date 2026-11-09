%define _unpackaged_files_terminate_build 1
%define pypi_name pydocket
%define mod_name docket

# tests require running docker
%def_without check

Name: python3-module-%pypi_name
Version: 0.28.0
Release: alt1

Summary: A distributed background task system for Python functions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydocket/
Vcs: https://github.com/chrisguidry/docket

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

# 'codespell' is provided by 'codespell' package, not 'python3-module-codespell'
%pyproject_configure_with_check_filter codespell
%pyproject_configure_with_check_filter loq
%pyproject_configure_with_check_filter pytest-flakefinder
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0
%if_with check
BuildRequires: codespell
%endif

%description
Docket is a distributed background task system for Python functions with
a focus on the scheduling of future work as seamlessly and efficiently
as immediate work.

%prep
%setup
%autopatch -p1
%pyproject_scm_init python/v%version
cd python
%pyproject_setup_deps

%build
cd python
%pyproject_build

%install
cd python
%pyproject_install

%check
cd python
%pyproject_run_pytest -vra -o=addopts= tests/cli

%files
%_bindir/docket
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 09 2026 Anton Zhukharev <ancieg@altlinux.org> 0.28.0-alt1
- Updated to 0.28.0.

* Thu Aug 20 2026 Anton Zhukharev <ancieg@altlinux.org> 0.24.1-alt1
- Packaged for ALT Sisyphus.
