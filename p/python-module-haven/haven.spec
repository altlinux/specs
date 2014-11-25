%define oname haven

%def_with python3

Name: python-module-%oname
Version: 1.1.60
Release: alt1.git20141120
Summary: flask's style binary server framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/haven/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dantezhu/haven.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-events python-module-netkit
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-events python3-module-netkit
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires events netkit

%description
flask's style binary server framework.

%package -n python3-module-%oname
Summary: flask's style binary server framework
Group: Development/Python3
%py3_provides %oname
%py3_requires events netkit

%description -n python3-module-%oname
flask's style binary server framework.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.60-alt1.git20141120
- Initial build for Sisyphus

