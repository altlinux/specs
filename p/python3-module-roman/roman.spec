%define oname roman

Name: python3-module-%oname
Version: 2.0.0
Release: alt2
Summary: Integer to Roman numerals converter
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/roman/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Integer to Roman numerals converter.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc CHANGES.txt PKG-INFO
%python3_sitelibdir/*

%changelog
* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus

