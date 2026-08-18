%define _unpackaged_files_terminate_build 1
# The test suite conftest unconditionally imports seleniumbase, a browser
# testing framework not available in Sisyphus, so %%check is disabled.
%def_without check
%if_with check
%define pyproject_deps_check_filter %nil
%add_pyproject_deps_check_filter 'pytest-playwright$'
%add_pyproject_deps_check_filter 'typing[-_]extensions$'
%endif

%define pypi_name sphinxext-rediraffe

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Sphinx Extension that redirects non-existent pages to working pages
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/sphinxext-rediraffe/
Vcs: https://github.com/sphinx-doc/sphinxext-rediraffe
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Sphinx Extension that redirects non-existent pages to working pages.

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
%pyproject_run_pytest tests

%files
%doc LICENCE.rst README.rst
%python3_sitelibdir/sphinxext/rediraffe.py
%python3_sitelibdir/sphinxext/__pycache__/rediraffe.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.0-alt1
- Initial build for ALT Sisyphus.
