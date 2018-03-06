%define _unpackaged_files_terminate_build 1
%define oname zope.i18nmessageid

%def_with check

Name: python-module-%oname
Version: 4.1.0
Release: alt1%ubt

Summary: Message Identifiers for internationalization
License: ZPLv2.1
Group: Development/Python
# Source-git https://github.com/zopefoundation/zope.i18nmessageid.git
Url: http://pypi.python.org/pypi/zope.i18nmessageid

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-dev
BuildRequires: python3-dev
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
%endif

%description
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

%package -n python3-module-%oname
Summary: Message Identifiers for internationalization (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

%package -n python3-module-%oname-tests
Summary: Tests for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
export PYTHONPATH=src
python setup.py test -v

pushd ../python3
python3 setup.py test -v
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/i18nmessageid/tests.*

%files tests
%python_sitelibdir/zope/i18nmessageid/tests.*

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/i18nmessageid/tests.*
%exclude %python3_sitelibdir/zope/i18nmessageid/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/i18nmessageid/tests.*
%python3_sitelibdir/zope/i18nmessageid/*/tests.*

%changelog
* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1%ubt
- 4.0.4 -> 4.1.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150309.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150309
- Version 4.0.4.dev0
- Added documentation
- Enabled check

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-3.3

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

