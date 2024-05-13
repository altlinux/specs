%define _unpackaged_files_terminate_build 1

%define pypi_name pynput
%define mod_name %pypi_name

Name: python3-module-pynput
Version: 1.7.7
Release: alt1

Summary: Monitor and control user input devices

License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/pynput/
Vcs: https://github.com/moses-palmer/pynput
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter setuptools-lint
%pyproject_builddeps_build

%description
This library allows you to control and monitor input devices.

Currently, mouse and keyboard input and monitoring are supported.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

rm -v lib/pynput/*/*darwin* lib/pynput/*/*win32*

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 13 2024 Stanislav Levin <slev@altlinux.org> 1.7.7-alt1
- 1.7.6 -> 1.7.7.

* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 1.7.6-alt2
- Fixed FTBFS (missing build dependency on six).

* Sat Mar 11 2023 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt1
- initial build for ALT Sisyphus
