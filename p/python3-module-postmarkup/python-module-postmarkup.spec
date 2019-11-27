%define oname postmarkup

Name: python3-module-%oname
Version: 1.2.0
Release: alt3

Summary: Generates XHTML snippets from BBCode
License: BSD
Group: Development/Python3
Url: http://code.google.com/p/postmarkup
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Generates XHTML snippets from BBCode.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt2.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt2.1
- Rebuilt with python 2.6

* Sun Feb 01 2009 Denis Klimov <zver@altlinux.org> 1.1.4-alt2
- more improve using setup_python_module macros
- use optimize and record options for install
- add BuildArch: noarch

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 1.1.4-alt1
- Initial build for ALT Linux

