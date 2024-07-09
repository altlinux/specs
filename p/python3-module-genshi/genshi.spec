%define modulename genshi

Name: python3-module-%modulename
Version: 0.7.9
Release: alt1

Summary: A toolkit for stream-based generation of output for the web

License: BSD
Group: Development/Python3
Url: http://genshi.edgewall.org/

# https://github.com/edgewall/genshi
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
%python3_test

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/*.egg-info

%changelog
* Tue Jul 09 2024 Grigory Ustinov <grenka@altlinux.org> 0.7.9-alt1
- Automatically updated to 0.7.9.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.7-alt1
- Automatically updated to 0.7.7.

* Mon Mar 14 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.6-alt1
- Build new version.

* Sat Oct 16 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.5-alt1
- Build new version.

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt2
- NMU: cleanup spec, don't pack tests, fix tests requires

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.4-alt1
- Build new version.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.3-alt1
- Build new version.
- Drop python2 support.

* Tue May 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7-alt2
- Added compiler.ast to skip python3 autoreq generator list.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6-alt2.1
- Rebuild with Python-3.3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6
- Added docs and examples

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Rebuilt with python 2.6

* Sun Nov 16 2008 Ivan Fedorov <ns@altlinux.org> 0.5.1-alt1
- 0.5.1

* Sun Jan 06 2008 Ivan Fedorov <ns@altlinux.org> 0.4.4-alt2
- fix building

* Sun Jan 06 2008 Ivan Fedorov <ns@altlinux.org> 0.4.4-alt1
- Initial build for ALT Linux Sisyphus.
