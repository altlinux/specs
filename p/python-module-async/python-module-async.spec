%define oname async

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.2
Release: alt1.1

Summary: Async Framework

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/GitPython/

Source: %name-%version.tar
BuildArch: noarch

%setup_python_module %oname

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest python3-module-nose python3-module-pytest rpm-build-python3 time

%description
Async is a framework to process interdependent tasks in a pool of
workers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Async is a framework to process interdependent tasks in a pool of
workers.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Async is a framework to process interdependent tasks in a pool of
workers.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Async is a framework to process interdependent tasks in a pool of
workers.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Async Framework
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Async is a framework to process interdependent tasks in a pool of
workers.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Async is a framework to process interdependent tasks in a pool of
workers.

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

%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.md
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- initial build for ALTLinux Sisyphus

