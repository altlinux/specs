%define oname sp

%def_with python3

Name: python-module-%oname
Version: 2.2.2
Release: alt2.1
Summary: SP (Simple Parser), Python parser generator
License: LGPL v3 or later
Group: Development/Python
Url: http://www.cdsoft.fr/sp/sp.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base
BuildRequires: rpm-build-python3

%description
SP (Simple Parser) is a Python parser generator. It is aimed at easy
usage rather than performance. SP produces Top-Down Recursive descent
parsers. SP also uses memoization to optimize parsers' speed when
dealing with ambiguous grammars.

%package -n python3-module-%oname
Summary: SP (Simple Parser), Python parser generator
Group: Development/Python3

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
%endif

%install
install -d %buildroot%python_sitelibdir
install -p -m644 %oname.py %buildroot%python_sitelibdir

%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir
install -p -m644 %oname.py %buildroot%python3_sitelibdir
popd
%endif

%files
%python_sitelibdir/*

%files docs
%doc doc examples

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.2-alt2.1
- NMU: Use buildreq for BR.

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt2
- Added module for Python 3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2-alt1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus

