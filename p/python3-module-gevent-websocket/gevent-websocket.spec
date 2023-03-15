%define _unpackaged_files_terminate_build 1
%define oname gevent-websocket

Name: python3-module-%oname
Version: 0.10.1
Release: alt1
Summary: Websocket handler for the gevent pywsgi server, a Python network library
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/gevent-websocket/

Source0: https://files.pythonhosted.org/packages/98/d2/6fa19239ff1ab072af40ebf339acd91fb97f34617c2ee625b8e34bf42393/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
gevent-websocket is a websocket library for the gevent networking
library.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.rst AUTHORS
%python3_sitelibdir/*

%changelog
* Thu Mar 02 2023 Anton Vyatkin <toni@altlinux.org> 0.10.1-alt1
- new version 0.10.1

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.5-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.3-alt1.hg20140424.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.3-alt1.hg20140424.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.hg20140424
- Version 0.9.3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.hg20131128
- Version 0.9.0

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.alpha0.hg20130417
- Version 0.4.0-alpha0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt2.hg20120723
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.3.6-alt1.hg20120723.1
- Rebuild with Python-3.3

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.hg20120723
- New snapshot

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.hg20120423
- Version 0.3.6
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus

