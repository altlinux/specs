%define oname pamqp

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.6.0
Release: alt1.git20141212.1.1
Summary: RabbitMQ Focused AMQP low-level library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pamqp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gmr/pamqp.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-lxml
#BuildPreReq: python-module-mock pylint python-tools-pep8
#BuildPreReq: python-module-coverage python-module-coveralls
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-lxml
#BuildPreReq: python3-module-mock pylint-py3 python3-tools-pep8
#BuildPreReq: python3-module-coverage python3-module-coveralls
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-egenix-mx-base python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-kerberos python-module-logilab-common python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-logilab-common python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-sh python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3
BuildRequires: pylint pylint-py3 python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pbr python-module-pytest python-module-unittest2 python-module-z4r-coveralls python-tools-pep8 python3-module-html5lib python3-module-nose python3-module-pbr python3-module-unittest2 python3-module-z4r-coveralls python3-tools-pep8 rpm-build-python3 time

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.git20141212.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.git20141212.1
- NMU: Use buildreq for BR.

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141212
- Version 1.6.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141105
- Version 1.5.0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140505
- Initial build for Sisyphus

