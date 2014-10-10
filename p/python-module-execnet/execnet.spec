%define oname execnet

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt1
Summary: execnet: rapid multi-Python deployment
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/execnet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%add_python_req_skip win32event win32evtlogutil win32service
%add_python_req_skip win32serviceutil register

%description
execnet provides carefully tested means to ad-hoc interact with Python
interpreters across version, platform and network barriers. It provides
a minimal and fast API targetting the following uses:

* distribute tasks to local or remote processes
* write and deploy hybrid multi-process applications
* write scripts to administer multiple hosts

%package -n python3-module-%oname
Summary: execnet: rapid multi-Python deployment
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip win32event win32evtlogutil win32service
%add_python3_req_skip win32serviceutil rlcompleter2 register

%description -n python3-module-%oname
execnet provides carefully tested means to ad-hoc interact with Python
interpreters across version, platform and network barriers. It provides
a minimal and fast API targetting the following uses:

* distribute tasks to local or remote processes
* write and deploy hybrid multi-process applications
* write scripts to administer multiple hosts

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
execnet provides carefully tested means to ad-hoc interact with Python
interpreters across version, platform and network barriers. It provides
a minimal and fast API targetting the following uses:

* distribute tasks to local or remote processes
* write and deploy hybrid multi-process applications
* write scripts to administer multiple hosts

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
execnet provides carefully tested means to ad-hoc interact with Python
interpreters across version, platform and network barriers. It provides
a minimal and fast API targetting the following uses:

* distribute tasks to local or remote processes
* write and deploy hybrid multi-process applications
* write scripts to administer multiple hosts

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGELOG *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

