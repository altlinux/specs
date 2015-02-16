%define oname pytsort

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20150215
Summary: Topological Sorting in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytsort/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mtasic85/pytsort.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname tsort

%description
Topological Sorting in Python.

%package -n python3-module-%oname
Summary: Topological Sorting in Python
Group: Development/Python3
%py3_provides %oname tsort

%description -n python3-module-%oname
Topological Sorting in Python.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python tsort.py
%if_with python3
pushd ../python3
python3 tsort.py
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150215
- Initial build for Sisyphus

