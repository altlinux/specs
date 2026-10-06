%define _unpackaged_files_terminate_build 1

Name: python3-module-tarsafe

Version: 0.0.6
Release: alt1.git3cadb99

Summary: A safe subclass of the TarFile class for interacting with tar files
License: MIT
Group: Development/Python
Url: https://pypi.org/project/tarsafe/
Vcs: https://github.com/beatsbears/tarsafe

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch0: tarsafe-0.0.6-use-setuptools-backend.patch
Patch1: tarsafe-0.0.6-exclude-test-package.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Tarsafe is a drop-in replacement for the tarfile module from the standard
library. Before extracting, it checks every archive member and raises
TarSafeException if a member would be written outside the target directory
(including via symlinks or hard links) or is a device file.

%prep
%setup
%patch0 -p1
%patch1 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test

%files
%doc *.md LICENSE
%python3_sitelibdir_noarch/tarsafe
%python3_sitelibdir_noarch/%{pyproject_distinfo tarsafe}

%changelog
* Tue Sep 29 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 0.0.6-alt1.git3cadb99
- Initial build for Sisyphus.

