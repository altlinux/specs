%define _unpackaged_files_terminate_build 1
%define dist Sub-Name
Name: perl-%dist
Version: 0.21
Release: alt1.1.1
Epoch: 1

Summary: (re)name a sub
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/Sub-Name-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel perl(Devel/CheckBin.pm) perl(Module/Metadata.pm)

%description
subname NAME, CODEREF
Assigns a new name to referenced sub.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Sub
%perl_vendor_autolib/Sub

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.21-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.21-alt1.1
- rebuild with new perl 5.24.1

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.21-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.19-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.15-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.14-alt1.1
- rebuild with new perl 5.22.0

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.14-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.13-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.12-alt1.1
- rebuild with new perl 5.20.1

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.12-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.09-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1:0.05-alt5
- built for perl 5.18

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1:0.05-alt4
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1:0.05-alt3
- rebuilt for perl-5.14

* Fri Nov 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1:0.05-alt2
- new release

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1:0.05-alt1
- 0.04 -> 0.05
- built for perl-5.12

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.4-alt1
- 0.4 version

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- NMU fixing directory ownership violation

* Sun Apr 20 2008 Michael Bochkaryov <misha@altlinux.ru> 0.03-alt1
- updated to 0.03 version
- docs added to package

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.02-alt1
- first build for ALT Linux Sisyphus

