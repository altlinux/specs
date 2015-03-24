%define oname ripozo

%def_with python3

Name: python-module-%oname
Version: 0.1.20
Release: alt1.dev0.git20150324
Summary: An tool for easily making RESTful interfaces
License: UNKNOWN
Group: Development/Python
Url: https://pypi.python.org/pypi/ripozo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vertical-knowledge/ripozo.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-jinja2
BuildPreReq: python-module-tox python-module-mock
BuildPreReq: python-module-ripozo-tests python-module-coverage
BuildPreReq: python-module-virtualenv
BuildPreReq: python-modules-json python-modules-logging
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-jinja2
BuildPreReq: python3-module-tox python3-module-mock
BuildPreReq: python3-module-ripozo-tests python3-module-coverage
BuildPreReq: python3-module-virtualenv
%endif

%py_provides %oname
%py_requires six jinja2 json logging

%description
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

%if_with python3
%package -n python3-module-%oname
Summary: An tool for easily making RESTful interfaces
Group: Development/Python3
%py3_provides %oname
%py3_requires six jinja2 json logging

%description -n python3-module-%oname
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=%buildroot%python_sitelibdir
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
* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20-alt1.dev0.git20150324
- Initial build for Sisyphus

