%define oname sp

Name: python3-module-%oname
Version: 2.2.2
Release: alt3

Summary: SP (Simple Parser), Python parser generator
License: LGPL v3 or later
Group: Development/Python3
Url: http://www.cdsoft.fr/sp/sp.html
BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3


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

find ./ -type f -name '*.py' -exec \
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%install
install -d %buildroot%python3_sitelibdir
install -p -m644 %oname.py %buildroot%python3_sitelibdir

%files
%python3_sitelibdir/*

%files docs
%doc doc examples


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.2-alt3
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.2-alt2.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.2-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.2-alt2.1
- NMU: Use buildreq for BR.

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt2
- Added module for Python 3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2-alt1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus

