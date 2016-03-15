nAME: python3-module-xlwt3
Version: 0.1.2
Release: alt1.1.1

Summary: Library to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003

License: BSD-style
Group: Development/Python3
Url: http://pypi.python.org/pypi/xlwt3/
BuildArch: noarch

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Buildrequires: python3-devel

%description
Provide a library for developers to use to generate spreadsheet
files compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or
packages outside the standard Python distribution.

%prep
%setup

%build
%python3_build

%install
%python3_build_install

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.1.2-alt1.1
- Rebuild with Python-3.3

* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Built for Python 3

