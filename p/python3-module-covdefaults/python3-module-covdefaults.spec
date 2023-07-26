%define _unpackaged_files_terminate_build 1
%define pypi_name covdefaults

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: A coverage plugin to provide sensible default settings
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/covdefaults/
Vcs: https://github.com/asottile/covdefaults

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-coverage
%endif

%description
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 26 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.2-alt1
- 2.2.0 -> 2.2.2

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- initial build for Sisyphus

