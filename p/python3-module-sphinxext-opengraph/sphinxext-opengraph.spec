%define _unpackaged_files_terminate_build 1
%define pypi_name sphinxext-opengraph
%define mod_name opengraph

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.0
Release: alt1
Summary: Sphinx extension to generate unique OpenGraph metadata
License: BSD-3-Clause
Group: Development/Python3
Url: https://sphinxext-opengraph.readthedocs.io
VCS: https://github.com/wpilibsuite/sphinxext-opengraph
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-tests
%endif

%description
Sphinx extension to generate OpenGraph metadata

%prep
%setup
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
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/sphinxext/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Apr 07 2025 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.8.0 -> 0.10.0.

* Wed Feb 08 2023 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.6.3 -> 0.8.0.

* Fri Apr 15 2022 Egor Ignatov <egori@altlinux.org> 0.6.3-alt1
- new version 0.6.3

* Mon Jan 10 2022 Egor Ignatov <egori@altlinux.org> 0.5.1-alt1
- 0.5.1

* Wed Dec 01 2021 Egor Ignatov <egori@altlinux.org> 0.5.0-alt1
- 0.5.0

* Wed Sep 01 2021 Egor Ignatov <egori@altlinux.org> 0.4.2-alt1
- Initial build for ALT
