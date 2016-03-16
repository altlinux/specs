%define oname robotframework-elasticsearch

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.git20150114.1
Summary: ElasticSearch library for Robot Framework
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-elasticsearch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pagesjaunes/robotframework-elasticsearch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-modules-json
BuildPreReq: python-module-robotframework
BuildPreReq: python-module-elasticsearch
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests
BuildPreReq: python3-module-robotframework
BuildPreReq: python3-module-elasticsearch
BuildPreReq: python-tools-2to3
%endif

%py_provides ElasticSearchLib
%py_requires robotframework elasticsearch

%description
This lib provides basic keywords to interact with elasticsearch in a
RobotFramework testsuite. It allows to query, count, create or delete an
index.

%if_with python3
%package -n python3-module-%oname
Summary: ElasticSearch library for Robot Framework
Group: Development/Python3
%py3_provides ElasticSearchLib
%py3_requires robotframework elasticsearch

%description -n python3-module-%oname
This lib provides basic keywords to interact with elasticsearch in a
RobotFramework testsuite. It allows to query, count, create or delete an
index.
%endif

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md doc/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md doc/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150114
- Version 1.1
- Added module for Python 3

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141223
- Initial build for Sisyphus

