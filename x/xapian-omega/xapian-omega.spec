%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: xapian-omega
Version: 1.4.22
Release: alt1

Summary: A CGI search frontend and indexers built on Xapian
License: GPL-2.0-or-later
Group: Networking/WWW

Url: http://www.xapian.org
Source: http://www.oligarchy.co.uk/xapian/%version/%name-%version.tar.bz2

BuildRequires: gcc-c++
BuildRequires: libmagic-devel
BuildRequires: libpcre2-devel
BuildRequires: libxapian-devel = %version
BuildRequires: perl-DBI
BuildRequires: zlib-devel

Requires: xapian-core >= %version

%description
Omega is a CGI application which uses the Xapian Information Retrieval
library to index and search collections of documents.

%prep
%setup
%ifarch %e2k
# unsupported as of lcc 1.23.12
sed -i 's, -fno-gnu-keywords,,' configure*
%endif

%build
%configure
%make_build

%install
%makeinstall_std

# CGI application
mkdir -p %buildroot%_var/www/cgi-bin/
mv %buildroot%_libdir/%name/bin/omega %buildroot%_var/www/cgi-bin

# Create /var directories
mkdir -p %buildroot%_localstatedir/omega/{cdb,data}
mkdir -p %buildroot%_logdir/omega

# Default templates
mkdir -p %buildroot%_localstatedir/omega/templates
cp -a templates/* %buildroot%_localstatedir/omega/templates/

# Images
mkdir -p %buildroot%_var/www/icons/omega
cp -a images/* %buildroot%_var/www/icons/omega/

rm -rf %buildroot%_docdir/%name/

%files
%doc AUTHORS ChangeLog README TODO NEWS docs/*.html
%_bindir/dbi2omega
%_bindir/omindex
%_bindir/omindex-list
%_bindir/scriptindex
%_bindir/htdig2omega
%_bindir/mbox2omega
%_libdir/%name

%dir %_datadir/omega
%_datadir/omega/*.script

%_localstatedir/omega
%_logdir/omega/

%_var/www/cgi-bin/omega
%dir %_var/www/icons/omega
%_var/www/icons/omega/*.png

%config(noreplace) %_sysconfdir/omega.conf
%_man1dir/omindex.1*
%_man1dir/omindex-list.1*
%_man1dir/scriptindex.1*

%changelog
* Sun Feb 05 2023 Vitaly Chikunov <vt@altlinux.org> 1.4.22-alt1
- Update to 1.4.22 (2023-02-02).

* Sun Oct 23 2022 Vitaly Chikunov <vt@altlinux.org> 1.4.21-alt1
- Update to 1.4.21 (2022-09-22).

* Thu Jun 13 2019 Michael Shigorin <mike@altlinux.org> 1.4.5-alt2
- E2K: avoid lcc-unsupported options
- minor spec cleanup

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1
- Updated to latest stable upstream version 1.4.5.

* Fri May 22 2015 Michael Shigorin <mike@altlinux.org> 1.2.21-alt1
- 1.2.21
  + added outlookmsg2html helper

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- NMU: 1.2.3
- dropped xapian-config hack (#22629 fixed long ago)

* Sun Jan 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt2
- add stub xapian-config
- buildreq -bi

* Sun Dec 27 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt1
- initial build for ALT Linux Sisyphus

* Sun Nov 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.17-1mdv2010.1
+ Revision: 469119
- update to new version 1.0.17

* Mon Sep 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.16-1mdv2010.0
+ Revision: 440614
- update to new version 1.0.16

* Mon Aug 31 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.15-1mdv2010.0
+ Revision: 422737
- update to new version 1.0.15

* Thu Jul 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.14-1mdv2010.0
+ Revision: 404778
- update to new version 1.0.14

* Fri Jun 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.13-1mdv2010.0
+ Revision: 387414
- update to new version 1.0.13

* Sat May 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.12-1mdv2010.0
+ Revision: 373733
- update to new version 1.0.12

* Fri May 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.11-1mdv2010.0
+ Revision: 369904
- update to new version 1.0.11

* Sun Dec 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.10-1mdv2009.1
+ Revision: 320544
- update to new version 1.0.10

* Tue Nov 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.9-1mdv2009.1
+ Revision: 299652
- update to new version 1.0.9

* Fri Sep 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.8-1mdv2009.0
+ Revision: 281110
- update to new version 1.0.8

* Fri Jul 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.7-1mdv2009.0
+ Revision: 238093
- update to new version 1.0.7

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.6-1mdv2009.0
+ Revision: 194446
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix no-buildroot-tag

* Thu Dec 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.5-1mdv2008.1
+ Revision: 138526
- set explicit xapian-devel version
- new version
- requires xapian-core

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 1.0.4-2mdv2008.1
+ Revision: 106451
- rebuild for new lzma

* Tue Oct 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.4-1mdv2008.1
+ Revision: 103797
- new version

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 98100
- New version 1.0.3

* Sun Jul 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 49826
- new version

* Tue Jun 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-2mdv2008.0
+ Revision: 41491
- fix group

* Thu Jun 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 39773
- remove useless doc file list

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version

* Tue May 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2008.0
+ Revision: 29744
- Import xapian-omega

