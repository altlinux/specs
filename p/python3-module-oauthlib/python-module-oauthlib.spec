%global oname oauthlib

Name: python3-module-oauthlib
Version: 3.2.2
Release: alt1

Summary: An implementation of the OAuth request-signing logic

License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/oauthlib

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_use Crypto >= 2.6

%description
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

# %check
# python setup.py test

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.2.2-alt1
- new version 3.2.2 (with rpmrb script)

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt2
- Fixed BuildRequires.

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- new version 3.2.0 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt2
- build python3 module separately, cleanup spec

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.2-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1.1
- NMU: Use buildreq for BR.

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1
- Version 0.6.3

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.1
- Added module for Python 3

* Fri Jul 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.6.0-alt1
- First build for ALT (based on Fedora 0.6.0-6.fc21.src)

