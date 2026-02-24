%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-examples
%define mod_name pyproject_examples

%def_with check

Name: python3-module-%pypi_name
Version: 2026.2.3
Release: alt1

Summary: Example pyproject.toml configs for testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-examples
Vcs: https://github.com/repo-helper/pyproject-examples

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

These are designed to be used in the testsuite for pyproject-parser and
whey, but may be useful for other tools based on those.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

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
* Tue Feb 24 2026 Anton Zhukharev <ancieg@altlinux.org> 2026.2.3-alt1
- Updated to 2026.2.3.

* Thu Jul 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2023.6.30-alt1
- Built for ALT Sisyphus.
