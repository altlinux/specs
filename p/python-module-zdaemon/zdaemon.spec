%define oname zdaemon

%def_with python3

Name: python-module-%oname
Version: 2.0.4
Release: alt2
Summary: Daemon process control library and tools for Unix-based systems
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zdaemon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
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
%py3_requires zope.testing

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
%py_requires zope.testing

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
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
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
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.4-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus

