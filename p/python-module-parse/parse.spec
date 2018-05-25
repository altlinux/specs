%define oname parse

%def_with python3

Name: python-module-%oname
Version: 1.8.2
Release: alt1
Summary: parse() is the opposite of format()
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/parse

# https://github.com/r1chardj0n3s/parse.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Parse strings using a specification based on the Python format() syntax.

%if_with python3
%package -n python3-module-%oname
Summary: parse() is the opposite of format()
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Parse strings using a specification based on the Python format() syntax.
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

%check
py.test
%if_with python3
pushd ../python3
py.test3
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
* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt1
- Updated to upstream version 1.8.2.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.6-alt2
- Fixed tests.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.6-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1.git20141117
- Initial build for Sisyphus

