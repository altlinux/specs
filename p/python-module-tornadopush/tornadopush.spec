%define _unpackaged_files_terminate_build 1
%define oname tornadopush

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 0.8.1
Release: alt1
Summary: Push and presence server built with Tornado and Redis
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tornadopush/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/frascoweb/tornadopush.git
Source0: https://pypi.python.org/packages/86/49/4309fb756777f4bcabd2797abcb5335a3ba80850f232be3c99e79463cdee/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tornado python-module-redis-py
#BuildPreReq: python-module-itsdangerous python-module-yaml
#BuildPreReq: python-module-jsmin python-module-tornado-redis
#BuildPreReq: python-module-backports.ssl_match_hostname
#BuildPreReq: python-module-certifi python-module-toredis
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tornado python3-module-redis-py
#BuildPreReq: python3-module-itsdangerous python3-module-yaml
#BuildPreReq: python3-module-jsmin python3-module-tornado-redis
#BuildPreReq: python3-module-backports.ssl_match_hostname
#BuildPreReq: python3-module-certifi python3-module-toredis
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires itsdangerous yaml jsmin tornadoredis toredis

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pycares python-module-pycurl python-module-pytest python-module-setuptools python-module-tornado python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-pycares python3-module-pytest python3-module-setuptools python3-module-tornado python3-module-zope python3-module-zope.interface
BuildRequires: python-module-setuptools-tests python-module-toredis python-module-yaml python3-module-setuptools-tests python3-module-toredis python3-module-yaml rpm-build-python3 time

%description
Push and presence server built with Tornado and Redis.

%package -n python3-module-%oname
Summary: Push and presence server built with Tornado and Redis
Group: Development/Python3
%py3_provides %oname
%py3_requires itsdangerous yaml jsmin tornadoredis toredis

%description -n python3-module-%oname
Push and presence server built with Tornado and Redis.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt1.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20150808
- Version 0.7.2

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20150119
- Version 0.6.2

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150101
- Version 0.6.1

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20141225
- Version 0.6

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.8-alt1.git20141128
- Initial build for Sisyphus

