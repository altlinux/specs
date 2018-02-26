nAME: python3-module-xlwt3
Version: 0.1.2
Release: alt1

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
* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Built for Python 3

