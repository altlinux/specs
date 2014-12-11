%define oname coveralls

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5
Release: alt1.git20141210
Summary: Show coverage stats online via coveralls.io
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/coveralls/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/coagulant/coveralls-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml python-module-docopt
BuildPreReq: python-module-coverage python-module-requests
BuildPreReq: python-module-mock python-module-pytest
BuildPreReq: python-module-sh python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml python3-module-docopt
BuildPreReq: python3-module-coverage python3-module-requests
BuildPreReq: python3-module-mock python3-module-pytest
BuildPreReq: python3-module-sh
%endif

%py_provides %oname

%description
Coveralls.io is service to publish your coverage stats online with a lot
of nice features. This package provides seamless integration with
coverage.py in your python projects. For ruby projects, there is an
official gem. Only projects hosted on Github are supported.

%package -n python3-module-%oname
Summary: Show coverage stats online via coveralls.io
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Coveralls.io is service to publish your coverage stats online with a lot
of nice features. This package provides seamless integration with
coverage.py in your python projects. For ruby projects, there is an
official gem. Only projects hosted on Github are supported.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst *.md example
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst *.md example
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20141210
- Version 0.5

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20140928
- Initial build for Sisyphus

