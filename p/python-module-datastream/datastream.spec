%define oname datastream

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20150108
Summary: Datastream API provides a powerful and unified Python API for time-series data
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/datastream/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wlanslovenija/datastream.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mongoengine python-module-pymongo
BuildPreReq: python-module-pytz
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mongoengine python3-module-pymongo
BuildPreReq: python3-module-pytz
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires mongoengine pymongo pytz

%description
Datastream API is one of the projects of wlan slovenija open wireless
network. It is a Python API for time-series data which abstracts the
database which is used to store the data, providing a powerful and
unified API. It provides an easy way to insert time-series datapoints
and automatically downsample them into multiple levels of granularity
for efficient querying time-series data at various time scales.

%package -n python3-module-%oname
Summary: Datastream API provides a powerful and unified Python API for time-series data
Group: Development/Python3
%py3_provides %oname
%py3_requires mongoengine pymongo pytz

%description -n python3-module-%oname
Datastream API is one of the projects of wlan slovenija open wireless
network. It is a Python API for time-series data which abstracts the
database which is used to store the data, providing a powerful and
unified API. It provides an easy way to insert time-series datapoints
and automatically downsample them into multiple levels of granularity
for efficient querying time-series data at various time scales.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Datastream API is one of the projects of wlan slovenija open wireless
network. It is a Python API for time-series data which abstracts the
database which is used to store the data, providing a powerful and
unified API. It provides an easy way to insert time-series datapoints
and automatically downsample them into multiple levels of granularity
for efficient querying time-series data at various time scales.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Datastream API is one of the projects of wlan slovenija open wireless
network. It is a Python API for time-series data which abstracts the
database which is used to store the data, providing a powerful and
unified API. It provides an easy way to insert time-series datapoints
and automatically downsample them into multiple levels of granularity
for efficient querying time-series data at various time scales.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150108
- Initial build for Sisyphus

