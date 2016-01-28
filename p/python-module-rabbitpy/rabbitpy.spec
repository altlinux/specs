%define oname rabbitpy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.23.0
Release: alt1.git20141105.1
Summary: A pure python, thread-safe, minimalistic and pythonic RabbitMQ client library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rabbitpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gmr/rabbitpy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pamqp python-module-nose
#BuildPreReq: python-module-mock python-module-coverage
#BuildPreReq: python-module-coveralls
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pamqp python3-module-nose
#BuildPreReq: python3-module-mock python3-module-coverage
#BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-sh python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pamqp python-module-pbr python-module-pytest python-module-unittest2 python-module-z4r-coveralls python3-module-html5lib python3-module-nose python3-module-pbr python3-module-pytest python3-module-unittest2 python3-module-z4r-coveralls rpm-build-python3 time

%description
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

%package -n python3-module-%oname
Summary: A pure python, thread-safe, minimalistic and pythonic RabbitMQ client library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

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
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.23.0-alt1.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1.git20141105
- Version 0.23.0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21.1-alt1.git20141030
- Initial build for Sisyphus

