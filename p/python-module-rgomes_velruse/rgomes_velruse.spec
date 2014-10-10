%define oname rgomes_velruse

%def_with python3

Name: python-module-%oname
Version: 1.1.2
Release: alt1.git20131030
Summary: Simplifying third-party authentication for web applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/rgomes_velruse
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/frgomes/velruse.git
# branch: feature.kotti_auth
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides velruse
Conflicts: python-module-velruse

%description
NON OFFICIAL FIXES on velruse.

See: https://github.com/frgomes/velruse/tree/feature.kotti_auth

%package -n python3-module-%oname
Summary: Simplifying third-party authentication for web applications
Group: Development/Python3
%py3_provides velruse
Conflicts: python3-module-velruse

%description -n python3-module-%oname
NON OFFICIAL FIXES on velruse.

See: https://github.com/frgomes/velruse/tree/feature.kotti_auth

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20131030
- Initial build for Sisyphus

