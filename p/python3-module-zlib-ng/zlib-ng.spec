Name: python3-module-zlib-ng
Version: 1.0.0
Release: alt1

Summary: Python bindings for the zlib-ng library
License: PSF-2.0
Group: Development/Python
Url: https://pypi.org/project/zlib-ng
VCS: https://github.com/pycompression/python-zlib-ng

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
BuildRequires: pkgconfig(zlib-ng)
BuildRequires: python3(test)
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
export PYTHON_ZLIB_NG_LINK_DYNAMIC=true
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/zlib_ng
%python3_sitelibdir/zlib_ng-%version.dist-info

%changelog
* Thu Dec 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0.0 released

* Wed Sep 10 2025 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt2
- Fixed build with python3.13.

* Fri Jul 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.3-alt1
- 0.4.3 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released
