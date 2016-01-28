%define oname zope.lifecycleevent

%def_with python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1.dev0.git20141229.1
Summary: Object life-cycle events
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.lifecycleevent/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zope.event python-module-zope.component-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-ZEO python-module-ZODB python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-serial python-module-setuptools python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc.lockfile python-module-zdaemon python-module-zope python-module-zope.component python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.interface python-module-zope.proxy python-module-zope.testing python-module-zope.testrunner python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-unittest2 python3-module-zope python3-module-zope.component python3-module-zope.configuration python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.schema python3-module-zope.testing python3-module-zope.testrunner
BuildRequires: python-module-pytest python-module-zope.component-tests python3-module-html5lib python3-module-pytest python3-module-zope.component-tests rpm-build-python3

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.event python3-module-zope.component-tests
%endif

%py_requires zope.interface zope.component zope.event

%description
In Zope, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

%if_with python3
%package -n python3-module-%oname
Summary: Object life-cycle events (Python 3)
Group: Development/Python3
%py3_requires zope.interface zope.component zope.event

%description -n python3-module-%oname
In Zope, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

%package -n python3-module-%oname-tests
Summary: Tests for zope.lifecycleevent (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.component zope.container

%description -n python3-module-%oname-tests
In Zope, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

This package contains tests for zope.lifecycleevent.
%endif

%package tests
Summary: Tests for zope.lifecycleevent
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component zope.container

%description tests
In Zope, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

This package contains tests for zope.lifecycleevent.

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

%check
export PYTHONPATH=$PWD/src
python src/zope/lifecycleevent/tests.py -v
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD/src
python3 src/zope/lifecycleevent/tests.py -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1.dev0.git20141229.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20141229
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 3.7.0-alt4.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

