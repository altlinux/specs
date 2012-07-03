%define oname zope.i18nmessageid

%def_with python3

Name: python-module-%oname
Version: 3.6.1
Release: alt2
Summary: Message Identifiers for internationalization
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.i18nmessageid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-zope
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-zope python-tools-2to3
%endif

%py_provides zope.i18nmessageid

%py_requires zope

%description
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

%if_with python3
%package -n python3-module-%oname
Summary: Message Identifiers for internationalization (Python 3)
Group: Development/Python3
%py3_provides zope.i18nmessageid
%py3_requires zope

%description -n python3-module-%oname
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

%package -n python3-module-%oname-tests
Summary: Tests for zope.i18nmessageid (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

This package contains tests for zope.i18nmessageid
%endif

%package tests
Summary: Tests for zope.i18nmessageid
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

This package contains tests for zope.i18nmessageid

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
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

