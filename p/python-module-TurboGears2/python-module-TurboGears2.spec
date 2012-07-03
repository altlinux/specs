%define oname TurboGears2

%def_without python3

Name: python-module-%oname
Version: 2.0.4
Release: alt1

Summary: Back-to-front web development in Python

License: MIT/X11
Group: Development/Python
Url: http://www.turbogears.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildPreReq: python-module-distribute
BuildArch: noarch

%py_requires setuptools

%setup_python_module tg
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

Source: http://www.turbogears.org/2.0/downloads/%version/%oname-%version.tar

%description
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

%if_with python3
%package -n python3-module-%oname
Summary: Back-to-front web development in Python 3
Group: Development/Python3

%description -n python3-module-%oname
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

%package -n python3-module-%oname-tests
Summary: Tests for TurboGears (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

This package contains tests for TurboGears.
%endif

%package tests
Summary: Tests for TurboGears
Group: Development/Python
Requires: %name = %version-%release

%description tests
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

This package contains tests for TurboGears.

%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
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
%doc README.txt
%python_sitelibdir/tg/
%python_sitelibdir/%{oname}*.egg-info
%exclude %python_sitelibdir/tg/test_stack
%exclude %python_sitelibdir/tg/tests

%files tests
%python_sitelibdir/tg/test_stack
%python_sitelibdir/tg/tests

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tg/test_stack
%exclude %python3_sitelibdir/tg/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/tg/test_stack
%python3_sitelibdir/tg/tests
%endif

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt1.1.1
- Rebuild with Python-2.7

* Sat Aug 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.1
- Fixed build

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) import in git

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.1
- Rebuilt with python 2.6

* Sun Mar 29 2009 Denis Klimov <zver@altlinux.org> 1.0.8-alt1
- Initial build for ALT Linux

