%define oname cov-core

Name: python3-module-%oname
Version: 1.15.0
Release: alt2.git20141122
Summary: plugin core for use by pytest-cov, nose-cov and nose2-cov
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/cov-core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/schlamar/cov-core.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-coverage

%py3_provides cov_core
%py3_provides cov_core_init

%description
This is a lib package for use by pytest-cov, nose-cov and nose2-cov.
Unless you're developing a coverage plugin for a test framework, you
probably want one of those.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst *.md
%python3_sitelibdir/*

%changelog
* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 1.15.0-alt2.git20141122
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.15.0-alt1.git20141122.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.15.0-alt1.git20141122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.0-alt1.git20141122
- Version 1.15.0

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.0-alt1.git20140822
- Initial build for Sisyphus

