%define oname pathtools

Name: python3-module-%oname
Version: 0.1.2
Release: alt2
Summary: Path utilities for Python
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/pathtools/

# https://github.com/gorakhargosh/pathtools.git
Source: %oname-%version.tar

Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-build-python3

%description
Pattern matching and various utilities for file systems paths.

%prep
%setup -n %oname-%version
%patch1 -p1

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS README
%python3_sitelibdir/*

%changelog
* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.2-alt2
- Drop ptyhon2 support.
- Build without docs.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Updated to upstream version 0.1.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20111003.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20111003.1
- NMU: Use buildreq for BR.

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20111003
- Initial build for Sisyphus

