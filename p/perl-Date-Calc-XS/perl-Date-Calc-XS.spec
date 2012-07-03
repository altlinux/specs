%define dist Date-Calc-XS
Name: perl-%dist
Version: 6.2
Release: alt3

Summary: XS wrapper and C library plug-in for Date::Calc
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Thu Nov 10 2011
BuildRequires: perl-Date-Calc perl-devel

# bootstrap: disable build dependency on Date::Calc
#def_disable test

%description
This package provides all sorts of date calculations based on the Gregorian
calendar (the one used in all western countries today).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	CHANGES.txt CREDITS.txt README.txt
%dir	%perl_vendor_archlib/Date
%dir	%perl_vendor_archlib/Date/Calc
	%perl_vendor_archlib/Date/Calc/XS.pm
%doc	%perl_vendor_archlib/Date/Calc/XS.pod
%dir	%perl_vendor_autolib/Date
%dir	%perl_vendor_autolib/Date/Calc
%dir	%perl_vendor_autolib/Date/Calc/XS
	%perl_vendor_autolib/Date/Calc/XS/XS.so

%changelog
* Thu Nov 10 2011 Alexey Tourbin <at@altlinux.ru> 6.2-alt3
- re-enabled build dependency on perl-Date-Calc

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 6.2-alt2
- rebuilt for perl-5.14

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 6.2-alt1.1
- rebuilt for perl-5.12
- disabled build dependency on perl-Date-Calc, for bootstrap

* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 6.2-alt1
- initial revision
