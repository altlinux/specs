Name: perl-Socket-Netlink
Version: 0.05
Release: alt1.1.1

Summary: interface to Linux's PF_NETLINK socket family
Group: Development/Perl
License: perl

Url: %CPAN Socket-Netlink
Source: %name-%version.tar

BuildRequires: perl(Test/HexString.pm) perl(Module/Build/Compat.pm) perl(ExtUtils/CChecker.pm) perl-devel perl(Module/Build.pm) perl(ExtUtils/H2PM.pm) perl(ExtUtils/CBuilder.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Socket/Netlink*
%perl_vendor_archlib/Socket/Netlink*
%perl_vendor_archlib/IO/Socket/Netlink*
%doc Changes LICENSE README

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1
- rebuild with new perl 5.24.1

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1
- rebuild with new perl 5.20.1

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build for ALTLinux

