%define oname TurboGears2

Name: python3-module-%oname
Version: 2.4.2
Release: alt1

Summary: Back-to-front web development in Python

License: MIT
Group: Development/Python
Url: http://www.turbogears.org

#BuildPreReq: python-module-distribute
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools rpm-build-python3 time

Source: %name-%version.tar

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

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
* Wed Dec 04 2019 Anton Farygin <rider@altlinux.ru> 2.4.2-alt1
- 2.4.2
- disabled python2 version

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.3-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.3.3-alt1.1
- NMU: Use buildreq for BR.

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1
- Version 2.3.3
- Added module for Python 3

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Version 2.2.0

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

