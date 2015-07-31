%define oname codecov

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.3
Release: alt1.git20150726
Summary: Python report uploader for Codecov
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/codecov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/codecov/codecov-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-coverage
BuildPreReq: python-module-unittest2 python-module-nose
BuildPreReq: python-module-nose-cov python-module-rednose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-coverage
BuildPreReq: python3-module-unittest2 python3-module-nose
BuildPreReq: python3-module-nose-cov python3-module-rednose
%endif

%py_provides %oname
%py_requires requests coverage

%description
Hosted coverage reports for @github, @bitbucket and @gitlab.

%if_with python3
%package -n python3-module-%oname
Summary: Python report uploader for Codecov
Group: Development/Python3
%py3_provides %oname
%py3_requires requests coverage

%description -n python3-module-%oname
Hosted coverage reports for @github, @bitbucket and @gitlab.
%endif

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

%check
python setup.py test
nosetests -vv --rednose --with-cov
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -vv --rednose --with-cov
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.git20150726
- Initial build for Sisyphus

