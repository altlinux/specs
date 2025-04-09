%define _unpackaged_files_terminate_build 1
%define pypi_name llm
%define pypi_nname llm
%define mod_name llm

%def_with check

Name: python3-module-%pypi_nname
Version: 0.24.2
Release: alt1

Summary: Access large language models from the command-line
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/llm/
Vcs: https://github.com/simonw/llm

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
A CLI utility and Python library for interacting with Large Language
Models, both via remote APIs and models that can be installed and run
on your own machine.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc README.md
%_bindir/llm
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 09 2025 Anton Zhukharev <ancieg@altlinux.org> 0.24.2-alt1
- Updated to 0.24.2.

* Tue Apr 08 2025 Anton Zhukharev <ancieg@altlinux.org> 0.24-alt1
- Updated to 0.24.

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.23-alt1
- Built for ALT Sisyphus.

