%define _unpackaged_files_terminate_build 1
%define oname jsonrpcserver

%def_with python3
%def_without python2
%def_disable check

Name: python-module-%oname
Version: 3.5.3
Release: alt1.1
Summary: JSON-RPC 2.0 server library
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/jsonrpcserver

Source: %oname-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-jsonschema
BuildRequires: python-module-nose python-module-pytest
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-nose python3-module-pytest
%endif

%py_provides %oname

%description
A JSON-RPC 2.0 server library for Python 3.

%if_with python3
%package -n python3-module-%oname
Summary: JSON-RPC 2.0 server library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A JSON-RPC 2.0 server library for Python 3.
%endif

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
rm -fR build
py.test
%endif
%if_with python3
pushd ../python3
rm -fR build
py.test3
popd
%endif

%if_with python2
%files
%doc *.md
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.3-alt1
- Updated to upstream version 3.5.3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.11-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.11-alt1.1
- NMU: Use buildreq for BR.

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1
- Version 1.0.11

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Version 1.0.6

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Version 1.0.5

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Version 1.0.4

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Version 1.0.3

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

