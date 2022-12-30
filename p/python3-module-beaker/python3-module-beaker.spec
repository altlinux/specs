%define oname Beaker

Name: python3-module-beaker
Version: 1.12.0
Release: alt1

Summary: A Session and Caching library with WSGI Middleware

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/bbangert/beaker

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

BuildArch: noarch

%add_python3_req_skip jarray javax
%add_python3_req_skip javax.crypto javax.crypto.spec

%description
Beaker is a web session and general caching library that includes WSGI
middleware for use in web applications. As a general caching library, Beaker can
handle storing for various times any Python object that can be pickled with
optional back-ends on a fine-grained basis. Beaker was built largely on the code
from MyghtyUtils, then refactored and extended with database support.

%prep
%setup

%build
%python3_build

%install
%python3_install

# need servers running
#check
#python3_test

%files
%doc README.rst
%python3_sitelibdir/beaker/
%python3_sitelibdir/Beaker-*.egg-info

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt1
- new version 1.12.0 (with rpmrb script)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt2
- build python3 module separately

* Wed May 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.10.1-alt1
- Build new version.
- Cleanup spec.

* Fri Apr 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.0-alt2
- Variable causing build error fixed

* Mon Mar 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9.0-alt1
- Version 1.9.0.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz at altlinux.org> 1.7.0-alt1.dev.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 1.7.0-alt1.dev.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem at altlinux.org> 1.7.0-alt1.dev.1
- NMU: Use buildreq for BR.

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.dev
- Version 1.7.0dev

* Fri Mar 22 2013 Aleksey Avdeev <solo at altlinux.ru> 1.6.4-alt1.1
- Rebuild with Python-3.3

* Sat Sep 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1
- Version 1.6.4

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1
- Version 1.6.3
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty at altlinux.ru> 1.3.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.1
- Rebuilt with python 2.6

* Tue Aug 04 2009 Paul Wolneykien <manowar at altlinux.ru> 1.3.1-alt1
- Initial build for ALTLinux

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Kyle VanderBeek <kylev@kylev.com> - 1.3.1-5
- Add patch based on upstream hg 403ef7c82d32 for config overwriting that
  breaks Pylons unit tests

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-4
- Add a patch to remove the use of __future__.absolute_import in the google
  backend

* Sat Jun 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-3
- Different hmac patch suitable for upstream inclusion.

* Tue Jun 02 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-2
- Add a patch to remove Beaker&#39;s use of hashlib on Python2.4,
  due to incompatiblities with Python&#39;s hmac module (#503772)

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Tue Apr 07 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3-1
- Update to 1.3
 
* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.3-1
- Update to 1.2.3
 
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Sat Dec 20 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.1.2-1
- Update to 1.1.2
 
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.3-2
- Rebuild for Python 2.6

* Tue Jun 24 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.0.3-1
- Update to 1.0.3.

* Tue Jun 24 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.5-1
- Update to 0.9.5.
- Remove license patch which is now corrected upstream.

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-4
- Fix files to not use wildcard, fixing dir ownership

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-3
- Corrected license

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-2
- More restrictive file includes for safety

* Sun May 11 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-1
- Update to 0.9.4 (security fix)
- Fix rpmlint complaints, add CHANGELOG and LICENSE

* Wed Apr  9 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.3-1
- Initial version.
