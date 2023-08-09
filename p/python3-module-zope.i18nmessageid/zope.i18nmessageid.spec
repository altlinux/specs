%define _unpackaged_files_terminate_build 1

%define pypi_name zope.i18nmessageid
%define ns_name zope
%define mod_name i18nmessageid

%define descr \
This package provides facilities for *declaring* messages within \
program source text;  translation of the messages is the responsiblity \
of the 'zope.i18n' package.

%def_with check

Name: python3-module-%pypi_name
Version: 6.0.1
Release: alt1
Summary: Message Identifiers for internationalization
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.i18nmessageid/
Vcs: https://github.com/zopefoundation/zope.i18nmessageid
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
%endif

%description
%descr

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
%descr

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
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version-nspkg.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*
# strip devel files
%exclude %python3_sitelibdir/%ns_name/%mod_name/*.c

%files tests
%python3_sitelibdir/%ns_name/%mod_name/tests.py
%python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*

%changelog
* Fri Aug 04 2023 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 5.0.1 -> 6.0.1.
- Modernized packaging.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.0.1-alt3.1
- NMU: mapped PyPI name to distro's one.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt3
- Bootstrap for python3.10.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt2
- Drop specsubst scheme.

* Tue Apr 28 2020 Stanislav Levin <slev@altlinux.org> 5.0.1-alt1
- 5.0.0 -> 5.0.1.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Build new version.
- Fix license.

* Fri Dec 28 2018 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt1
- Build new version.

* Mon May 14 2018 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1.S1
- 4.0.4 -> 4.1.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150309.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150309
- Version 4.0.4.dev0
- Added documentation
- Enabled check

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt4
- Added necessary requirements
- Excluded *.pth

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt3
- Added %%py_provides zope.i18nmessageid

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Don't build python-module-zope.arch

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

