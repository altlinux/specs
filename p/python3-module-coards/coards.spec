%define oname coards

Name: python3-module-%oname
Version: 1.0.5
Release: alt2
Summary: A parser for COADS-compliant dates
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/coards/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
A COADS compliant time parser.

This module is intended to help parse time values represented using the
COARDS convention.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.txt *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.5-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus

