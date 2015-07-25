%define oname see

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt1.git20150417
Summary: A human-readable alternative to dir
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/see
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/inky/see.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%py_provides %oname

%description
An alternative to Python's dir function. Easy to type; easy to read! For
humans only.

%if_with python3
%package -n python3-module-%oname
Summary: A human-readable alternative to dir
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
An alternative to Python's dir function. Easy to type; easy to read! For
humans only.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150417
- Initial build for Sisyphus

