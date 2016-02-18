%define oname flask-pymongo

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20131201.1
Summary: PyMongo support for Flask applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-PyMongo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dcrosta/flask-pymongo.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-flask python-module-pymongo
#BuildPreReq: python-module-nose python-module-pymongo-gridfs
#BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-flask python3-module-pymongo
#BuildPreReq: python3-module-nose python3-module-gridfs
#BuildPreReq: python3-module-coverage
%endif

%py_provides flask_pymongo

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-jinja2 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-jinja2 python3-module-setuptools
BuildRequires: python-module-coverage python-module-nose python-module-pytest python3-module-coverage python3-module-nose python3-module-pytest rpm-build-python3

%description
PyMongo support for Flask applications.

%package -n python3-module-%oname
Summary: PyMongo support for Flask applications
Group: Development/Python3
%py3_provides flask_pymongo

%description -n python3-module-%oname
PyMongo support for Flask applications.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc *.md docs/*.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20131201.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20131201
- Initial build for Sisyphus

