%define oname providerjson

%def_with python3

Name: python-module-%oname
Version: 0.0.22
Release: alt1.git20141119
Summary: Provider JSON - Command Line Utitlity and Python Library
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/providerjson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/HHSIDEAlab/pjson.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides pjson

%description
Outputs a JSON array of errors and warnings found in a Provider JSON
string or file.

%package -n python3-module-%oname
Summary: Provider JSON - Command Line Utitlity and Python Library
Group: Development/Python3
%py3_provides pjson

%description -n python3-module-%oname
Outputs a JSON array of errors and warnings found in a Provider JSON
string or file.

%prep
%setup

mv python/* ./

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
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
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
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.22-alt1.git20141119
- Initial build for Sisyphus

