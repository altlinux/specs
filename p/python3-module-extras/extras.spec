%define _unpackaged_files_terminate_build 1
%define oname extras

Name: python3-module-%oname
Version: 1.0.0
Release: alt3

Summary: Useful extra bits for Python - things that shold be in the standard library

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/extras

Source0: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.

%package tests
Summary: Tests for extras
Group: Development/Python3
Requires: %name = %EVR

%description tests
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.

This package contains tests for extras.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE NEWS *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Sun Jun 05 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt3
- Drop 2to3 dependency.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20140919.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20140919
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1
- Initial build for Sisyphus

