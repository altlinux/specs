%global pypi_name python-editor

Name: python3-module-editor
Version: 1.0.4
Release: alt3

Summary: Programmatically open an editor, capture the result

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/fmoo/python-editor

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://pypi.python.org/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-python3

%description
An python module which provides a convenient example.

%prep
%setup -n %pypi_name-%version
rm -rf %pypi_name.egg-info

%build
%python3_build

%install
%python3_install
chmod a+x %buildroot%python3_sitelibdir/editor.py
%__subst "s|python$|python3|g" %buildroot%python3_sitelibdir/editor.py

%check

%files
%doc README.md
%doc LICENSE
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/editor.py*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.4-alt3
- Drop python2 support.

* Sun Feb 09 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt2
- use python2 in the script

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- new version 1.0.4 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Linux Sisyphus

* Wed Aug 26 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.4-1
- Bump to 0.4

* Tue Aug 25 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.3-1
- initial package
