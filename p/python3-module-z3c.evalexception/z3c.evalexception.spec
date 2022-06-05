%define oname z3c.evalexception

Name: python3-module-%oname
Version: 3.0
Release: alt1

Summary: Debugging middlewares for zope.publisher-based web applications

License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/z3c.evalexception

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%py3_requires paste zope.security

%description
z3c.evalexception provides two WSGI middlewares for debugging web
applications running on the zope.publisher object publishing framework
(e.g. Zope 3). Both middlewares will intercept an exception thrown by
the application and provide means for debugging.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.txt
%exclude %python3_sitelibdir/*.pth
%python3_sitelibdir/z3c/evalexception
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Sun Jun 05 2022 Grigory Ustinov <grenka@altlinux.org> 3.0-alt1
- Build new version.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt4
- python3 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

