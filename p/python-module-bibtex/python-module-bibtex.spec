Name: python-module-bibtex
Version: 1.2.4
Release: alt3.3.1.1

Summary: Python extension to parse BibTeX files

License: GPL
Group: Development/Python
Url: http://www.pybliographer.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://downloads.sf.net/pybliographer/python-bibtex-%version.tar.bz2
Patch: %name-%version-fix-test.patch

%setup_python_module bibtex

# manually removed: eric
# Automatically added by buildreq on Sat Jan 12 2008
BuildRequires: glib2-devel python-devel python-modules-compiler recode recode-devel

BuildPreReq: rpm-build-compat >= 1.4 recode >= 3.6-alt6

Provides: python-bibtex

%description
This module contains two extensions needed for pybliographer:
 - a bibtex parser
 - a simple binding to GNU Recode

%prep
%setup -q -n python-bibtex-%version
%patch -p1

%build
%python_build
# missing macros
#python_check
#python setup.py check

%install
%python_install

%files
%python_sitelibdir/_bibtex.so
%python_sitelibdir/_recode.so
%python_sitelibdir/*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt3.3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt3.3.1
- Rebuild with Python-2.7

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt3.3
- Disabled check (broken)

* Fri Nov 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt3.2
- Enabled check

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt3.1
- Rebuilt with python 2.6

* Thu Aug 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt3
- fix checking (thanks, Ubuntu)

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt2
- update buildreq
- cleanup spec with python macroses

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt1
- new version 1.2.4 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)

* Tue Dec 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- rebuild with python 2.4
- add setup_python_module

* Mon Nov 29 2004 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- first build for ALT Linux Sisyphus

* Tue Nov 16 2004 Zoltan Kota <z.kota at gmx.net> - 0:1.2.1-1.rhfdr_core_3
- initial rpm for Fedora Core 3
