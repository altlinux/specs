%define _unpackaged_files_terminate_build 1
%define pypi_name zope.schema

%def_with check

Name: python3-module-%pypi_name
Version: 7.0.1
Release: alt2

Summary: zope.interface extension for defining data schemas
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.schema/
Vcs: https://github.com/zopefoundation/zope.schema

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
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods). Every schema is an interface and specifies
the public fields of an object. A field roughly corresponds to an
attribute of a python object. But a Field provides space for at least a
title and a description. It can also constrain its value and provide a
validation method. Besides you can optionally specify characteristics
such as its value being read-only or not required.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods). Every schema is an interface and specifies
the public fields of an object. A field roughly corresponds to an
attribute of a python object. But a Field provides space for at least a
title and a description. It can also constrain its value and provide a
validation method. Besides you can optionally specify characteristics
such as its value being read-only or not required.

This package contains tests for %pypi_name

%prep
%setup
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
%python3_sitelibdir/zope/schema/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Mon Jul 31 2023 Stanislav Levin <slev@altlinux.org> 7.0.1-alt2
- Mapped PyPI name to distro's one.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 7.0.1-alt1
- New version 7.0.1.

* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.9.3-alt2
- Build for python2 disabled.

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.9.3-alt1
- Version updated to 4.4.3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.3-alt1.dev0.git20150128.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.3-alt1.dev0.git20150128.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.3-alt1.dev0.git20150128.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.3-alt1.dev0.git20150128.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt1.dev0.git20150128
- Version 4.4.3.dev0
- Added documentation
- Enabled check

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1
- Version 4.3.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.1-alt1.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.0-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Initial build for Sisyphus

