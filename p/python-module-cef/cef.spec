%define oname cef

%def_without python3

Name: python-module-%oname
Version: 0.5
Release: alt2.git20121017.1
Summary: Module that emits CEF logs
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cef
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla/cef.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Most Mozilla Services applications need to generate CEF logs. A CEF Log
is a formatted log that can be used by ArcSight, a central application
used by the infrasec team to manage application security.

The cef module provide a log_cef function that can be used to emit CEF
logs.

%if_with python3
%package -n python3-module-%oname
Summary: Module that emits CEF logs
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Most Mozilla Services applications need to generate CEF logs. A CEF Log
is a formatted log that can be used by ArcSight, a central application
used by the infrasec team to manage application security.

The cef module provide a log_cef function that can be used to emit CEF
logs.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt2.git20121017.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.git20121017
- Fixed build

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20121017
- Initial build for Sisyphus

