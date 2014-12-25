%define oname pamqp

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.6.0
Release: alt1.git20141212
Summary: RabbitMQ Focused AMQP low-level library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pamqp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gmr/pamqp.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-lxml
BuildPreReq: python-module-mock pylint python-tools-pep8
BuildPreReq: python-module-coverage python-module-coveralls
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-lxml
BuildPreReq: python3-module-mock pylint-py3 python3-tools-pep8
BuildPreReq: python3-module-coverage python3-module-coveralls
%endif

%py_provides %oname

%description
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

%package -n python3-module-%oname
Summary: RabbitMQ Focused AMQP low-level library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

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
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141212
- Version 1.6.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141105
- Version 1.5.0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140505
- Initial build for Sisyphus

