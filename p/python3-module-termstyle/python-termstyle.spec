%define oname termstyle

Name: python3-module-%oname
Version: 0.1.10
Release: alt2
Summary: Console colouring for python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-termstyle/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%py3_provides %oname

%description
termstyle is a simple python library for adding coloured output to
terminal (console) programs. The definitions come from ECMA-048, the
"Control Functions for Coded Character Sets" standard.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.10-alt2
- Drop python2 support.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt1
- Initial build for Sisyphus

