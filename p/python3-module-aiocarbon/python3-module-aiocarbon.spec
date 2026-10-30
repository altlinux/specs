%define _unpackaged_files_terminate_build 1
%define pypi_name aiocarbon
%define mod_name aiocarbon

%def_with check

Name: python3-module-%pypi_name
Version: 0.17.0
Release: alt1

Summary: Asynchronous client for carbon
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiocarbon/
Vcs: https://github.com/mosquito/aiocarbon

BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

# Set version instead of forgetful upstream
sed -i '/^version/s/= .*/= "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 30 2026 Anton Zhukharev <ancieg@altlinux.org> 0.17.0-alt1
- Updated to 0.17.0.

* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 0.15.3-alt1
- Updated to 0.15.3.

* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.15.2-alt1
- Changed version to 0.15.2.

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.15.1-alt1.git0dbbe0c
- Initial commit for ALT Sisyphus.
