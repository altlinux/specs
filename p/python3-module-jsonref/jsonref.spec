%define _unpackaged_files_terminate_build 1
%define pypi_name jsonref
%define mod_name jsonref
%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: A library for automatic dereferencing of JSON Reference objects for Python (supporting Python 3.7+)

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jsonref/
VCS: https://github.com/gazpachoking/jsonref

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Jsonref library lets you use a data structure with JSON
reference objects, as if the references had been replaced
with the referent data. There aresome features like lazily
evaluation of references, so nothing is deferenced until
it is used, and supporting recursive references, and
creating recursive python data structures.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pdm test
%endif

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE* *.md
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/proxytypes.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/__pycache__/proxytypes.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Feb 18 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.1.0-alt1
- Initial Build for Sisyphus.