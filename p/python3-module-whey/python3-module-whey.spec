%define _unpackaged_files_terminate_build 1
%define pypi_name whey
%define mod_name %pypi_name

# tests disabled becase they need whey-conda
%def_without check

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: A simple Python wheel builder for simple projects
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/whey/
Vcs: https://github.com/repo-helper/whey

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
A simple Python wheel builder for simple projects.

whey:
* supports PEP 621 metadata.
* can be used as a PEP 517 build backend.
* creates PEP 427 wheels.
* handles type hint files (py.typed and *.pyi stubs).
* is distributed under the MIT License.
* is the liquid remaining after milk has been curdled and strained.
  It is a byproduct of the manufacture of cheese and has several
  commercial uses.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 27 2024 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Thu Apr 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.1.0-alt1
- Updated to 0.1.0.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.24-alt1.gitde39bb1
- Updated to 0.0.24.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.23-alt1
- initial build for Sisyphus

