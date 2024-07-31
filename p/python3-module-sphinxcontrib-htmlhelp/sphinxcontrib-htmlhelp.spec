%define _unpackaged_files_terminate_build 1
%define pypi_name sphinxcontrib-htmlhelp
%define ns_name sphinxcontrib
%define mod_name htmlhelp

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: A sphinx extension which renders HTML help files
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/sphinxcontrib-htmlhelp
Vcs: https://github.com/sphinx-doc/sphinxcontrib-htmlhelp
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra standalone
# filtered by default but actually used
BuildRequires: python3-module-sphinx
# subpackaged
BuildRequires: python3-module-sphinx-tests
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.rst
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 29 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.6 -> 2.1.0.

* Mon Jul 22 2024 Stanislav Levin <slev@altlinux.org> 2.0.6-alt1
- 2.0.5 -> 2.0.6.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 2.0.5-alt1
- 2.0.0 -> 2.0.5.

* Sat Apr 16 2022 Fr. Br. George <george@altlinux.ru> 2.0.0-alt2
- Fix old version in version.py

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Mon Apr 29 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- new version 1.0.2

* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
