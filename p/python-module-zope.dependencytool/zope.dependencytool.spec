%define oname zope.dependencytool

%def_with python3

Name: python-module-%oname
Version: 3.4.0
Release: alt3.1
Summary: Package-Dependency Discovery Tool
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.dependencytool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope

%description
This package installs a script that allows a developer to discover the
used packages of a given package. This is useful when creating a list of
dependencies for setup.py.

%package -n python3-module-%oname
Summary: Package-Dependency Discovery Tool
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package installs a script that allows a developer to discover the
used packages of a given package. This is useful when creating a list of
dependencies for setup.py.

%package -n python3-module-%oname-tests
Summary: Tests for Package-Dependency Discovery Tool
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package installs a script that allows a developer to discover the
used packages of a given package. This is useful when creating a list of
dependencies for setup.py.

This package contains tests for Package-Dependency Discovery Tool.

%package tests
Summary: Tests for Package-Dependency Discovery Tool
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package installs a script that allows a developer to discover the
used packages of a given package. This is useful when creating a list of
dependencies for setup.py.

This package contains tests for Package-Dependency Discovery Tool.

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
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

