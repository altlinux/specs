%define _unpackaged_files_terminate_build 1
%define pypi_name uncalled-for
%define mod_name uncalled_for

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: Async dependency injection for Python functions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/uncalled-for/
Vcs: https://github.com/chrisguidry/uncalled-for

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

# 'codespell' is provided by 'codespell' package, not 'python3-module-codespell'
%pyproject_configure_with_check_filter codespell
%pyproject_configure_with_check_filter loq
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0
%if_with check
BuildRequires: codespell
%endif

%description
Async dependency injection for Python functions.

Declare what your function needs as parameter defaults. They show up resolved
when the function runs. No ceremony, no container, no configuration.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 09 2026 Anton Zhukharev <ancieg@altlinux.org> 0.6.0-alt1
- Updated to 0.6.0.

* Wed Aug 19 2026 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- Packaged for ALT Sisyphus.
