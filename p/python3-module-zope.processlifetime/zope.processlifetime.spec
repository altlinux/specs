%define _unpackaged_files_terminate_build 1
%define pypi_name zope.processlifetime
%define ns_name zope
%define mod_name processlifetime

%def_with check

Name: python3-module-%pypi_name
Version: 4.0
Release: alt1
Summary: Zope process lifetime events
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.processlifetime/
Vcs: https://github.com/zopefoundation/zope.processlifetime
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
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
%pyproject_builddeps_check
%endif

%description
This package provides interfaces / implementations for events relative
to the lifetime of a server process (startup, database opening, etc.)

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*

%changelog
* Fri Mar 20 2026 Stanislav Levin <slev@altlinux.org> 4.0-alt1
- 3.1 -> 4.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 3.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Feb 16 2025 Anton Vyatkin <toni@altlinux.org> 3.1-alt1
- New version 3.1.

* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- New version 3.0.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Add necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

