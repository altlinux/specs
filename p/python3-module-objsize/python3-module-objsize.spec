%define _unpackaged_files_terminate_build 1
%define pypi_name objsize
%define mod_name objsize

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: Traversal over Python's objects subtree and calculate the total size of the subtree in bytes (deep size)
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/objsize/
Vcs: https://github.com/liran-funaro/objsize

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter bumpver
%add_pyproject_deps_check_filter pip-tools
%pyproject_builddeps_metadata_extra dev
%endif

%description
The objsize Python package allows for the exploration and measurement
of an object's complete memory usage in bytes, including its child
objects. This process, often referred to as deep size calculation, is
achieved through Python's internal Garbage Collection (GC) mechanism.

The objsize package is designed to ignore shared objects, such as None,
types, modules, classes, functions, and lambdas, because they are
shared across many instances. One of the key performance features of
objsize is that it avoids recursive calls, ensuring a faster and safer
execution.

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Mar 19 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Tue Apr 29 2025 Anton Zhukharev <ancieg@altlinux.org> 0.7.1-alt1
- Packaged for ALT Sisyphus.
