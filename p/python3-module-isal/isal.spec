Name: python3-module-isal
Version: 1.8.0
Release: alt1

Summary: Python bindings for the ISA-L library
License: PSF-2.0
Group: Development/Python
Url: https://pypi.org/project/isal
VCS: https://github.com/pycompression/python-isal

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
BuildRequires: libisal-devel python3-test
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_tox tox.ini testenv

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PYTHON_ISAL_LINK_DYNAMIC=1
%pyproject_build

%install
%pyproject_install

%check
%ifarch aarch64 x86_64
%pyproject_run_pytest -o addopts= tests
%endif

%files
%python3_sitelibdir/isal
%python3_sitelibdir/isal-%version.dist-info

%changelog
* Mon Oct 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.0-alt1
- 1.8.0 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.1-alt1
- 1.7.1 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.0-alt1
- 1.7.0 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.1-alt1
- 1.6.1 released
