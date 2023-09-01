%define _unpackaged_files_terminate_build 1
%define pypi_name autoflake

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: Removes unused imports and unused variables as reported by pyflakes
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/autoflake/
Vcs: https://github.com/PyCQA/autoflake

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
autoflake removes unused imports and unused variables from Python code.
It makes use of pyflakes to do this.

By default, autoflake only removes unused imports for modules that are
part of the standard library. (Other modules may have side effects
that make them unsafe to remove automatically.)
Removal of unused variables is also disabled by default.

autoflake also removes useless pass statements by default.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

rm %buildroot%python3_sitelibdir/{LICENSE,README.md}

find %buildroot%python3_sitelibdir -name 'test_*' -exec rm -rfv {} \;

%check
%pyproject_run_unittest test_autoflake.py

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/*

%changelog
* Fri Sep 01 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1.

* Thu Aug 03 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- Built for ALT Sisyphus.

