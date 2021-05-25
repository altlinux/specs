%define _unpackaged_files_terminate_build 1

%define oname cgen

Name: python3-module-%oname
Version: 2017.1
Release: alt2
Summary: C/C++ source generation from an AST
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: http://pypi.python.org/pypi/cgen/

# https://github.com/inducer/cgen.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires decorator

%description
C/C++ source generation from an AST.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/*

%changelog
* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 2017.1-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2017.1-alt1.qa1
- NMU: applied repocop patch

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.1-alt1
- Updated to upstream version 2017.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.1.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.1.2-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1
- Version 2013.1.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 2012.1-alt1.1
- Rebuild with Python-3.3

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt1
- Initial build for Sisyphus

