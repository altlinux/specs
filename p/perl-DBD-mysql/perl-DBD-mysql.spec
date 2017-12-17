%define _unpackaged_files_terminate_build 1
%define dist DBD-mysql
Name: perl-%dist
Version: 4.043
Release: alt1.1

Summary: MySQL driver for DBI interface in Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MI/MICHIELB/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libmysqlclient-devel perl-DBI-devel perl-Encode perl-devel perl(Devel/CheckLib.pm)

%description
DBD::mysql is an interface driver for connecting the DBMS independent
Perl-API DBI to the mysql DBMS.

%prep
%setup -q -n %{dist}-%{version}
bzip2 -k Changes

%build
%ifdef _mysql_testdb
export SLOW_TESTS=1
%perl_vendor_build --ssl --nocatchstderr --testdb=%_mysql_testdb
%else
%def_without test
%perl_vendor_build --ssl --nocatchstderr
%endif

%install
%perl_vendor_install

# should not be packaged
rm %buildroot%perl_vendor_archlib/DBD/mysql/INSTALL.pod
rm %buildroot%perl_vendor_archlib/Bundle/DBD/mysql.pm

%files
%doc README* Changes
%perl_vendor_archlib/DBD
%perl_vendor_autolib/DBD

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.043-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 4.043-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.042-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 4.041-alt1.1
- rebuild with new perl 5.24.1

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 4.041-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.039-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.037-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.036-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 4.035-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.033-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 4.033-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 4.032-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 4.031-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 4.029-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 4.028-alt1.1
- rebuild with new perl 5.20.1

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.028-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 4.027-alt1
- automated CPAN update

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 4.026-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 4.025-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.024-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 4.023-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.023-alt1
- automated CPAN update

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.022-alt1.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 4.022-alt1
- 4.020 -> 4.022
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 4.020-alt2
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 4.020-alt1
- 4.018 -> 4.020
- rebuilt as plain src.rpm

* Sun Feb 13 2011 Alexey Tourbin <at@altlinux.ru> 4.018-alt1
- 4.016 -> 4.018

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 4.016-alt1.1
- rebuilt with perl 5.12

* Thu Aug 05 2010 Alexey Tourbin <at@altlinux.ru> 4.016-alt1
- 4.014 -> 4.016

* Sat Apr 17 2010 Alexey Tourbin <at@altlinux.ru> 4.014-alt1
- 4.013 -> 4.014

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 4.013-alt1
- 4.012 -> 4.013

* Fri Jun 19 2009 Alexey Tourbin <at@altlinux.ru> 4.012-alt1
- 4.011 -> 4.012

* Wed Apr 15 2009 Alexey Tourbin <at@altlinux.ru> 4.011-alt1
- 4.010 -> 4.011

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 4.010-alt1
- 4.008 -> 4.010

* Sun Sep 07 2008 Alexey Tourbin <at@altlinux.ru> 4.008-alt1
- 4.007 -> 4.008

* Fri Aug 15 2008 Alexey Tourbin <at@altlinux.ru> 4.007-alt1
- 4.006 -> 4.007

* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 4.006-alt1
- 4.005 -> 4.006

* Wed Jul 04 2007 Alexey Tourbin <at@altlinux.ru> 4.005-alt1
- 4.001 -> 4.005

* Mon Feb 26 2007 Alexey Tourbin <at@altlinux.ru> 4.001-alt1
- 3.0007 -> 4.001
- Msql-Mysql driver emulation code was removed
- also removed Bundle::DBD::mysql

* Sat Sep 09 2006 Alexey Tourbin <at@altlinux.ru> 3.0007-alt1
- 3.0006 -> 3.0007

* Sun Jun 25 2006 Alexey Tourbin <at@altlinux.ru> 3.0006-alt1
- 3.0004 -> 3.0006

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 3.0004-alt1
- 3.0002 -> 3.0004

* Fri Jul 15 2005 Alexey Tourbin <at@altlinux.ru> 3.0002-alt1
- 2.9008 -> 3.0002

* Wed Jun 08 2005 Alexey Tourbin <at@altlinux.ru> 2.90.08-alt1
- 2.9007 -> 2.9008

* Thu Apr 28 2005 Alexey Tourbin <at@altlinux.ru> 2.90.07-alt1
- 2.9006 -> 2.9007

* Wed Apr 06 2005 Alexey Tourbin <at@altlinux.ru> 2.90.06-alt1
- 2.9004 -> 2.9006

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 2.90.04-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Mon Aug 02 2004 Alexey Tourbin <at@altlinux.ru> 2.90.04-alt1
- 2.9003 -> 2.9004

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 2.90.03-alt1
- 2.9003

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 2.90.03-alt0.1
- 2.9003_1
- build against libmysqlclient.so.12

* Sat Jul 05 2003 Alexey Tourbin <at@altlinux.ru> 2.90.02-alt1
- 2.9002 (some changes are significant)

* Thu Mar 06 2003 Alexey Tourbin <at@altlinux.ru> 2.10.26-alt1
- 2.1026
- build without test by default

* Fri Oct 25 2002 Alexey Tourbin <at@altlinux.ru> 2.10.20-alt1
- 2.1020
- rebuilt for perl-5.8 whith new rpm macros

* Thu Mar 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.10.11-alt1
- 2.1011.
- Adopted for Sisyphus.

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.22.15-ipl5mdk
- Rebuilt with new perl again.

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.22.15-ipl4mdk
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Sat Mar 17 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.22.15-ipl3mdk
- Full perlmacroization and a small cleanup
- Added perl in AutoReqProv
- Removed perl-ExtUtils-PerlPP from Requires

* Sat Feb 24 2001 Alexander Bokovoy <ab@avilink.net> 1.22.15-ipl2mdk
- Dependencies changed to follow MySQL libification
- Small typo fixed in Spec file
- Rebuild against MySQL 3.23.33 final

* Fri Dec 29 2000 Alexander Bokovoy <ab@avilink.net> 1.22.15-ipl1mdk
- SPEC file cleaned according IPL policy
- Rebuild against 3.23.29-gamma
- Dependencies fixed

* Tue Nov 14 2000 François Pons <fpons@mandrakesoft.com> 1.22_15-4mdk
- added documentation.
- removed filelist.

* Fri Sep  8 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.22_15-3mdk
- rebuilt with lmysqlclient_r (new implementation in MySQL)
- now requires ExtUtils-PerlPP
- took my template spec to be sure we include all files, including
  /usr/bin/pmysql and Mysql::Statement

* Wed Aug 30 2000 François Pons <fpons@mandrakesoft.com> 1.22_15-2mdk
- created patch to add missing libpthread reference.

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 1.22_15-1mdk
- 1.22_15.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 1.22_14-2mdk
- macroszifications
- add doc.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 1.22_14-1mdk
- 1.22_14.

* Wed May 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.22_11-2mdk
- Fix build for i486

* Tue Apr 04 2000 François Pons <fpons@mandrakesoft.com> 1.22_11-1mdk
- updated to 1.22.11.
- spec file clean.
- use of perl 5.6.0.

* Tue Dec 14 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- finish tidying files so it builds

* Sun Dec 05 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- backdown to 1.19_14 to match MySQL_GPL
- replace i386-linux w/ %%_arch

* Thu Dec 02 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Adapt specfile for Linux-Mandrake

