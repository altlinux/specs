%define oname kafka

%def_with python3

Name: python-module-%oname
Version: 0.9.3
Release: alt1.dev.git20150102
Summary: Pure Python client for Apache Kafka
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/kafka-python/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mumrah/kafka-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tox python-module-mock
BuildPreReq: python-module-six python-module-snappy
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tox python3-module-mock
BuildPreReq: python3-module-six python3-module-snappy
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires six gzip snappy json

%description
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

%package -n python3-module-%oname
Summary: Pure Python client for Apache Kafka
Group: Development/Python3
%py3_provides %oname
%py3_requires six gzip snappy

%description -n python3-module-%oname
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

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
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.md example.py load_example.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md example.py load_example.py
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.dev.git20150102
- Initial build for Sisyphus

