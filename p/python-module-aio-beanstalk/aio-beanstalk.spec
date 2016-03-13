%define oname aio-beanstalk

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20141204.1.1
Summary: The asyncio client for beanstalkd work queue
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aio-beanstalk/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tailhook/aio-beanstalk.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-modules-json
#BuildPreReq: python-module-yaml
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
#BuildPreReq: python3-module-yaml
%endif

%py_provides aiobeanstalk
%py_requires asyncio json yaml

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python3-module-asyncio python3-module-pytest python3-module-yaml rpm-build-python3 time

%description
Asyncio-based client for beanstalkd task server.

%package -n python3-module-%oname
Summary: The asyncio client for beanstalkd work queue
Group: Development/Python3
%py3_provides aiobeanstalk
%py3_requires asyncio json yaml

%description -n python3-module-%oname
Asyncio-based client for beanstalkd task server.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
touch aiobeanstalk/__init__.py
%python_build_debug
%endif

%if_with python3
pushd ../python3
touch aiobeanstalk/__init__.py
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
py.test aiobeanstalk/*.py -vv
%endif
%if_with python3
pushd ../python3
py.test-%_python3_version aiobeanstalk/*.py -vv
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141204.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20141204.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141204
- Initial build for Sisyphus

