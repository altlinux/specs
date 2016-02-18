%define oname gitdb

%def_with python3
%def_disable check

Name: python-module-GitDB
Version: 0.6.4
Release: alt1.git20150112.1

Summary: IO of git-style object databases

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/gitdb/

# https://github.com/gitpython-developers/gitdb.git
Source: %name-%version.tar

%setup_python_module gitdb

#BuildPreReq: python-devel python-module-setuptools-tests git
#BuildPreReq: python-module-smmap python-module-nose
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-smmap python3-module-nose
#BuildPreReq: python3-module-coverage
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: git-core python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-smmap python3-devel rpm-build-python3 time

%description
IO of git-style object databases.

%package -n python3-module-%oname
Summary: IO of git-style object databases
Group: Development/Python3
%py3_provides %oname
Provides: python3-module-GitDB = %EVR

%description -n python3-module-%oname
IO of git-style object databases.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
IO of git-style object databases.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
IO of git-style object databases.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing
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
rm -f %buildroot%python3_sitelibdir/%oname/_perf.*.so
popd
%endif

%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
%make coverage
%if_with python3
pushd ../python3
%make coverage PYTHON=python3 TESTRUNNER=nosetests3
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.git20150112
- Version 0.6.4

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141114
- Version 0.6.0
- Added module for Python 3

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALTLinux Sisyphus

