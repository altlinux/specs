%define oname watchdog

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.8.3
Release: alt1.git20150211
Summary: Filesystem events monitoring
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/watchdog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gorakhargosh/watchdog.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel python-module-pathtools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pathtools
%endif

%py_provides %oname
%py_requires pathtools
%add_python_req_skip AppKit FSEvents _watchdog_fsevents argh

%description
Python API and shell utilities to monitor file system events.

%package -n python3-module-%oname
Summary: Filesystem events monitoring
Group: Development/Python3
%py3_provides %oname
%py3_requires pathtools
%add_python3_req_skip AppKit FSEvents _watchdog_fsevents argh

%description -n python3-module-%oname
Python API and shell utilities to monitor file system events.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Python API and shell utilities to monitor file system events.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python API and shell utilities to monitor file system events.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150211
- Version 0.8.3

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141031
- Version 0.8.2

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140916
- Initial build for Sisyphus

