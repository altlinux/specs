%define oname ClientForm

Name: python3-module-%oname
Version: 0.2.10
Release: alt5

Summary: Python module for handling HTML forms on the client side

License: BSD-like
Group: Development/Python3
Url: http://wwwsearch.sourceforge.net/ClientForm

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://wwwsearch.sourceforge.net/ClientForm/src/%oname-%version.tar.gz

BuildArch: noarch

#BuildPreReq: rpm-build-compat >= 1.2

BuildRequires(pre): rpm-build-python3 /usr/bin/2to3

%description
ClientForm is a Python module for handling HTML forms on the client side,
useful for parsing HTML forms, filling them in and returning the completed
forms to the server. It developed from a port of Gisle Aas' Perl module
HTML::Form, from the libwww-perl library, but the interface is not the same.

%prep
%setup -n %oname-%version

%build
find . -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build

%install
%python3_install

%files
%doc ChangeLog.txt COPYING.txt COPYRIGHT.txt GeneralFAQ.html README.txt
%python3_sitelibdir/__pycache__/ClientForm*
%python3_sitelibdir/ClientForm.*
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.10-alt5
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.10-alt4.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.10-alt4.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.10-alt4.1
- NMU: Use buildreq for BR.

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt4
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.10-alt3.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt3
- Rebuilt with python 2.6

* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.10-alt2
- cleanup spec (thanks to Dmitry Levin)
- build as noarch

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.10-alt1
- new version 0.2.10, cleanup spec
- change Packager

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.1.17-alt1.1
- Rebuilt with python-2.5.

* Sat Apr 2 2005 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.17-alt1
- Updated to 0.1.17

* Sat Aug 7 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.16-alt1
- Updated to 0.1.16

* Thu Feb 26 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.15-alt2
  Fixed URL

* Tue Feb 24 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.15-alt1
  Initial build
