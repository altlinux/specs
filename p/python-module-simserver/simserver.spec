%define oname simserver

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20121102
Summary: Document similarity server, using gensim
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/simserver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/piskvorky/gensim-simserver.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-gensim python-module-Pyro4
BuildPreReq: python-module-sqlitedict libnumpy-devel
BuildPreReq: python-module-serpent
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-gensim python3-module-Pyro4
BuildPreReq: python3-module-sqlitedict python-tools-2to3
BuildPreReq: python3-module-serpent python3-module-six
BuildPreReq: libnumpy-py3-devel python3-module-scipy
%endif

%py_provides %oname
%py_requires gensim

%description
Index plain text documents and query the index for semantically related
documents.

Simserver uses transactions internally to provide a robust and scalable
similarity server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Index plain text documents and query the index for semantically related
documents.

Simserver uses transactions internally to provide a robust and scalable
similarity server.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Document similarity server, using gensim
Group: Development/Python3
%py3_provides %oname
%py3_requires gensim

%description -n python3-module-%oname
Index plain text documents and query the index for semantically related
documents.

Simserver uses transactions internally to provide a robust and scalable
similarity server.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Index plain text documents and query the index for semantically related
documents.

Simserver uses transactions internally to provide a robust and scalable
similarity server.

This package contains tests for %oname.

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
%doc *.rst docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20121102
- Initial build for Sisyphus

