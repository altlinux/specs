%define oname cgen

Name: python3-module-%oname
Version: 2025.1
Release: alt1
Summary: C/C++ source generation from an AST
License: MIT
Group: Development/Python3
BuildArch: noarch
URL: https://pypi.org/project/cgen
VCS: https://github.com/inducer/cgen

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%py3_requires decorator

%description
C/C++ source generation from an AST.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Jun 24 2025 Grigory Ustinov <grenka@altlinux.org> 2025.1-alt1
- Automatically updated to 2025.1.

* Tue Jun 29 2021 Grigory Ustinov <grenka@altlinux.org> 2020.1-alt1
- Automatically updated to 2020.1.

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

