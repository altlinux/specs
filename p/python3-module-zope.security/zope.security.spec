%define _unpackaged_files_terminate_build 1
%define pypi_name zope.security
%define ns_name zope
%define mod_name security

%def_with check

Name: python3-module-%pypi_name
Version: 7.0
Release: alt1
Summary: Zope Security Framework
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.security/
Vcs: https://github.com/zopefoundation/zope.security
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# setuptools(pkg_resources) is used by namespace root that is packaged
# separately at python3-module-zope
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
# zope/proxy/proxy.h
BuildRequires: python3-module-zope.proxy-devel
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-module-zope.component-tests
%endif

%description
The Security framework provides a generic mechanism to implement
security policies on Python objects.

%package tests
Summary: Tests for Zope Security Framework
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains tests for Zope Security Framework.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src

%files
%doc *.txt
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/examples/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/
%exclude %python3_sitelibdir/%ns_name/%mod_name/testing.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/testing.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/*.c

%files tests
%python3_sitelibdir/%ns_name/%mod_name/tests/
%python3_sitelibdir/%ns_name/%mod_name/testing.py
%python3_sitelibdir/%ns_name/%mod_name/__pycache__/testing.*

%changelog
* Thu May 30 2024 Stanislav Levin <slev@altlinux.org> 7.0-alt1
- 6.2 -> 7.0.

* Fri Mar 15 2024 Stanislav Levin <slev@altlinux.org> 6.2-alt1
- 6.1 -> 6.2.

* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 6.1-alt2
- Mapped PyPI name to distro's one.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 6.1-alt1
- 5.1.1 -> 6.1.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 5.1.1-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt2
- Bootstrap for python3.9.

* Wed Apr 01 2020 Nikolai Kostrigin <nickel@altlinux.org> 5.1.1-alt1
- 5.1.0 -> 5.1.1
- Reenable check and docs sections; switch back to uniform def_with macro
- Rearrange check section according to upstream changes

* Fri Mar 06 2020 Anton Farygin <rider@altlinux.ru> 5.1.0-alt2
- temporary  disabled check and docs sections to avoid cyclic dependencies
  on zope.component when building python-3.8

* Wed Mar 04 2020 Nikolai Kostrigin <nickel@altlinux.org> 5.1.0-alt1
- 5.0 -> 5.1.0
- Fix license

* Mon Dec 23 2019 Nikolai Kostrigin <nickel@altlinux.org> 5.0-alt1
- NMU: 4.0.4 -> 5.0
- Remove python2 module build
- Cleanup excessive commented BRs
- Add unittests execution

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.4-alt1.dev0.git20150602.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150602.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150602.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150602.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150602
- Version 4.0.4.dev0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2.dev.git20140319
- Python 3: moved examples into separate package

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev.git20140319
- Version 4.0.2dev
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git20130709
- Version 4.0.1dev

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3.b2.dev0.git20130327
- Version 4.0.0b2.dev0

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.bzr20120517
- Added necessary .zcml files (ALT #28301)

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.bzr20120517
- Version 4.0.0dev

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Version 3.8.3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

