%define oname pyresttest

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 1.3.1
Release: alt1.git20150213.1
Summary: Python RESTful API Testing & Microbenchmarking Tool
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pyresttest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/svanoort/pyresttest.git
Source: %name-%version.tar
Source1: repocop-test-hint:binary:python-module-pyresttest:altlinux-python-test-is-packaged
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-yaml python-module-pycurl
BuildPreReq: python-module-django-tests python-module-jsonschema
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-yaml python3-module-pycurl
BuildPreReq: python3-module-django-tests python3-module-jsonschema
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
* A simple but powerful REST testing and benchmarking framework
* Minimal dependencies, designed to slot into automated configuration
  management/orchestration tools
* Tests are defined in basic YAML or JSON config files, no code needed
* Logic is written and extensible in Python

%if_with python3
%package -n python3-module-%oname
Summary: Python RESTful API Testing & Microbenchmarking Tool
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
* A simple but powerful REST testing and benchmarking framework
* Minimal dependencies, designed to slot into automated configuration
  management/orchestration tools
* Tests are defined in basic YAML or JSON config files, no code needed
* Logic is written and extensible in Python
%endif

%prep
%setup

chmod +x run_tests.sh

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
	mv $i ${i}3
done
popd
%endif

%python_install

%check
./run_tests.sh
%if_with python3
pushd ../python3
sed -i 's|^python|python3|' run_tests.sh
export PYTHONPATH=$PWD
./run_tests.sh
popd
%endif

%files
%doc *.md *.yaml *.json
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.yaml *.json
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.git20150213.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20150213
- Version 1.3.1

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20141231
- Version 1.2.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141228
- Version 1.1.1

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20141125
- Initial build for Sisyphus

