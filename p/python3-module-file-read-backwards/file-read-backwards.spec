%define _unpackaged_files_terminate_build 1
%define pypi_name file-read-backwards
%define mod_name file_read_backwards

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.0
Release: alt1
Summary: Memory efficient way of reading files line-by-line from the end of file
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/file-read-backwards/
Vcs: https://github.com/RobinNil/file_read_backwards
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-mock
%endif

%description
Memory efficient way of reading files line-by-line from the end of file.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 21 2024 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.0.0 -> 3.1.0.

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Sisyphus
