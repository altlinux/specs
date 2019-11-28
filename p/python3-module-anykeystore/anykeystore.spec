%define oname anykeystore

Name: python3-module-%oname
Version: 0.2
Release: alt3

Summary: A key-value store supporting multiple backends
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/anykeystore/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

This package contains tests for %oname.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt3
- python2 disabled

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

