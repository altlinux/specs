%define _unpackaged_files_terminate_build 1
%add_findreq_skiplist %perl_vendor_archlib/MongoDB/BulkWrite.pm
%add_findreq_skiplist %perl_vendor_archlib/MongoDB/Collection.pm
%define dist MongoDB
Name: perl-%dist
Version: 1.8.0
Release: alt1.1

Summary: Mongo Driver for Perl
License: GPL or Artistic
Group: Development/Perl

URL: http://www.cpan.org
Source0: http://www.cpan.org/authors/id/M/MO/MONGODB/%{dist}-v%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011 (-bb)
BuildRequires: perl-Any-Moose perl-Class-Method-Modifiers perl-Data-Types perl-DateTime perl-File-Slurp perl-JSON perl-Module-Install perl-Moose perl-Package-Stash-XS perl-Readonly perl-Readonly-XS perl-Test-Exception perl-Tie-IxHash perl-boolean perl(Config/AutoConf.pm) perl(Path/Tiny.pm) perl(Throwable.pm) perl(Syntax/Keyword/Junction.pm) perl(Safe/Isa.pm) perl(DateTime/Locale.pm) perl(Authen/SCRAM/Client.pm) perl(Digest/SHA.pm) perl(BSON/Decimal128.pm)

%description
This is the Perl driver for MongoDB, a document-oriented database.

%prep
%setup -q -n %{dist}-v%{version}

# need database connection
%def_without test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README CONTRIBUTING.md INSTALL.md README.md
%perl_vendor_archlib/MongoDB*
%perl_vendor_autolib/MongoDB

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.5-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- automated CPAN update

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1
- automated CPAN update

* Sun Oct 18 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.708.1.0-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.708.0.0-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.707.2.0-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.707.1.0-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.705.0.0-alt2.1
- rebuild with new perl 5.20.1

* Sun Dec 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.705.0.0-alt2
- fixed build

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.705.0.0-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.704.5.0-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.704.4.0-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.704.2.0-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.704.1.0-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.702.2-alt1
- 0.702.0 -> 0.702.2

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.702.0-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.701.4-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.501.1-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

* Sat Jan 01 2011 Denis Smirnov <mithraen@altlinux.ru> 0.40-alt1
- initial build for ALT Linux Sisyphus
