%define oname twilio

%def_with python3

Name: python-module-%oname
Version: 3.6.15
Release: alt1.git20150212
Summary: Twilio API client and TwiML generator
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/twilio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/twilio/twilio-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-httplib2 python-module-six
BuildPreReq: python-module-pysocks python-module-nose
BuildPreReq: python-module-coverage python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-httplib2 python3-module-six
BuildPreReq: python3-module-pysocks python3-module-nose
BuildPreReq: python3-module-coverage python3-module-mock
%endif

%py_provides %oname
%py_requires httplib2 six socks

%description
The Twilio REST SDK simplifies the process of making calls using the
Twilio REST API.
The Twilio REST API lets to you initiate outgoing calls, list previous
calls, and much more.

%package -n python3-module-%oname
Summary: Twilio API client and TwiML generator
Group: Development/Python3
%py3_provides %oname
%py3_requires httplib2 six socks

%description -n python3-module-%oname
The Twilio REST SDK simplifies the process of making calls using the
Twilio REST API.
The Twilio REST API lets to you initiate outgoing calls, list previous
calls, and much more.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The Twilio REST SDK simplifies the process of making calls using the
Twilio REST API.
The Twilio REST API lets to you initiate outgoing calls, list previous
calls, and much more.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The Twilio REST SDK simplifies the process of making calls using the
Twilio REST API.
The Twilio REST API lets to you initiate outgoing calls, list previous
calls, and much more.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
nosetests -v --with-coverage --cover-package=twilio
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v --with-coverage --cover-package=twilio
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.15-alt1.git20150212
- Initial build for Sisyphus

