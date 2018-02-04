%define oname pyga

%def_with python3

Name: python-module-%oname
Version: 2.5.0
Release: alt1.git20140809.1.1.1
Summary: Server side implemenation of Google Analytics in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyga/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kra3/py-ga-mob.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-mock
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-mock python-tools-2to3
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pbr python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-setuptools python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-unittest2 rpm-build-python3 time

%description
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

%package -n python3-module-%oname
Summary: Server side implemenation of Google Analytics in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%make -C doc pickle
mkdir -p build/docs
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst RELEASES
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst RELEASES
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.git20140809.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt1.git20140809.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.5.0-alt1.git20140809.1
- NMU: Use buildreq for BR.

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20140809
- Initial build for Sisyphus

