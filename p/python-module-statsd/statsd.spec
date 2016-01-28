%define oname statsd

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.0.1
Release: alt1.git20141105.1
Summary: A simple statsd client
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/statsd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jsocol/pystatsd.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-mock
#BuildPreReq: python-module-flake8
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-mock
#BuildPreReq: python3-module-flake8
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mccabe python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-docutils python-module-flake8 python-module-html5lib python-module-nose python-module-objects.inv python-module-pbr python-module-pytest python-module-unittest2 python3-module-flake8 python3-module-html5lib python3-module-nose python3-module-pbr python3-module-unittest2 rpm-build-python3 time

%description
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: A simple statsd client
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

This package contains pickles for %oname.

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
%doc AUTHORS CHANGES *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.1-alt1.git20141105.1
- NMU: Use buildreq for BR.

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20141105
- Initial build for Sisyphus

