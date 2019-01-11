%define _unpackaged_files_terminate_build 1

%define oname zdaemon

%def_with python3

Name: python-module-%oname
Version: 4.3
Release: alt1
Summary: Daemon process control library and tools for Unix-based systems
License: ZPL
Group: Development/Python
BuildArch: noarch
Url: http://pypi.python.org/pypi/zdaemon/

# https://github.com/zopefoundation/zdaemon.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-zconfig
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zc.customdoctests python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-zconfig
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zc.customdoctests python3-module-mock
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
Requires: python3-module-%oname = %EVR
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
Requires: %name = %EVR
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
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in * ; do
	mv $i ${i}.py3
done
popd
%endif

%python_install

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%_bindir/zdaemon
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%_bindir/zdaemon.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Thu Jan 10 2019 Grigory Ustinov <grenka@altlinux.org> 4.3-alt1
- new version 4.3

* Thu Jun 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt1
- Updated to upstream version 4.2.0.

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

