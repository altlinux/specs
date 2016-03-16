%define oname z3c.etree

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt3.1
Summary: Integrating any ElementTree engine with the Zope component architecture
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.etree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
z3c.etree provides some mechanisms (a common interface) for integrating
any ElementTree engine with the Zope component architecture. This allows
applications to look up a engine against this interface. As such this
package does not implement the ElementTree API.

z3c.etree also provides a set of utilities that can be used to make
testing XML output in doctests easier. This functionality can also be
called from a python based unit test via the assertXMLEqual method.

%package -n python3-module-%oname
Summary: Integrating any ElementTree engine with the Zope component architecture
Group: Development/Python3

%description -n python3-module-%oname
z3c.etree provides some mechanisms (a common interface) for integrating
any ElementTree engine with the Zope component architecture. This allows
applications to look up a engine against this interface. As such this
package does not implement the ElementTree API.

z3c.etree also provides a set of utilities that can be used to make
testing XML output in doctests easier. This functionality can also be
called from a python based unit test via the assertXMLEqual method.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.etree
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.component elementtree cElementTree lxml

%description -n python3-module-%oname-tests
z3c.etree provides some mechanisms (a common interface) for integrating
any ElementTree engine with the Zope component architecture. This allows
applications to look up a engine against this interface. As such this
package does not implement the ElementTree API.

z3c.etree also provides a set of utilities that can be used to make
testing XML output in doctests easier. This functionality can also be
called from a python based unit test via the assertXMLEqual method.

This package contains tests for z3c.etree.

%package tests
Summary: Tests for z3c.etree
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component elementtree cElementTree lxml

%description tests
z3c.etree provides some mechanisms (a common interface) for integrating
any ElementTree engine with the Zope component architecture. This allows
applications to look up a engine against this interface. As such this
package does not implement the ElementTree API.

z3c.etree also provides a set of utilities that can be used to make
testing XML output in doctests easier. This functionality can also be
called from a python based unit test via the assertXMLEqual method.

This package contains tests for z3c.etree.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/*/test*
#python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus

