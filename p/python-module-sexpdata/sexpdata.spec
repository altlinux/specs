%define oname sexpdata

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.dev1.git20140308
Summary: S-expression parser for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sexpdata/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tkf/sexpdata.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
sexpdata is a simple S-expression parser/serializer. It has simple load
and dump functions like pickle, json or PyYAML module.

%package -n python3-module-%oname
Summary: S-expression parser for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
sexpdata is a simple S-expression parser/serializer. It has simple load
and dump functions like pickle, json or PyYAML module.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	../python3/sexp2json.py
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
install -p -m755 sexp2json.py %buildroot%python_sitelibdir/
install -d %buildroot%_bindir
ln -s %python_sitelibdir/sexp2json.py %buildroot%_bindir/sexp2json

%if_with python3
pushd ../python3
%python3_install
install -p -m755 sexp2json.py %buildroot%python3_sitelibdir/
ln -s %python3_sitelibdir/sexp2json.py %buildroot%_bindir/sexp2json.py3
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
%doc *.rst doc/source/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/source/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.dev1.git20140308
- Initial build for Sisyphus

