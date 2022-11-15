%define oname httplib2

Name: python3-module-httplib2
Version: 0.21.0
Release: alt1

Summary: A comprehensive HTTP client library in Python

License: MIT
Group: Development/Python
URL: https://github.com/httplib2/httplib2

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

%description
A comprehensive HTTP client library that supports many features left out
of other HTTP libraries.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
#doc CHANGELOG *.html *.md doc/html
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Nov 15 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.21.0-alt1
- NMU: new version 0.21.0

* Sat Feb 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.20.4-alt1
- NMU: new version 0.20.4 (ALT #41865)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.19.1-alt1
- new version 0.19.1 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt1
- new version 0.19.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.18.1-alt1
- new version 0.18.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- build python3 package

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Version 0.9

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Version 0.8

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.7-alt1.1
- Rebuild with Python-3.3

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.7-alt1
- Version 0.7.7

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1
- Version 0.7.4

* Sat May 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.5.0-alt1
- Building 0.5.0-alt instead of 0.4.0-alt2. Version up + fixed packaging errors.

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.4.0-alt2
- Fixing packaging errors.

* Wed Oct 08 2008 Mikhail Pokidko <pma@altlinux.org> 0.4.0-alt1
- Initial ALT build


