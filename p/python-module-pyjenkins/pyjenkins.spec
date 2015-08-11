%define oname jenkins

%def_with python3

Name: python-module-py%oname
Version: 0.4.8
Release: alt1.git20150810
Summary: Python bindings for the remote Jenkins API
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-jenkins/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.openstack.org/stackforge/python-jenkins
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-pbr python-module-six
BuildPreReq: python-module-coverage python-module-discover
BuildPreReq: python-module-hacking python-module-mock
BuildPreReq: python-module-unittest2 python-module-subunit-tests
BuildPreReq: python-module-testrepository
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests git
BuildPreReq: python3-module-pbr python3-module-six
BuildPreReq: python3-module-coverage python3-module-discover
BuildPreReq: python3-module-hacking python3-module-mock
BuildPreReq: python3-module-unittest2 python3-module-subunit-tests
BuildPreReq: python3-module-testrepository
BuildPreReq: python3-module-sphinx
%endif

%py_provides %oname py%oname
%py_requires pbr six
Conflicts: python-module-%oname

%description
Python Jenkins is a python wrapper for the Jenkins REST API which aims
to provide a more conventionally pythonic way of controlling a Jenkins
server. It provides a higher-level API containing a number of
convenience functions.

%if_with python3
%package -n python3-module-py%oname
Summary: Python bindings for the remote Jenkins API
Group: Development/Python3
%py3_provides %oname py%oname
%py3_requires pbr six
Conflicts: python3-module-%oname

%description -n python3-module-py%oname
Python Jenkins is a python wrapper for the Jenkins REST API which aims
to provide a more conventionally pythonic way of controlling a Jenkins
server. It provides a higher-level API containing a number of
convenience functions.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Python Jenkins is a python wrapper for the Jenkins REST API which aims
to provide a more conventionally pythonic way of controlling a Jenkins
server. It provides a higher-level API containing a number of
convenience functions.

This package contains pickles for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

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
%make -C doc html
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
python setup.py testr -v --slowest
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 setup.py testr -v --slowest
popd
%endif

%files
%doc *.rst doc/build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-py%oname
%doc *.rst doc/build/html
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1.git20150810
- Initial build for Sisyphus

