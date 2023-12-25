%define _unpackaged_files_terminate_build 1
%define pypi_name astunparse

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.3
Release: alt1

Summary: An AST unparser for Python
License: PSF-2.0
Group: Development/Python3
Url: https://pypi.org/project/astunparse/
Vcs: https://github.com/simonpercivall/astunparse

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
An AST unparser for Python.

This is a factored out version of unparse found in the Python source
distribution; under Demo/parser in Python 2 and under Tools/parser
in Python 3.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test_requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 22 2023 Anton Zhukharev <ancieg@altlinux.org> 1.6.3-alt1
- Built for ALT Sisyphus.

