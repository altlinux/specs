%define oname zope.deferredimport

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt1
Summary: Allows you to perform imports names that will be resolved when used in the code
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.deferredimport/
Vcs: https://github.com/zopefoundation/zope.deferredimport.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-zope.proxy
BuildRequires: python3-module-zope.testrunner
%endif

%py3_requires zope zope.proxy

%description
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

This package contains tests for %oname.

%package examples
Summary: Example files for %oname
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description examples
Example files for %oname.

%prep
%setup
mv src/zope/deferredimport/samples ./

%build
%pyproject_build

%install
%pyproject_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

install -d %buildroot%_docdir/%name
cp -fR samples %buildroot%_docdir/%name

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc CHANGES.rst README.rst
%python3_sitelibdir/zope/deferredimport/
%python3_sitelibdir/%oname-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files examples
%doc %_docdir/%name/samples

%changelog
* Thu Jun 29 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.1-alt1
- NMU: 4.3 -> 4.3.1
- Remove python2 module build
- Rearrange unittests execution

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.3-alt1
- Version updated to 4.3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools
- Move samples to examples subpackage

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150402
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

