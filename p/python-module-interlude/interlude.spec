%define oname interlude

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt2
Summary: Interlude for Doctests provides an Interactive Console
License: LGPL
Group: Development/Python
Url: http://pypi.python.org/pypi/interlude/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
Provides an interactive shell aka console inside your doctest case.

The console looks exact like in a doctest-case and you can copy and
paste code from the shell into your doctest. It feels as you are in the
test case itself. Its not pdb, it's a python shell.

%if_with python3
%package -n python3-module-%oname
Summary: Interlude for Doctests provides an Interactive Console (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Provides an interactive shell aka console inside your doctest case.

The console looks exact like in a doctest-case and you can copy and
paste code from the shell into your doctest. It feels as you are in the
test case itself. Its not pdb, it's a python shell.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

