%define pypi_nname mss
%define _unpackaged_files_terminate_build 1

Name: python3-module-%pypi_nname
Version: 9.0.1
Release: alt1

Summary: An ultra fast cross-platform multiple screenshots module in pure python using ctypes.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mss/
VCS: https://github.com/click-contrib/click-plugins.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
An ultra fast cross-platform multiple screenshots module
in pure python using ctypes.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/%pypi_nname
%python3_sitelibdir/*

%changelog
* Tue Dec 12 2023 Mikhail Chernonog <snowmix@altlinux.org> 9.0.1-alt1
- Initial build for Sisyphus
