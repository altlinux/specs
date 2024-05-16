%define _unpackaged_files_terminate_build 1
%define pypi_name zope.interface
%define ns_name zope
%define mod_name interface

%def_with check

Name: python3-module-%pypi_name
Version: 6.4
Release: alt1

Summary: Zope interfaces package
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.interface/
Vcs: https://github.com/zopefoundation/zope.interface
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
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-module-zope.testrunner
%endif

%description
This is a separate distribution of the %pypi_name package used in
Zope 3, along with the packages it depends on.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.event

%description tests
This package contains tests for %pypi_name.

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
# per .github/workflows/tests.yml
# ``python -m unittest discover`` only works with editable
# installs, so we have to duplicate some work and can't
# install the built wheel. (zope.testrunner
# works fine with non-editable installs.)
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version-nspkg.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/
%exclude %python3_sitelibdir/%ns_name/%mod_name/common/tests/
%exclude %python3_sitelibdir/%ns_name/%mod_name/*.c

%files tests
%python3_sitelibdir/%ns_name/%mod_name/tests/
%python3_sitelibdir/%ns_name/%mod_name/common/tests/

%changelog
* Thu May 16 2024 Stanislav Levin <slev@altlinux.org> 6.4-alt1
- 6.3 -> 6.4.

* Mon Apr 15 2024 Stanislav Levin <slev@altlinux.org> 6.3-alt1
- 6.2 -> 6.3.

* Thu Mar 14 2024 Stanislav Levin <slev@altlinux.org> 6.2-alt1
- 6.0 -> 6.2.

* Fri Aug 04 2023 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.4.0 -> 6.0.
- Modernized packaging.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.4.0-alt2.1
- NMU: mapped PyPI name to distro's one.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 5.4.0-alt2
- Bootstrap for python3.10.

* Sun Apr 25 2021 Grigory Ustinov <grenka@altlinux.org> 5.4.0-alt1
- Automatically updated to 5.4.0.
- Build with check.
- Drop python2 support.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt3
- Bootstrap for python3.9.

* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 5.1.0-alt2
- Disabled testing against Python2.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Tue Mar 17 2020 Grigory Ustinov <grenka@altlinux.org> 4.7.2-alt1
- Automatically updated to 4.7.2.
- Build with check.

* Thu Jan 16 2020 Grigory Ustinov <grenka@altlinux.org> 4.7.1-alt2
- Bootstrap for python3.8.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 4.7.1-alt1
- Build new version 4.7.1.
- Fix license.

* Fri Apr 19 2019 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1
- Build new version without bootstrap.

* Wed Apr 03 2019 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1.qa1.1
- Bootstrap for python3.7.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Stanislav Levin <slev@altlinux.org> 4.5.0-alt1
- 4.3.3 -> 4.5.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.3.3-alt1
- automated PyPI update

* Tue Mar 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.3-alt1.dev0.git20150601.4
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 22 2016 Denis Medvedev <nbr@altlinux.org> 4.1.3-alt1.dev0.git20150601.3
- Fix deps for python 3.5

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.3-alt1.dev0.git20150601.2
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.3-alt1.dev0.git20150601.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1.dev0.git20150601
- New snapshot

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1.dev0.git20141227
- Version 4.1.3.dev0

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev.git20140319
- Version 4.1.2dev
- Added docs

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Moved all tests into tests subpackage

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Sat Mar 16 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.5-alt1
- Version 4.0.5

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt2
- Don't pack zope*egg-info

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Version 3.6.2

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Set as archdep package

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Rebuilt with python 2.6

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.2
- Fixed file conflict with python-module-zope

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.1
- Fixed file conflict with python-module-zope (ALT #21981)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.3.0-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Mon Nov 20 2006 Ivan Fedorov <ns@altlinux.ru> 3.1.0-alt1.c1
- 3.1.0c1

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 3.0.1-alt1
- Initial build for ALT Linux.
