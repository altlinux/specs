%define oname cctrial

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt1.git20150814
Summary: Continous trial runner
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cctrial
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tardyp/cctrial.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-twisted-core-test python-module-argh
BuildPreReq: python-module-watchdog
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-twisted-core-test python3-module-argh
BuildPreReq: python3-module-watchdog
%endif

%py_provides %oname
Requires: python-module-twisted-core-test
%py_requires argh watchdog

%description
cctrial is a tool for using twisted trial in a continuous manner.

cctrial will re-run failed tests until all succeed.

cctrial is designed for a specific workflow, which helps doing big
refactors that break lots of tests.

cctrial smart mode can run only the tests that import the modified file.

cctrial is not designed to replace trial, for all other usecases.

%if_with python3
%package -n python3-module-%oname
Summary: Continous trial runner
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-twisted-core-test
%py3_requires argh watchdog

%description -n python3-module-%oname
cctrial is a tool for using twisted trial in a continuous manner.

cctrial will re-run failed tests until all succeed.

cctrial is designed for a specific workflow, which helps doing big
refactors that break lots of tests.

cctrial smart mode can run only the tests that import the modified file.

cctrial is not designed to replace trial, for all other usecases.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python setup.py test -v
py.test -vv %oname/*.py
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv %oname/*.py
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150814
- Initial build for Sisyphus

