%define oname ioloop

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2.a.git20141215.1
Summary: Simple IOloop by epoll or kqueue
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/ioloop/

# https://github.com/mengzhuo/ioloop.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Simple IOloop by epoll or kqueue.

%if_with python3
%package -n python3-module-%oname
Summary: Simple IOloop by epoll or kqueue
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Simple IOloop by epoll or kqueue.
%endif

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
2to3 -w -n test.py
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt2.a.git20141215.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2.a.git20141215
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.a.git20141215.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.a.git20141215
- Initial build for Sisyphus

