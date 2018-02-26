%define oname yum-metadata-parser

Name: python-module-yum-metadata-parser
Version: 1.1.4
Release: alt1.1.1

Summary: A fast metadata parser for yum

License: GPL
Group: System/Configuration/Packaging
Url: http://devel.linux.duke.edu/cgi-bin/viewcvs.cgi/yum-metadata-parser/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://linux.duke.edu/projects/yum/download/yum-metadata-parser/%oname-%version.tar

# Automatically added by buildreq on Sat Feb 12 2011
BuildRequires: glib2-devel libsqlite3-devel libxml2-devel python-module-paste python-module-peak

%description
Fast metadata parser for yum implemented in C.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README AUTHORS ChangeLog
%python_sitelibdir/_sqlitecache.so
%python_sitelibdir/sqlitecachec.py
%python_sitelibdir/sqlitecachec.pyc
%python_sitelibdir/sqlitecachec.pyo
%python_sitelibdir/yum_metadata_parser-*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt1.1
- Rebuild with Python-2.7

* Sat Feb 12 2011 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Wed Jan 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.4-1mdv2010.1
+ Revision: 490763
- update to new version 1.1.4

* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1.2-6mdv2010.0
+ Revision: 446314
- rebuild

* Thu Dec 25 2008 Michael Scherer <misc@mandriva.org> 1.1.2-5mdv2009.1
+ Revision: 318499
- rebuild for new python

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1.2-4mdv2009.0
+ Revision: 262976
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1.2-3mdv2009.0
+ Revision: 262813
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-1mdv2008.1
+ Revision: 115434
- import yum-metadata-parser

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-1mdv2008.1
- first mdv release
