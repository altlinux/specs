%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-nodejs-version
%define mod_name hatch_nodejs_version

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.2
Release: alt1

Summary: Hatch plugin to read pyproject.toml metadata from package.json
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-nodejs-version/
Vcs: https://github.com/agoose77/hatch-nodejs-version

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
This package provides two Hatch plugins:

* version source plugin that reads/writes the package version from the
  version field of the Node.js package.json file.

* metadata hook plugin that reads PEP 621 metadata from the Node.js
  package.json file.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pdm dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- initial build for Sisyphus

