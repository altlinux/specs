%define oname pycobertura

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20141127
Summary: A Cobertura coverage report parser written in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pycobertura/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/SurveyMonkey/pycobertura.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-click-tests python-module-colorama
BuildPreReq: python-module-tabulate python-module-mock
BuildPreReq: python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-click-tests python3-module-colorama
BuildPreReq: python3-module-tabulate python3-module-mock
BuildPreReq: python3-module-pytest-cov
%endif

%py_provides %oname

%description
A Cobertura coverage report parser written in Python.

%package -n python3-module-%oname
Summary: A Cobertura coverage report parser written in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Cobertura coverage report parser written in Python.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version
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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141127
- Initial build for Sisyphus

