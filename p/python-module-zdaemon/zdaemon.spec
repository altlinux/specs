%define oname zdaemon

%def_with python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1.dev0.git20150416.1.1.1
Summary: Daemon process control library and tools for Unix-based systems
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zdaemon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zdaemon.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zconfig python-module-zope.testing
#BuildPreReq: python-module-zope.testrunner python-module-manuel
#BuildPreReq: python-module-zc.customdoctests python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-extras python-module-funcsigs python-module-linecache2 python-module-manuel python-module-manuel-tests python-module-mimeparse python-module-numpy python-module-pbr python-module-pyasn1 python-module-pytest python-module-serial python-module-setuptools python-module-six python-module-subunit python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zc python-module-zope python-module-zope.exceptions python-module-zope.interface python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-unittest2 python3-module-zope python3-module-zope.exceptions python3-module-zope.interface python3-module-zope.testing
BuildRequires: python-module-mock python-module-setuptools python-module-zc.customdoctests python-module-zconfig python-module-zope.testrunner python3-module-html5lib python3-module-pytest python3-module-zc.customdoctests python3-module-zope.testrunner rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
#BuildPreReq: python3-module-zconfig python3-module-zope.testing
#BuildPreReq: python3-module-zope.testrunner python3-module-manuel
#BuildPreReq: python3-module-zc.customdoctests python3-module-mock
%endif

%description
zdaemon is a Python package which provides APIs for managing
applications run as daemons. Its principal use to date has been to
manage the application server and storage server daemons for Zope / ZEO,
although it is not limited to running Python-based applications (for
instance, it has been used to manage the 'spread' daemon).

%if_with python3
%package -n python3-module-%oname
Summary: Daemon process control library and tools for Unix-based systems (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
zdaemon is a Python package which provides APIs for managing
applications run as daemons. Its principal use to date has been to
manage the application server and storage server daemons for Zope / ZEO,
although it is not limited to running Python-based applications (for
instance, it has been used to manage the 'spread' daemon).

%package -n python3-module-%oname-tests
Summary: Tests for zdaemon (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.testrunner zc.customdoctests

%description -n python3-module-%oname-tests
zdaemon is a Python package which provides APIs for managing
applications run as daemons. Its principal use to date has been to
manage the application server and storage server daemons for Zope / ZEO,
although it is not limited to running Python-based applications (for
instance, it has been used to manage the 'spread' daemon).

This package contains tests for zdaemon.
%endif

%package tests
Summary: Tests for zdaemon
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.testrunner zc.customdoctests

%description tests
zdaemon is a Python package which provides APIs for managing
applications run as daemons. Its principal use to date has been to
manage the application server and storage server daemons for Zope / ZEO,
although it is not limited to running Python-based applications (for
instance, it has been used to manage the 'spread' daemon).

This package contains tests for zdaemon.

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
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/zdaemon %buildroot%_bindir/zdaemon3
%endif

%python_install

%check
python setup.py test

%files
%doc *.txt
%_bindir/zdaemon
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
# broken now
#_bindir/zdaemon3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150416.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150416.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1.dev0.git20150416.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150416
- Version 4.1.1.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git20140809
- Version 4.0.1dev
- Enabled testing

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0.4-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.4-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus

