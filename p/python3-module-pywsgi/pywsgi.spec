%define oname pywsgi

Name: python3-module-%oname
Version: 0.9.0
Release: alt3

Summary: A high-level class-based API around WSGI, CGI, and mod_python
License: GPLv2
Group: Development/Python3
Url: http://pypi.python.org/pypi/pywsgi/
BuildArch: noarch

Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
pywsgi provides the following features:

 - An abstraction from low-level gateway interface handlers like WSGI,
   CGI, and mod_python.
 - A consistent high-level, class-based interface.
 - Session handling.
 - Cookie handling.
 - GET/POST data handling.
 - Error handling.
 - A pywsgi.util namespace with useful tools.

%prep
%setup
%patch0 -p2

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt3
- python2 disabled
- porting on python3

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

