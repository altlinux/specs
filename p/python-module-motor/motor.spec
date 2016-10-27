%define oname motor

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.7
Release: alt1.git20161010
Summary: Non-blocking MongoDB driver for Tornado
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/motor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mongodb/motor.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tornado
BuildPreReq: python-module-pymongo python-module-pymongo-gridfs
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-futures
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tornado
BuildPreReq: python3-module-pymongo python3-module-gridfs
%endif

%py_provides %oname
%py_requires tornado pymongo gridfs

%description
Motor is a full-featured, non-blocking MongoDB driver for Python Tornado
applications.

%package -n python3-module-%oname
Summary: Non-blocking MongoDB driver for Tornado
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado pymongo gridfs

%description -n python3-module-%oname
Motor is a full-featured, non-blocking MongoDB driver for Python Tornado
applications.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Motor is a full-featured, non-blocking MongoDB driver for Python Tornado
applications.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc html

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

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 27 2016 Vladimir Didenko <cow@altlinux.org> 0.7-alt1.git20161010
- New version (closes: #31269)

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140705
- Initial build for Sisyphus
