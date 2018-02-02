# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20150203.1.1.1
%define mname greplin
%define oname scales

%def_with python3

Name: python-module-%oname
Version: 1.0.8
#Release: alt1.git20150203.1
Summary: Stats for Python processes
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/scales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Cue/scales.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-six python3-module-nose
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires six json

%description
Tracks server state and statistics, allowing you to see what your server
is doing. It can also send metrics to Graphite for graphing or to a file
for crash forensics.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Tracks server state and statistics, allowing you to see what your server
is doing. It can also send metrics to Graphite for graphing or to a file
for crash forensics.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Stats for Python processes
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires six

%description -n python3-module-%oname
Tracks server state and statistics, allowing you to see what your server
is doing. It can also send metrics to Graphite for graphing or to a file
for crash forensics.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Tracks server state and statistics, allowing you to see what your server
is doing. It can also send metrics to Graphite for graphing or to a file
for crash forensics.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 src/%mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/*/*/*test*

%files -n python-module-%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.8-alt1.git20150203.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt1.git20150203.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt1.git20150203.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20150203
- Initial build for Sisyphus

