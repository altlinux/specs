%define _unpackaged_files_terminate_build 1
%define pypi_name pyinfra-testgen
%define mod_name testgen

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: Generate Python unit tests from JSON and YAML files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyinfra-testgen/
Vcs: https://github.com/pyinfra-dev/testgen

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jan 15 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Packaged for ALT Sisyphus.
