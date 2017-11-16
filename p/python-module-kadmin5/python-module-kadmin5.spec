%define oname kadmin5

Name: python-module-%oname
Version: 0.0.5
Release: alt6

Summary: Kerveros 5 database administration API for Python.

License: GPLv2
Group: System/Libraries
Url: http://git.etersoft.ru/people/iv/packages/python-module-kadmin5.git

Packager: Ivan Melnikov <iv@altlinux.org>

%setup_python_module %oname

Source: %oname-%version.tar.bz2

# Automatically added by buildreq on Wed Apr 23 2008
BuildRequires: boost-python-devel gcc-c++ libcom_err-devel libkrb5-devel python-devel scons

BuildRequires: boost-devel >= 1.39.0

%description
Kerveros 5 database administration API for Python.

%prep
%setup -q -n %oname-%version

%build
scons

%install
scons install DESTDIR=%buildroot

%files
%python_sitelibdir/*

%changelog
* Fri Jul 14 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.5-alt6
- Rebuild with krb5-1.15

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 0.0.5-alt5.qa6.1
- NMU: Rebuild with krb5-1.14

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0.5-alt5.qa6
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.0.5-alt5.4.1
- rebuild with boost 1.57.0

* Mon Mar 31 2014 Timur Aitov <timonbl4@altlinux.org> 0.0.5-alt5.4
- Rebuild with krb5-1.12

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt5.3
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt5.2
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt5.1
- Rebuilt with Boost 1.51.0

* Mon Apr 23 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.5-alt5
- Rebuild with krb5-1.10

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.5-alt4.1.3.3.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt4.1.3.3
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt4.1.3.2
- Rebuilt with Boost 1.48.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.5-alt4.1.3.1
- Rebuild with Python-2.7

* Wed Jul 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt4.1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt4.1.2
- Rebuilt with Boost 1.46.1 and for debuginfo

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.5-alt4.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt4.1
- Rebuilt with python 2.6

* Sat Jun 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.5-alt4
- rebuild with boost-1.39.0

* Fri Jan 23 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.5-alt3
- build for sisyphus

* Fri Nov 07 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.5-alt2
- added workaround for better return code from kadmin5::get_princ_keys(...)

* Fri Nov 07 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.5-alt1
- new version:
  - support for error callbacks
  - kadm5 error codes binded

* Thu Sep 11 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.4-alt1
- new version: bugfixes

* Wed Sep 10 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.3-alt1
- new version: added get_realm() method to kadmin class

* Thu Jun 26 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.2-eter1
- new version: access to principal atributes implemented

* Wed Apr 23 2008 Ivan Melnikov <imelnikov@etersoft.ru> 0.0.1-eter1
- inital build


