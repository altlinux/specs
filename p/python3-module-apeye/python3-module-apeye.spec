%define _unpackaged_files_terminate_build 1
%define pypi_name apeye

# tests disabled due to Internet connection requirement
%def_without check

Name: python3-module-%pypi_name
Version: 1.4.1
Release: alt1

Summary: Handy tools for working with URLs and APIs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/apeye/
Vcs: https://github.com/domdfcoding/apeye

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

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
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Aug 18 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- Updated to 1.4.1.

* Thu Jul 20 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- New version.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- initial build for Sisyphus

