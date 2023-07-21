%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-examples
%define mod_name pyproject_examples

%def_with check

Name: python3-module-%pypi_name
Version: 2023.6.30
Release: alt1

Summary: Example pyproject.toml configs for testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-examples
Vcs: https://github.com/repo-helper/pyproject-examples

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-importcheck
%endif

%description
%summary.

These are designed to be used in the testsuite for pyproject-parser and
whey, but may be useful for other tools based on those.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- importcheck --show

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jul 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2023.6.30-alt1
- Built for ALT Sisyphus.
