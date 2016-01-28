%define oname zope.app.appsetup

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt2.a1.1
Summary: Zope app setup helper
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.appsetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.testrunner python-module-eggtestinfo
#BuildPreReq: python-module-zope.interface python-module-zope.exceptions
#BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.testrunner python3-module-eggtestinfo
#BuildPreReq: python3-module-zope.interface python3-module-zope.exceptions
#BuildPreReq: python3-module-six
%endif

%py_requires zope.app.publication zope.component zope.configuration
%py_requires zope.container zope.error zope.event zope.interface
%py_requires zope.processlifetime zope.security zope.session zope.site
%py_requires zope.traversing ZODB3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-numpy python-module-pbr python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-unittest2 python-module-zope.exceptions python-module-zope.interface python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-unittest2 python3-module-zope python3-module-zope.exceptions python3-module-zope.interface python3-module-zope.testing
BuildRequires: python-module-eggtestinfo python-module-zope.testrunner python3-module-eggtestinfo python3-module-html5lib python3-module-pytest python3-module-zope.testrunner rpm-build-python3

%description
This package provides application setup helpers for the Zope3 appserver.

%package -n python3-module-%oname
Summary: Zope app setup helper
Group: Development/Python3
%py3_requires zope.app.publication zope.component zope.configuration
%py3_requires zope.container zope.error zope.event zope.interface
%py3_requires zope.processlifetime zope.security zope.session zope.site
%py3_requires zope.traversing ZODB3

%description -n python3-module-%oname
This package provides application setup helpers for the Zope3 appserver.

%package -n python3-module-%oname-tests
Summary: Tests for Zope app setup helper
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.componentvocabulary zope.principalregistry
%py3_requires zope.testing zope.testrunner

%description -n python3-module-%oname-tests
This package provides application setup helpers for the Zope3 appserver.

This package contains tests for Zope app setup helper.

%package tests
Summary: Tests for Zope app setup helper
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.componentvocabulary zope.principalregistry
%py_requires zope.testing zope.testrunner

%description tests
This package provides application setup helpers for the Zope3 appserver.

This package contains tests for Zope app setup helper.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
mv %buildroot%_bindir/debug %buildroot%_bindir/debug.py3
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif
mv %buildroot%_bindir/debug %buildroot%_bindir/debug.app

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt2.a1.1
- NMU: Use buildreq for BR.

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt4
- Renamed %_bindir/debug -> %_bindir/debug.app (ALT #28797)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.16.0-alt3.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt2
- Excluded .pth file

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt1
- Initial build for Sisyphus

