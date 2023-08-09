%define _unpackaged_files_terminate_build 1
%define pypi_name zope.publisher
%define ns_name zope
%define mod_name publisher

%def_with check

Name: python3-module-%pypi_name
Version: 6.1.0
Release: alt1
Epoch: 1
Summary: The Zope publisher publishes Python objects on the web
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.publisher/
Vcs: https://github.com/zopefoundation/zope.publisher
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# this projects depends on pkg_resources that is subpackaged in ALTLinux
%add_pyproject_deps_runtime_filter setuptools
Requires: python3-module-pkg_resources
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-module-zope.security-tests
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.interface-tests
%endif

%description
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

%package tests
Summary: Tests for zope.publisher
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testrunner
%py3_requires zope.testing
Requires: python3-module-zope.security-tests
Requires: python3-module-zope.component-tests
Requires: python3-module-zope.interface-tests

%description tests
This package contains tests for %pypi_name.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/
%exclude %python3_sitelibdir/%ns_name/%mod_name/testing.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/testing.*

%files tests
%python3_sitelibdir/%ns_name/%mod_name/tests/
%python3_sitelibdir/%ns_name/%mod_name/testing.py
%python3_sitelibdir/%ns_name/%mod_name/__pycache__/testing.*

%changelog
* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 1:6.1.0-alt1
- 6.0.1 -> 6.1.0.

* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 1:6.0.1-alt1
- Automatically updated to 6.0.1.

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 1:5.1.1-alt1
- NMU: 4.3.2 -> 5.1.1
- Remove python2 module build
- Remove ubt tag from changelog
- Enable check
- Remove obsolete fix-tests patch

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.3.2-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Apr 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.3.2-alt3
- requires for tests fixed

* Thu Mar 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.3.2-alt2
- Tests fixed

* Mon Mar 05 2018 Stanislav Levin <slev@altlinux.org> 1:4.3.2-alt1
- 4.2.1 -> 4.3.2

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.2.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.2.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.2.1-alt1
- Version 4.2.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.0-alt1
- Version 4.1.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt2
- Version 4.0.0

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt1.a4
- Version 4.0.0a4 again

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt1
- Version 3.13.4

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a4
- Version 4.0.0a4

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt1
- Version 3.13.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.6-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt1
- Initial build for Sisyphus

