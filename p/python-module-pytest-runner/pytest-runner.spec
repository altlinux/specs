%define oname pytest-runner

%def_with python3

Name: python-module-%oname
Version: 2.6.1
Release: alt2
Summary: Invoke py.test as distutils command with dependency resolution
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-runner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-setuptools_scm
#python-module-hgtools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-setuptools_scm
#python3-module-hgtools
%endif

%py_provides ptr

%description
Setup scripts can use pytest-runner to add setup.py test support for
pytest runner.

%package -n python3-module-%oname
Summary: Invoke py.test as distutils command with dependency resolution
Group: Development/Python3
%py3_provides ptr

%description -n python3-module-%oname
Setup scripts can use pytest-runner to add setup.py test support for
pytest runner.

%prep
%setup

pushd ..
git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version
popd

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.1-alt2
- remove hgtools from buildreq

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1
- Version 2.6.1

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

