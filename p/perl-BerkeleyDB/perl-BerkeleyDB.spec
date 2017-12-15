BuildRequires: perl-podlators
%define _unpackaged_files_terminate_build 1
%define dist BerkeleyDB
Name: perl-%dist
Version: 0.55
Release: alt1.3.1

Summary: Perl bindings to Berkeley DB version 2.x and greater
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/P/PM/PMQS/BerkeleyDB-%{version}.tar.gz
Patch: perl-BerkeleyDB-0.49-alt-DB_VERSION.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libdb4-devel perl-MLDBM perl-Test-Pod perl-unicore

%description
BerkeleyDB is a module which allows Perl programs to make use
of the facilities provided by Berkeley DB version 2 or 3.
(Note: if you want to use version 1 of Berkeley DB with Perl
you need the DB_File module).

Berkeley DB is a C library which provides a consistent interface
to a number of database formats. BerkeleyDB provides an interface
to all four of the database types (hash, btree, queue and recno)
currently supported by Berkeley DB.

%prep
%setup -q -n %dist-%version
%patch -p1
rm -rv t/Test/

%build
%perl_vendor_build

%install
%perl_vendor_install

rm %buildroot%perl_vendor_archlib/mkconsts.pl
rm %buildroot%perl_vendor_archlib/scan.pl

%files
%doc	Changes README
	%perl_vendor_archlib/BerkeleyDB.pm
%doc	%perl_vendor_archlib/BerkeleyDB.pod
	%perl_vendor_archlib/BerkeleyDB
	%perl_vendor_autolib/BerkeleyDB

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1.3.1
- rebuild with new perl 5.26.1

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1.3
- enabled test

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1.2
- rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1.1.1
- disabled test in preparation for new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1.1
- rebuild with new perl 5.22.0

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1.1
- rebuild with new perl 5.20.1

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.53-alt1
- 0.52 -> 0.53

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.51-alt1
- 0.49 -> 0.51
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.49-alt2
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.49-alt1
- 0.43 -> 0.49
- rebuilt as plain src.rpm

* Thu Dec 23 2010 Alexey Tourbin <at@altlinux.ru> 0.43-alt1
- 0.42 -> 0.43

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.42-alt1.1
- rebuilt for perl-5.12

* Mon Apr 05 2010 Alexey Tourbin <at@altlinux.ru> 0.42-alt1
- 0.39 -> 0.42

* Fri Jun 12 2009 Alexey Tourbin <at@altlinux.ru> 0.39-alt1
- 0.38 -> 0.39

* Sun Apr 05 2009 Alexey Tourbin <at@altlinux.ru> 0.38-alt1
- 0.36 -> 0.38

* Fri Oct 03 2008 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- 0.35 -> 0.36

* Thu Sep 25 2008 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- 0.34 -> 0.35

* Wed Aug 06 2008 Alexey Tourbin <at@altlinux.ru> 0.34-alt1
- 0.33 -> 0.34
- built with libdb4.7

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.32 -> 0.33

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.32-alt1
- 0.31 -> 0.32

* Wed Dec 20 2006 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.30 -> 0.31
- fix DB_ENV() return value (cpan #22588)

* Fri Oct 06 2006 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- 0.29 -> 0.30
- imported source into git and built with gear

* Tue Jul 04 2006 Alexey Tourbin <at@altlinux.ru> 0.29-alt1
- 0.28 -> 0.29

* Tue Jun 13 2006 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- 0.27 -> 0.28

* Mon May 15 2006 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- 0.26 -> 0.27

* Sun Mar 20 2005 Alexey Tourbin <at@altlinux.ru> 0.26-alt2
- deb-db_version.patch: work with all patchlevels of libdb

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.26-alt1.1
- Updated libdb4 build dependencies.
- Rebuilt with libdb4.3.

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 0.26-alt1
- 0.25 -> 0.26
- manual pages not packaged (use perldoc)

* Fri Feb 13 2004 Alexey Tourbin <at@altlinux.ru> 0.25-alt2
- rebuilt against libdb4.2

* Sun Nov 16 2003 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.25: a bug fixed as I reported (test suite was broken with perl-5.8.1;
  it does not apply to perl-5.8.2, though)
- test base extended (BuildRequires: perl-MLDBM)

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 0.24-alt1
- 0.24

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 0.23-alt2
- build explicitly with libdb4.0

* Thu Jun 26 2003 Stanislav Ievlev <inger@altlinux.ru> 0.23-alt1
- 0.23

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.20-alt1
- rebuild with new perl

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 0.18-alt1
- 0.18
- Build with db4

* Thu Sep 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.16-alt1
- Initial revision.
