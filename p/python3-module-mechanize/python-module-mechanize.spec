%define oname mechanize

Name: python3-module-%oname
Version: 0.4.7
Release: alt1

Summary: Stateful programmatic web browsing

License: BSD ZPL
Group: Development/Python3
Url: https://github.com/python-mechanize/mechanize

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

%description
Stateful programmatic web browsing in Python,
after Andy Lester's Perl module WWW::Mechanize.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc examples/
%python3_sitelibdir/*

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 0.4.7-alt1
- new version 0.4.7 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt1
- new version 0.4.5 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt2
- build python3 package separately

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt1
- new version 0.4.3 (with rpmrb script)

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version (0.4.2) with rpmgs script

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt1.1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1.1.1
- NMU: Use buildreq for BR.

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.1
- Added module for Python 3

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt1
- new version 0.2.5 (with rpmrb script)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.11-alt1.1
- Rebuild with Python-2.7

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.11-alt1
- new version 0.1.11 (with rpmrb script)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt3
- Rebuilt with python 2.6

* Thu Feb 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt2
- build as noarch

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt1
- new version 0.1.10 (with rpmrb script)

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.7b-alt1
- initial build for ALT Linux Sisyphus

