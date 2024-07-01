%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-examples
%define mod_name pytest_examples

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.10
Release: alt4

Summary: Pytest plugin for testing examples in docstrings and markdown files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-examples/
Vcs: https://github.com/pydantic/pytest-examples

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
BuildRequires: python3-module-black
BuildRequires: python3-module-ruff
%endif

%description
Pytest plugin for testing Python code examples in docstrings
and markdown files.

pytest-examples can:

* lint code examples using ruff and black
* run code examples
* run code examples and check print statements are inlined correctly
  in the code

It can also update code examples in place to format them and insert
or update print statements.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
cat requirements/{pyproject,testing}.txt > requirements.txt
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.10-alt4
- Fixed FTBFS (ruff 0.5.0).

* Tue Feb 06 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.10-alt3
- Fixed FTBFS.

* Wed Oct 18 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.10-alt2
- Fixed FTBFS (ruff 0.1.0).

* Thu Sep 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.10-alt1
- Built for ALT Sisyphus.

