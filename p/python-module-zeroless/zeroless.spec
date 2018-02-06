%define oname zeroless

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20150102.1.1.1
Summary: A pythonic approach for distributed systems with ZeroMQ
License: LGPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/zeroless/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zmqless/zeroless.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zmq
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zmq
%endif

%py_provides %oname
%py_requires zmq

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-genshi python-module-greenlet python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-greenlet python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python-module-zmq python3-module-setuptools python3-module-zmq rpm-build-python3 time
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest

%description
Yet another ZeroMQ wrapper for Python. However, differing from pyzmq,
which tries to stay very close to the C++ implementation, this project
aims to make distributed systems employing 0MQ as pythonic as possible.

Being simpler to use, Zeroless doesn't supports all of the fine aspects
and features of 0MQ. However, you can expect to find all the message
passing patterns you were accustomed to (i.e. pair, request/reply,
publisher/subscriber, push/pull). Depite that, the only transport
available is TCP, as threads are not as efficient in Python due to the
GIL and IPC is unix-only.

%package -n python3-module-%oname
Summary: A pythonic approach for distributed systems with ZeroMQ
Group: Development/Python3
%py3_provides %oname
%py3_requires zmq

%description -n python3-module-%oname
Yet another ZeroMQ wrapper for Python. However, differing from pyzmq,
which tries to stay very close to the C++ implementation, this project
aims to make distributed systems employing 0MQ as pythonic as possible.

Being simpler to use, Zeroless doesn't supports all of the fine aspects
and features of 0MQ. However, you can expect to find all the message
passing patterns you were accustomed to (i.e. pair, request/reply,
publisher/subscriber, push/pull). Depite that, the only transport
available is TCP, as threads are not as efficient in Python due to the
GIL and IPC is unix-only.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Yet another ZeroMQ wrapper for Python. However, differing from pyzmq,
which tries to stay very close to the C++ implementation, this project
aims to make distributed systems employing 0MQ as pythonic as possible.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Yet another ZeroMQ wrapper for Python. However, differing from pyzmq,
which tries to stay very close to the C++ implementation, this project
aims to make distributed systems employing 0MQ as pythonic as possible.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150102.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150102.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20150102.1
- NMU: Use buildreq for BR.

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150102
- Initial build for Sisyphus

