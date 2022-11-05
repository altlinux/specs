%define oname sphinx_rtd_theme

Name: python3-module-%oname
Version: 1.1.1
Release: alt1

Summary: ReadTheDocs.org theme for Sphinx

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinx_rtd_theme/

# https://github.com/snide/sphinx_rtd_theme.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This is a prototype mobile-friendly sphinx_ theme I made for
readthedocs.org_. It's currently in development and includes some rtd
variable checks that can be ignored if you're just trying to use it on
your project outside of that site.

%prep
%setup

%build
export CI=":"
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Sat Nov 05 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Build new version.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.2-alt2
- Drop python2 support.

* Sun May 30 2021 Fr. Br. George <george@altlinux.ru> 0.5.2-alt1
- Build new version.

* Fri Feb 15 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt1
- Build new version.

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.4.2-alt1
- Build new version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.8-alt1.git20150730.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt1.git20150730.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20150730
- Version 0.1.8

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141202
- New snapshot
- Added module for Python 3

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140821
- Initial build for Sisyphus

