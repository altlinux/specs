%define oname ioloop

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.a.git20141215.1
Summary: Simple IOloop by epoll or kqueue
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ioloop/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mengzhuo/ioloop.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Simple IOloop by epoll or kqueue.

%package -n python3-module-%oname
Summary: Simple IOloop by epoll or kqueue
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Simple IOloop by epoll or kqueue.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
python test.py
%if_with python3
pushd ../python3
python3 setup.py test
2to3 -w -n test.py
python3 test.py
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.a.git20141215.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.a.git20141215
- Initial build for Sisyphus

