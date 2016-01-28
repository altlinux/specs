%define oname rpyc

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.3.0
Release: alt1.git20141023.1
Summary: Remote Python Call (RPyC), a transparent and symmetric RPC library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/rpyc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tomerfiliba/rpyc.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-plumbum
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-plumbum
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-plumbum python-module-pytest python3-module-nose python3-module-pytest rpm-build-python3 time

%description
RPyC (pronounced like are-pie-see), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls, clustering,
and distributed-computing. RPyC makes use of object-proxying, a
technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can
be manipulated as if they were local.

%package -n python3-module-%oname
Summary: Remote Python Call (RPyC), a transparent and symmetric RPC library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
RPyC (pronounced like are-pie-see), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls, clustering,
and distributed-computing. RPyC makes use of object-proxying, a
technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can
be manipulated as if they were local.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
RPyC (pronounced like are-pie-see), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls, clustering,
and distributed-computing. RPyC makes use of object-proxying, a
technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can
be manipulated as if they were local.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
RPyC (pronounced like are-pie-see), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls, clustering,
and distributed-computing. RPyC makes use of object-proxying, a
technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can
be manipulated as if they were local.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
python setup.py test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html demos

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/* 
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.3.0-alt1.git20141023.1
- NMU: Use buildreq for BR.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.git20141023
- Initial build for Sisyphus

