%define _unpackaged_files_terminate_build 1
%define dist Class-C3
Name: perl-%dist
Version: 0.34
Release: alt1

Summary: A pragma to use the C3 method resolution order algortihm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-MRO-Compat perl-NEXT perl-Sub-Name perl-Test-Pod perl-Test-Pod-Coverage

%description
This is pragma to change Perl 5's standard method resolution
order from depth-first left-to-right (a.k.a - pre-order) to the
more sophisticated C3 method resolution order.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class

%changelog
* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.23-alt2
- rebuilt as plain src.rpm

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.21-alt2
- updated dependencies for Class::C3::XS

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.21-alt1
- 0.21 version

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.19-alt2
- fix directory ownership violation

* Fri May 16 2008 Michael Bochkaryov <misha@altlinux.ru> 0.19-alt1
- 0.19 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.14-alt1
- first build for ALT Linux Sisyphus
