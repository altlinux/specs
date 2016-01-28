%define oname jsonpickle

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt1.git20150116.1
Summary: Python library for serializing any arbitrary object graph into JSON
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonpickle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/jsonpickle/jsonpickle.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-feedparser python-modules-json
#BuildPreReq: python-module-demjson python-module-jsonlib
#BuildPreReq: python-module-yajl python-module-ujson
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-sphinx-devel python-module-sphinxtogithub
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-demjson python3-module-jsonlib
#BuildPreReq: python3-module-yajl python3-module-ujson
#BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname
%py_requires json demjson jsonlib yajl ujson

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cjson python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-coverage python-module-demjson python-module-docutils python-module-feedparser python-module-html5lib python-module-jsonlib python-module-nose python-module-objects.inv python-module-setuptools-tests python-module-sphinxtogithub python-module-ujson python-module-yajl python3-module-coverage python3-module-demjson python3-module-jsonlib python3-module-nose python3-module-setuptools-tests python3-module-ujson python3-module-yajl rpm-build-python3 time

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150116
- Version 0.9.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141022
- Initial build for Sisyphus

