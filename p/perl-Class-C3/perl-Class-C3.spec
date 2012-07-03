%define dist Class-C3
Name: perl-%dist
Version: 0.23
Release: alt2

Summary: A pragma to use the C3 method resolution order algortihm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-MRO-Compat perl-NEXT perl-Sub-Name perl-Test-Pod perl-Test-Pod-Coverage

%description
This is pragma to change Perl 5's standard method resolution
order from depth-first left-to-right (a.k.a - pre-order) to the
more sophisticated C3 method resolution order.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Class

%changelog
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
