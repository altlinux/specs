%define oname smmap

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt1.git20150107.1.1.1

Summary:  Sliding window memory map manager

License: BSD
Group: Development/Python
Url: git://github.com/Byron/smmap.git

Source: %name-%version.tar

%setup_python_module %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-nose python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-nose python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nosexcover python-module-objects.inv python-module-setuptools python3-module-coverage python3-module-nosexcover python3-module-setuptools rpm-build-python3 time

#BuildRequires: python-devel python-module-setuptools
#BuildPreReq: python-module-nose python-module-nosexcover
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose python3-module-nosexcover
#BuildPreReq: python3-module-coverage
%endif

BuildArch: noarch

%description
A pure python implementation of a sliding window memory map manager

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A pure python implementation of a sliding window memory map manager

This package contains tests for %oname.

%package -n python3-module-%oname
Summary:  Sliding window memory map manager
Group: Development/Python3

%description -n python3-module-%oname
A pure python implementation of a sliding window memory map manager

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A pure python implementation of a sliding window memory map manager

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONOPATH=%buildroot%python_sitelibdir
%make -C doc html

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.md doc/build/html
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/test
%python_sitelibdir/*.egg-info

%files tests
%python_sitelibdir/%modulename/test

%if_with python3
%files -n python3-module-%oname
%doc README.md doc/build/html
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/test
%python3_sitelibdir/*.egg-info

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1.git20150107.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150107.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150107.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150107
- Version 0.9.0

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141113
- Version 0.8.3

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140714
- New snapshot
- Added module for Python 3

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- initial
