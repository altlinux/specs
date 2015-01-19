%define oname tornadopush

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.2
Release: alt1.git20150119
Summary: Push and presence server built with Tornado and Redis
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tornadopush/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/frascoweb/tornadopush.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tornado python-module-redis-py
BuildPreReq: python-module-itsdangerous python-module-yaml
BuildPreReq: python-module-jsmin python-module-tornado-redis
BuildPreReq: python-module-backports.ssl_match_hostname
BuildPreReq: python-module-certifi python-module-toredis
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tornado python3-module-redis-py
BuildPreReq: python3-module-itsdangerous python3-module-yaml
BuildPreReq: python3-module-jsmin python3-module-tornado-redis
BuildPreReq: python3-module-backports.ssl_match_hostname
BuildPreReq: python3-module-certifi python3-module-toredis
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Push and presence server built with Tornado and Redis.

%package -n python3-module-%oname
Summary: Push and presence server built with Tornado and Redis
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Push and presence server built with Tornado and Redis.

%prep
%setup

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
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20150119
- Version 0.6.2

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150101
- Version 0.6.1

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20141225
- Version 0.6

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.8-alt1.git20141128
- Initial build for Sisyphus

