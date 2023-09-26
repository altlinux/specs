%define _unpackaged_files_terminate_build 1
%define pypi_name aiocarbon

# tests are broken
%def_without check

Name: python3-module-%pypi_name
Version: 0.15.3
Release: alt1

Summary: Asynchronous client for carbon
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiocarbon/
Vcs: https://github.com/mosquito/aiocarbon

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

# fix version
VERSION=`python3 -c 'print(tuple(map(int, "%version".split("."))))'`
sed -i "/version_info =/s/= .*/ = ${VERSION}/" %pypi_name/version.py

# fix python_requires version specifier
sed -i '/python_requires=/s/3.5.\*/3.5/' setup.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENCE.md README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 0.15.3-alt1
- Updated to 0.15.3.

* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.15.2-alt1
- Changed version to 0.15.2.

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.15.1-alt1.git0dbbe0c
- Initial commit for ALT Sisyphus.

