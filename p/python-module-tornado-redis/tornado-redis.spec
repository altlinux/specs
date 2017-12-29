%define oname tornado-redis

%def_with python3

Name: python-module-%oname
Version: 2.4.18
Release: alt2.git20141002
Summary: Asynchronous Redis client that works within Tornado IO loop
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/tornado-redis/

# https://github.com/leporo/tornado-redis.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-tornado
%endif

%py_provides tornadoredis

%description
Asynchronous Redis client for the Tornado Web Server.

This is a fork of brukva redis client modified to be used via Tornado's
native 'tornado.gen' interface instead of 'adisp' call dispatcher.

%if_with python3
%package -n python3-module-%oname
Summary: Asynchronous Redis client that works within Tornado IO loop
Group: Development/Python3
%py3_provides tornadoredis

%description -n python3-module-%oname
Asynchronous Redis client for the Tornado Web Server.

This is a fork of brukva redis client modified to be used via Tornado's
native 'tornado.gen' interface instead of 'adisp' call dispatcher.
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
python setup.py build_ext -i
python runtests.py
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
python3 runtests.py
popd
%endif

%files
%doc *.md demos
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md demos
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.18-alt2.git20141002
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.18-alt1.git20141002.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.18-alt1.git20141002
- Initial build for Sisyphus

