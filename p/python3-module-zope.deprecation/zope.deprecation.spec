%define pypi_name zope.deprecation

%def_with check

Name: python3-module-%pypi_name
Epoch: 1
Version: 5.0
Release: alt2

Summary: Zope Deprecation Infrastructure
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.deprecation/
Vcs: https://github.com/zopefoundation/zope.deprecation.git

Source: %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%py3_requires zope

%description
This package provides a simple function called deprecated(names, reason)
to mark deprecated modules, classes, functions, methods and properties.

%package tests
Summary: Tests for Zope 3 Deprecation Infrastructure (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing
%add_python3_req_skip deprecation

%description tests
This package provides a simple function called deprecated(names, reason)
to mark deprecated modules, classes, functions, methods and properties.

This package contains tests for Zope Deprecation Infrastructure.

%prep
%setup

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
%doc *.txt
%python3_sitelibdir/zope/deprecation/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/__pycache__/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/__pycache__/tests.*

%changelog
* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 1:5.0-alt2
- Mapped PyPI name to distro's one.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 1:5.0-alt1
- New version 5.0.

* Fri Jul 02 2021 Vitaly Lipatov <lav@altlinux.ru> 1:4.4.0-alt3
- NMU: fix build

* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 1:4.4.0-alt2
- NMU: Remove python2 module build
- Add unittests execution

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.4.0-alt1
- Version updated to 4.4.0

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1
- NMU: Use buildreq for BR.

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.3-alt1.dev0.git20150113
- Version 4.1.3.dev0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.1-alt1
- Version 4.1.1

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.2.2-alt1
- Version 4.0.2

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Version 3.5.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Version 3.5.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Enable tests

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus
