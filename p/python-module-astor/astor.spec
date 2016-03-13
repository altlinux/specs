%define oname astor

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.git20150130.1
Summary: Read/rewrite/write Python ASTs
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/astor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/berkerpeksag/astor.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-wheel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-wheel
%endif

%py_provides %oname

%description
astor is designed to allow easy manipulation of Python source via the
AST.

%package -n python3-module-%oname
Summary: Read/rewrite/write Python ASTs
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
astor is designed to allow easy manipulation of Python source via the
AST.

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
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc AUTHORS CHANGES *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20150130.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150130
- Initial build for Sisyphus

