%define _unpackaged_files_terminate_build 1
%define pypi_name handy-archives
%define mod_name handy_archives

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: Some handy archive helpers for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/handy-archives/
Vcs: https://github.com/domdfcoding/handy-archives

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-test
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

# use reason= instead of deprecated msg= arg for pytest.skip()
sed -i '/pytest.skip/ s/msg/reason/' tests/test_zipfile.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt2
- fix requires

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt1
- initial build for Sisyphus (temporary broken package)

