%define _unpackaged_files_terminate_build 1
%define dist DBD-Pg
Name: perl-%dist
Version: 3.7.0
Release: alt2

Summary: PostgreSQL database driver for the DBI module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/T/TU/TURNSTEP/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: net-tools perl-DBI-devel perl-Encode perl-Test-Warn postgresql-devel postgresql10-server perl(charnames.pm)

%description
DBD::Pg is an interface driver for connecting the DBMS independent
Perl-API DBI to the PostgreSQL DBMS.

%prep
%setup -q -n %{dist}-%{version}

%build
POSTGRES_INCLUDE=`pg_config --includedir`
POSTGRES_LIB=`pg_config --libdir`
export POSTGRES_INCLUDE POSTGRES_LIB
%perl_vendor_build

%install
%perl_vendor_install

# should not be packaged
rm %buildroot%perl_vendor_archlib/Bundle/DBD/Pg.pm

%files
%doc Changes README README.dev README.win32
%perl_vendor_archlib/DBD
%perl_vendor_autolib/DBD

%changelog
* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 3.7.0-alt2
- fix buildreq

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 3.7.0-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.4.2-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.4.2-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 2.19.3-alt2
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 2.19.3-alt1
- 2.18.1 -> 2.19.3
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.18.1-alt2
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.18.1-alt1
- 2.17.2 -> 2.18.1
- rebuilt as plain src.rpm

* Sun Feb 13 2011 Alexey Tourbin <at@altlinux.ru> 2.17.2-alt1
- 2.17.1 -> 2.17.2

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 2.17.1-alt1
- 2.17.0 -> 2.17.1
- built for perl-5.12

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 2.17.0-alt1
- 2.16.1 -> 2.17.0

* Sat Mar 20 2010 Alexey Tourbin <at@altlinux.ru> 2.16.1-alt1
- 2.15.1 -> 2.16.1

* Sun Aug 09 2009 Alexey Tourbin <at@altlinux.ru> 2.15.1-alt1
- 2.14.0 -> 2.15.1

* Tue Jul 28 2009 Alexey Tourbin <at@altlinux.ru> 2.14.0-alt1
- 2.13.1 -> 2.14.0

* Mon May 11 2009 Alexey Tourbin <at@altlinux.ru> 2.13.1-alt1
- 2.13.0 -> 2.13.1

* Wed Apr 15 2009 Alexey Tourbin <at@altlinux.ru> 2.13.0-alt1
- 2.12.0 -> 2.13.0

* Sun Mar 29 2009 Alexey Tourbin <at@altlinux.ru> 2.12.0-alt1
- 2.11.7 -> 2.12.0

* Sat Dec 20 2008 Alexey Tourbin <at@altlinux.ru> 2.11.7-alt1
- 2.11.5 -> 2.11.7

* Wed Nov 26 2008 Alexey Tourbin <at@altlinux.ru> 2.11.5-alt1
- 2.11.2 -> 2.11.5

* Sun Oct 19 2008 Alexey Tourbin <at@altlinux.ru> 2.11.2-alt1
- 2.10.6 -> 2.11.2

* Sun Sep 21 2008 Alexey Tourbin <at@altlinux.ru> 2.10.6-alt1
- 2.10.3 -> 2.10.6

* Sun Sep 07 2008 Alexey Tourbin <at@altlinux.ru> 2.10.3-alt1
- 2.9.0 -> 2.10.3

* Fri Aug 15 2008 Alexey Tourbin <at@altlinux.ru> 2.9.0-alt1
- 2.8.1 -> 2.9.0

* Tue Jun 17 2008 Alexey Tourbin <at@altlinux.ru> 2.8.1-alt1
- 2.7.2 -> 2.8.1

* Thu May 15 2008 Alexey Tourbin <at@altlinux.ru> 2.7.2-alt1
- 2.6.4 -> 2.7.2

* Sun May 04 2008 Alexey Tourbin <at@altlinux.ru> 2.6.4-alt1
- 2.6.1 -> 2.6.4

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 2.6.1-alt1
- 2.2.2 -> 2.6.1

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 2.2.2-alt1
- 2.2.0 -> 2.2.2

* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 2.2.0-alt1
- 1.49 -> 2.2.0
- fixed a few bugs in C code (rt.cpan.org #33737 #33738 #33743)

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.49-alt1.0
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 1.49-alt1
- 1.48 -> 1.49

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 1.48-alt1
- 1.43 -> 1.48
- is_high_bit_set.patch merged upstream (cpan #13406)

* Wed Jun 29 2005 Alexey Tourbin <at@altlinux.ru> 1.43-alt2
- dbdimp.c: fixed is_high_bit_set() loop condition (cpan #13406)

* Fri Jun 24 2005 Alexey Tourbin <at@altlinux.ru> 1.43-alt1
- 1.42 -> 1.43

* Sun May 22 2005 Alexey Tourbin <at@altlinux.ru> 1.42-alt1
- 1.41 -> 1.42
- built against libpq4/postgresql8.0

* Fri Apr 08 2005 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.40 -> 1.41

* Thu Mar 03 2005 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- 1.32 -> 1.40
- alt-CLONE.patch merged upstream (Andrew Fediushin, #5403, cpan #11365)

* Thu Feb 03 2005 Alexey Tourbin <at@altlinux.ru> 1.32-alt3
- added CLONE method for use with threads (Andrew Fediushin, #5403, cpan #11365)

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1.32-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Thu Feb 26 2004 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- 1.32; autodetect.patch and type_info.patch needed no more

* Sat Feb 07 2004 Alexey Tourbin <at@altlinux.ru> 1.31-alt3
- type_info.patch: fixes segfault (Sir Raorn, #3408)

* Fri Dec 19 2003 Alexey Tourbin <at@altlinux.ru> 1.31-alt2
- fixed PostgreSQL-7.4 autodetection

* Wed Nov 19 2003 Alexey Tourbin <at@altlinux.ru> 1.31-alt1
- 1.31

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 1.21-alt1
- 1.21

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.13-alt2
- rebuild with new perl

* Tue May 28 2002 Grigory Milev <week@altlinux.ru> 1.13-alt1
- new version released

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.01-alt2
- Rebuilt for new perl.

* Tue Jul 10 2001 Grigory Milev <week@altlinux.ru> 1.01-alt1
- new version (1.01)

* Fri Jun 22 2001 Grigory Milev <week@altlinux.ru> 1.00-alt2
- Fix provides
- Spec rewritten for compatibility with new policy

* Thu Jun 21 2001 Sergey Bolshakov <s.bolshakov@belcaf.com>
- First spec file for ALT Linux distribution.
