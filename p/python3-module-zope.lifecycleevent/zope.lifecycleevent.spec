%define _unpackaged_files_terminate_build 1
%define pypi_name zope.lifecycleevent
%define ns_name zope
%define mod_name lifecycleevent

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: Object life-cycle events
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.lifecycleevent
Vcs: https://github.com/zopefoundation/zope.lifecycleevent.git
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
# zope.component.testing is required but subpackaged
BuildRequires: python3-module-zope.component-tests
%endif

%description
This package defines a specific set of event objects and API functions for
describing the life-cycle of objects in the system: object creation, object
modification, and object removal.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -v

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*

%changelog
* Fri Mar 20 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt2
- Mapped PyPI name to the RPM one.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Feb 16 2025 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Thu Jul 06 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Tue Mar 21 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3-alt1
- NMU: 4.2.0 -> 4.3
- Remove python2 module build
- Remove ubt tags from changelog

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2
- NMU: remove ubt from release

* Fri Feb 16 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1
- 4.1.1 -> 4.2.0

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20141229.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20141229.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1.dev0.git20141229.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20141229
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 3.7.0-alt4.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

