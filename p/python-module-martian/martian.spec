%define oname martian

%def_with python3

Name: python-module-%oname
Version: 0.14
Release: alt3.1
Summary: A library to grok configuration from Python code
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/martian/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.interface

%description
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

%package -n python3-module-%oname
Summary: A library to grok configuration from Python code
Group: Development/Python3
%py3_requires zope.interface

%description -n python3-module-%oname
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

%package -n python3-module-%oname-tests
Summary: Tests for martian
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing setuptools.tests

%description -n python3-module-%oname-tests
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

This package contains tests for martian.

%package tests
Summary: Tests for martian
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing setuptools.tests

%description tests
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

This package contains tests for martian.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.14-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt2
- Added necessary requirements

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Initial build for Sisyphus

