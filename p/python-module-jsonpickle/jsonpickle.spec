%define oname jsonpickle

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt1.git20150116
Summary: Python library for serializing any arbitrary object graph into JSON
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonpickle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/jsonpickle/jsonpickle.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-feedparser python-modules-json
BuildPreReq: python-module-demjson python-module-jsonlib
BuildPreReq: python-module-yajl python-module-ujson
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-sphinx-devel python-module-sphinxtogithub
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-demjson python3-module-jsonlib
BuildPreReq: python3-module-yajl python3-module-ujson
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname
%py_requires json demjson jsonlib yajl ujson

%description
jsonpickle converts complex Python objects to and from JSON.

%package -n python3-module-%oname
Summary: Python library for serializing any arbitrary object graph into JSON
Group: Development/Python3
%py3_provides %oname
%py3_requires demjson jsonlib yajl ujson

%description -n python3-module-%oname
jsonpickle converts complex Python objects to and from JSON.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
jsonpickle converts complex Python objects to and from JSON.

This package contains pickles for %oname.

%package docs
Summary: documentaiton for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
jsonpickle converts complex Python objects to and from JSON.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|feedparser|speedparser|g' ../python3/tests/*.py
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

%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.rst contrib
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst contrib
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150116
- Version 0.9.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141022
- Initial build for Sisyphus

