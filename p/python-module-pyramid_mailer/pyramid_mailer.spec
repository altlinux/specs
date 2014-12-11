%define oname pyramid_mailer

%def_with python3

Name: python-module-%oname
Version: 0.14
Release: alt1
Summary: Sendmail package for Pyramid
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_mailer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid repoze.sendmail lamson

%description
pyramid_mailer is a package for taking the pain out of sending emails in
your Pyramid project.

%package -n python3-module-%oname
Summary: Sendmail package for Pyramid
Group: Development/Python3
%py3_requires pyramid repoze.sendmail lamson

%description -n python3-module-%oname
pyramid_mailer is a package for taking the pain out of sending emails in
your Pyramid project.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_mailer
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires nose

%description -n python3-module-%oname-tests
pyramid_mailer is a package for taking the pain out of sending emails in
your Pyramid project.

This package contains tests for pyramid_mailer.

%package tests
Summary: Tests for pyramid_mailer
Group: Development/Python
Requires: %name = %version-%release
%py_requires nose

%description tests
pyramid_mailer is a package for taking the pain out of sending emails in
your Pyramid project.

This package contains tests for pyramid_mailer.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Version 0.14

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt2
- Added module for Python 3

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Version 0.11

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

