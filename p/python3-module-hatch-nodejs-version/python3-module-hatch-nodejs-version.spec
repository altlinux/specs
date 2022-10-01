%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-nodejs-version

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Hatch plugin to read pyproject.toml metadata from package.json
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-nodejs-version/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
This package provides two Hatch plugins:

* version source plugin that reads/writes the package version from the
  version field of the Node.js package.json file.

* metadata hook plugin that reads PEP 621 metadata from the Node.js
  package.json file.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/hatch_nodejs_version/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- initial build for Sisyphus

