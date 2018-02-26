%define dist Object-Accessor
Name: perl-%dist
Version: 0.42
Release: alt1

Summary: Per object accessors
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Object-Accessor-0.42.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-Params-Check perl-devel

%description
Object::Accessor provides an interface to create per object accessors (as
opposed to per Class accessors, as, for example, Class::Accessor provides).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Object

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 0.38-alt1
- 0.36 -> 0.38

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt2
- fix directory ownership violation

* Fri Jun 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt1
- new version 0.34 (with rpmrb script)
- update buildreqs

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus
