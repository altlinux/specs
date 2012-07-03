%define oname pyramid_mailer
Name: python-module-%oname
Version: 0.5.1
Release: alt1
Summary: Sendmail package for Pyramid
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_mailer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid repoze.sendmail lamson

%description
pyramid_mailer is a package for taking the pain out of sending emails in
your Pyramid project.

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

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

