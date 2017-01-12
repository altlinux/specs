%define _unpackaged_files_terminate_build 1
%define oname gevent-websocket

%def_with python3

Name: python-module-%oname
Version: 0.9.5
Release: alt1
Summary: Websocket handler for the gevent pywsgi server, a Python network library
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/gevent-websocket/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/Jeffrey/gevent-websocket
Source0: https://pypi.python.org/packages/de/93/6bc86ddd65435a56a2f2ea7cc908d92fea894fc08e364156656e71cc1435/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires gevent greenlet

%description
gevent-websocket is a websocket library for the gevent networking
library.

%if_with python3
%package -n python3-module-%oname
Summary: Websocket handler for the gevent pywsgi server, a Python 3 network library
Group: Development/Python3
%py3_provides %oname
%py3_requires gevent greenlet

%description -n python3-module-%oname
gevent-websocket is a websocket library for the gevent networking
library.
%endif

%prep
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc LICENSE README.rst AUTHORS
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst AUTHORS
%python3_sitelibdir/*
%endif

%changelog
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

