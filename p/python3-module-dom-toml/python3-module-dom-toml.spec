%define _unpackaged_files_terminate_build 1
%define pypi_name dom-toml
%define mod_name dom_toml

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.1
Release: alt2

Summary: Dom's tools for Tom's Obvious, Minimal Language
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dom-toml/
Vcs: https://github.com/domdfcoding/dom_toml

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: dom-toml-0.6.1-py312-fix.patch

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 02 2024 Anton Vyatkin <toni@altlinux.org> 0.6.1-alt2
- (NMU) Fixed FTBFS (with python 3.12)

* Wed May 10 2023 Anton Zhukharev <ancieg@altlinux.org> 0.6.1-alt1
- New version.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.0-alt2
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.0-alt1
- initial build for Sisyphus

