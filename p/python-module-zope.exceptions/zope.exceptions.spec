%define _unpackaged_files_terminate_build 1
%define oname zope.exceptions

%def_with check

Name: python-module-%oname
Version: 4.2.0
Release: alt2%ubt

Summary: Zope Exceptions
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.exceptions.git
Url: http://pypi.python.org/pypi/zope.exceptions

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python-module-zope.interface
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-zope.interface

%if_with check
BuildRequires: python-module-zope.testrunner
BuildRequires: python3-module-zope.testrunner
%endif

%py_requires zope zope.interface

%description
This package contains exception interfaces and implementations which are
so general purpose that they don't belong in Zope application-specific
packages.

%package -n python3-module-%oname
Summary: Zope Exceptions (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package contains exception interfaces and implementations which are
so general purpose that they don't belong in Zope application-specific
packages.

%package -n python3-module-%oname-tests
Summary: Tests for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains exception interfaces and implementations which are
so general purpose that they don't belong in Zope application-specific
packages.

This package contains tests for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains exception interfaces and implementations which are
so general purpose that they don't belong in Zope application-specific
packages.

This package contains tests for %oname.

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
        %buildroot%python_sitelibdir/
%endif

pushd ../python3
%python3_install
popd

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
        %buildroot%python3_sitelibdir/
%endif

%check
python setup.py test -v

pushd ../python3
python3 setup.py test -v
popd

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%changelog
* Wed Feb 14 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt2%ubt
- Fix a wrong logic of packaging for non x86_64 arch

* Mon Feb 12 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1%ubt
- v4.0.8 -> v4.2.0

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.8-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.8-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.8-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Version 4.0.8

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt1
- Version 4.0.7

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1
- Version 4.0.6

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.7.1-alt1.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

