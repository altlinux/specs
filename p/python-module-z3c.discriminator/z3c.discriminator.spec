%define oname z3c.discriminator
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: Provides a formalism for marking adapter specifications as discriminators
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.discriminator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

%package tests
Summary: Tests for z3c.discriminator
Group: Development/Python
Requires: %name = %version-%release

%description tests
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

This package contains tests for z3c.discriminator.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

