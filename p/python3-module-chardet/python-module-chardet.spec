%define pkgname	chardet

Name: python3-module-chardet
Version: 3.0.4
Release: alt3
Epoch: 1

Summary: Character encoding auto-detection in Python

License: LGPL-2.1
Url: https://pypi.python.org/pypi/%pkgname
Group: Development/Python3

Packager: Evgenii Terechkov <evg@altlinux.ru>

Source: https://pypi.python.org/packages/source/c/chardet/%pkgname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Character encoding auto-detection in Python.

%prep
%setup -n %pkgname-%version

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%_bindir/

%files
%python3_sitelibdir/%pkgname/
%python3_sitelibdir/*.egg-info/

%changelog
* Wed Sep 08 2021 Grigory Ustinov <grenka@altlinux.org> 1:3.0.4-alt3
- Build without python2 support.

* Sun Dec 13 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.0.4-alt2
- Downgrade to version 3.0.4.

* Fri Dec 11 2020 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Sun Apr 13 2014 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)
- build for python3 too

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Mar 22 2010 Terechkov Evgenii <evg@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.3.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.3
- Site-packages removed from packages (Closes #18909)
- Packager tag added

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.2
- Really fix build on x86_64

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.1
- Egg dropped to build on x86_64

* Sun Dec 28 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux Sisyphus (thanks Mandriva for initial spec)
