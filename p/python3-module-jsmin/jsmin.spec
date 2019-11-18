%define _unpackaged_files_terminate_build 1
%define oname jsmin

Name: python3-module-%oname
Version: 2.2.1
Release: alt2

Summary: JavaScript minifier
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsmin/
BuildArch: noarch

Source0: https://pypi.python.org/packages/87/8c/89cfe7ea967e0a4623b4e61008523ff40805c2bd4eabb1b07671643ea953/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
JavaScript minifier.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
JavaScript minifier.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.11-alt1
- Initial build for Sisyphus

