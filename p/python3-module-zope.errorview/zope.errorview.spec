%define _unpackaged_files_terminate_build 1
%define pypi_name zope.errorview
%define ns_name zope
%define mod_name errorview

%def_with check

Name: python3-module-%pypi_name
Version: 3.0
Release: alt1
Summary: Basic HTTP and Browser exception views
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.errorview
Vcs: https://github.com/zopefoundation/zope.errorview
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
# zope.component.eventtesting is required but subpackaged
BuildRequires: python3-module-zope.component-tests
%endif

%description
Provides basic HTTP and Browser views for common exceptions.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Wed Mar 18 2026 Stanislav Levin <slev@altlinux.org> 3.0-alt1
- 2.1 -> 3.0.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 2.1-alt1
- 2.0 -> 2.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 2.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Tue Mar 21 2023 Anton Vyatkin <toni@altlinux.org> 2.0-alt1
- New version 2.0.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt1
- version updated to 1.2.0
- python2 disabled

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt3
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.11-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt2.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Version 0.11

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Initial build for Sisyphus

