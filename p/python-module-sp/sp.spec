%define oname sp
Name: python-module-%oname
Version: 2.2.2
Release: alt1.1
Summary: SP (Simple Parser), Python parser generator
License: LGPL v3 or later
Group: Development/Python
Url: http://www.cdsoft.fr/sp/sp.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel

%description
SP (Simple Parser) is a Python parser generator. It is aimed at easy
usage rather than performance. SP produces Top-Down Recursive descent
parsers. SP also uses memoization to optimize parsers' speed when
dealing with ambiguous grammars.

%package docs
Summary: Documentation and examples for Simple Parser
Group: Development/Documentation

%description docs
SP (Simple Parser) is a Python parser generator. It is aimed at easy
usage rather than performance. SP produces Top-Down Recursive descent
parsers. SP also uses memoization to optimize parsers' speed when
dealing with ambiguous grammars.

This package contains documentation and examples for Simple Parser.

%prep
%setup

%install
install -d %buildroot%python_sitelibdir
install -p -m644 %oname.py %buildroot%python_sitelibdir

%files
%python_sitelibdir/*

%files docs
%doc doc examples

%changelog
* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2-alt1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus

