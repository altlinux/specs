%define _unpackaged_files_terminate_build 1
%define pypi_name pygit2

%def_with check

Name: python3-module-%pypi_name
Version: 1.13.3
Release: alt1

Summary: Python bindings for libgit2
License: GPL-2.0 with linking exception
Group: Development/Python3
Url: https://pypi.org/project/pygit2/
Vcs: https://github.com/libgit2/pygit2

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libgit2-devel
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Bindings to the libgit2 shared library, implements Git plumbing.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra test -k 'not (test_filter or test_buffered_filter)'

%files
%doc COPYING AUTHORS.rst CHANGELOG.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 15 2023 Anton Zhukharev <ancieg@altlinux.org> 1.13.3-alt1
- Built for ALT Sisyphus.

