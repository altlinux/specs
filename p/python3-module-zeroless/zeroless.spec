%define oname zeroless

Name: python3-module-%oname
Version: 0.3.0
Release: alt2

Summary: A pythonic approach for distributed systems with ZeroMQ
License: LGPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/zeroless/
# https://github.com/zmqless/zeroless.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildRequires: python3-module-sphinx

%py3_provides %oname
%py3_requires zmq

BuildRequires: python3-module-zmq python3-module-pytest


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

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150102.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150102.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20150102.1
- NMU: Use buildreq for BR.

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150102
- Initial build for Sisyphus

