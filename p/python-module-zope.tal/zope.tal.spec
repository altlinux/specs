%define oname zope.tal

%def_with python3

Name: python-module-%oname
Version: 4.2.0
Release: alt2
Summary: Zope 3 Template Application Languate (TAL)
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.tal/

# https://github.com/zopefoundation/zope.tal.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-fix-test-for-unicode-for-python3.patch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner
BuildPreReq: python-module-zope.i18nmessageid
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.testing
BuildPreReq: python3-module-zope.testrunner
BuildPreReq: python3-module-zope.i18nmessageid
BuildPreReq: python-tools-2to3
%endif

%py_requires zope zope.i18nmessageid zope.interface

%description
The Zope3 Template Attribute Languate (TAL) specifies the custom
namespace and attributes which are used by the Zope Page Templates
renderer to inject dynamic markup into a page. It also includes the
Macro Expansion for TAL (METAL) macro language used in page assembly.

The dynamic values themselves are specified using a companion language,
TALES (see the 'zope.tales' package for more).

%if_with python3
%package -n python3-module-%oname
Summary: Zope 3 Template Application Languate (TAL) (Python 3)
Group: Development/Python3
%py3_requires zope zope.i18nmessageid zope.interface

%description -n python3-module-%oname
The Zope3 Template Attribute Languate (TAL) specifies the custom
namespace and attributes which are used by the Zope Page Templates
renderer to inject dynamic markup into a page. It also includes the
Macro Expansion for TAL (METAL) macro language used in page assembly.

The dynamic values themselves are specified using a companion language,
TALES (see the 'zope.tales' package for more).

%package -n python3-module-%oname-tests
Summary: Tests for Zope 3 Template Application Languate (TAL) (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The Zope3 Template Attribute Languate (TAL) specifies the custom
namespace and attributes which are used by the Zope Page Templates
renderer to inject dynamic markup into a page. It also includes the
Macro Expansion for TAL (METAL) macro language used in page assembly.

The dynamic values themselves are specified using a companion language,
TALES (see the 'zope.tales' package for more).

This package contains tests for Zope 3 Template Application Languate.
%endif

%package tests
Summary: Tests for Zope 3 Template Application Languate (TAL)
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The Zope3 Template Attribute Languate (TAL) specifies the custom
namespace and attributes which are used by the Zope Page Templates
renderer to inject dynamic markup into a page. It also includes the
Macro Expansion for TAL (METAL) macro language used in page assembly.

The dynamic values themselves are specified using a companion language,
TALES (see the 'zope.tales' package for more).

This package contains tests for Zope 3 Template Application Languate.

%prep
%setup
%patch1 -p1
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
sed -i 's|.*def setSourceFile\(.*\)|    def setSourceFile\1|' \
	src/zope/tal/interfaces.py
sed -i 's|.*def setGlobal\(.*\)|    def setGlobal\1|' \
	src/zope/tal/interfaces.py

%python3_build
popd
%endif

%install
%python_install
%if "%_lib" == "lib64"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%_lib" == "lib64"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/runtest.*

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/runtest.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/runtest.*
%exclude %python3_sitelibdir/*/*/*/runtest.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/runtest.*
%python3_sitelibdir/*/*/*/runtest.*
%endif

%changelog
* Thu Feb 08 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.0-alt2
- fix lib/lib64 stupidity

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt1
- Updated to upstream version 4.2.0.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.2-alt1.dev0.git10150605.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev0.git10150605
- Version 4.1.2.dev0

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git10141229
- Version 4.1.1.dev0

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git10140113
- Version 4.0.1dev

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt1.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Version 3.6.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added necesssary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

