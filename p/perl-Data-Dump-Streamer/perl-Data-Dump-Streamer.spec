%define _unpackaged_files_terminate_build 1
%define dist Data-Dump-Streamer
Name: perl-%dist
Version: 2.40
Release: alt1.1.1

Summary: Accurately serialize a data structure as Perl code
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/Y/YV/YVES/Data-Dump-Streamer-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Algorithm-Diff perl-B-Utils perl-IO-Compress perl-Module-Build perl-PadWalker perl-Text-Balanced

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects.  The contents of each
variable is output using the least number of Perl statements as convenient,
usually only one.  Self-referential structures, closures, and objects are
output correctly.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README*
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.40-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.40-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.40-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.39-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.38-alt2.1
- rebuild with new perl 5.22.0

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.38-alt2
- quick hack for new perl 5.22

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.38-alt1.1
- rebuild with new perl 5.20.1

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.38-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.37-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.36-alt2
- built for perl 5.18

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.36-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 2.34-alt1
- 2.32 -> 2.34
- built for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 2.32-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.22-alt1.1
- rebuilt with perl 5.12

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Sun Jan 11 2009 Vitaly Lipatov <lav@altlinux.ru> 2.08.40-alt1
- initial build for ALT Linux Sisyphus

