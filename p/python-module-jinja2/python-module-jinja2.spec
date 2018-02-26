%define oname jinja2

%def_with python3

Name: python-module-%oname
Version: 2.7
Release: alt1.git20120313

Summary: The new and improved version of a small but fast template engine
License: BSD
Group: Development/Python
Url: http://jinja.pocoo.org/2/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/jinja2.git
Source0: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
# for docs
BuildPreReq: python-module-sphinx python-module-Pygments
BuildPreReq: python-module-jinja2-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

Requires: %name-tests = %version-%release

%description
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%if_with python3
%package -n python3-module-%oname
Summary: The new and improved version of a small but fast template engine (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%package -n python3-module-%oname-tests
Summary: Tests for Jinja2 (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains tests for Jinja2.
%endif

%package tests
Summary: Tests for Jinja2
Group: Development/Python
Requires: %name = %version-%release

%description tests
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains tests for Jinja2.

%package doc
Summary: Documentation for Jinja2
Group: Development/Documentation

%description doc
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains HTML documentation for Jinja2.

%package pickles
Summary: Pickles for Jinja2
Group: Development/Python

%description pickles
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains pickles for Jinja2.


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

%make_build -C docs html
%make_build -C docs pickle

%install
%python_install
# IronPython support
rm -f %buildroot%python_sitelibdir/jinja2/_ipysupport.py

%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/jinja2/_ipysupport.py
%endif

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/jinja2/

%check
make test

%files
%python_sitelibdir/jinja2/
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/jinja2/tests.py*
%exclude %python_sitelibdir/jinja2/testsuite
%exclude %python_sitelibdir/jinja2/pickle
%doc AUTHORS CHANGES
%doc ext/

%files tests
%python_sitelibdir/jinja2/tests.py*
%python_sitelibdir/jinja2/testsuite

%files doc
%doc docs/_build/html/*

%files pickles
%dir %python_sitelibdir/jinja2
%python_sitelibdir/jinja2/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES
%python3_sitelibdir/jinja2/
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/jinja2/tests.py*
%exclude %python3_sitelibdir/jinja2/testsuite

%files -n python3-module-%oname-tests
%python3_sitelibdir/jinja2/tests.py*
%python3_sitelibdir/jinja2/testsuite
%endif

%changelog
* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20120313
- New snapshot
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20111215
- Version 2.7

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt2
- Enabled docs

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.5-alt1.1
- Rebuild with Python-2.7 (bootstraping without docs)

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt1
- Version 2.5.5

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Added requirement on tests package

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5
- Extracted tests into separate package
- Added pickles

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.2
- Enable building of documentation

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Rebuilt with python 2.6 (bootstrap)

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.1-alt1
- 2.2.1
- enable building of documentation
- build as noarch

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.1.1-alt1
- initial build
