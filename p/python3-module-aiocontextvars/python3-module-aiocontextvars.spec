%define _unpackaged_files_terminate_build 1
%define pypi_name aiocontextvars

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.2
Release: alt1

Summary: Asyncio support for PEP-567 contextvars backport
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/aiocontextvars/
Vcs: https://github.com/fantix/aiocontextvars

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: aiocontextvars-0.2.2-alt-setup.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter bumpversion
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements_dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst HISTORY.rst AUTHORS.rst
%python3_sitelibdir/*

%changelog
* Sun May 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.2-alt1
- Initial build for ALT Sisyphus.

