## SPEC file for Perl module Finance::Currency::Convert::Yahoo

%define version    0.2
%define release    alt2

Name: perl-Finance-Currency-Convert-Yahoo
Version: %version
Release: alt2.1

Summary: Perl module to convert currencies using Yahoo
Summary(ru_RU.UTF-8): модуль Perl для преобразования валют с использованием Yahoo

License: GPL or Artistic
Group: Development/Perl

%define real_name Finance-Currency-Convert-Yahoo
%define real_version 0.2
URL: http://search.cpan.org/~lgoddard/Finance-Currency-Convert-Yahoo/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://search.cpan.org/CPAN/authors/id/L/LG/LGODDARD/%real_name-%real_version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel perl-libwww

%description
Perl module Finance::Currency::Convert::Yahoo converts a sum between two 
currencies using data from Finance.Yahoo.com.

%description -l ru_RU.UTF-8
Модуль Perl  Finance::Currency::Convert::Yahoo преобразует сумму из одной 
валюты в другую, используя курсы валют с Finance.Yahoo.com.

%prep
%setup -q -n %real_name-%real_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES
%exclude /.perl.req
%dir %perl_vendor_privlib/Finance
%dir %perl_vendor_privlib/Finance/Currency
%dir %perl_vendor_privlib/Finance/Currency/Convert
     %perl_vendor_privlib/Finance/Currency/Convert/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.2-alt2
- Fix typo in package summary

* Tue Mar 20 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.2-alt1
- Initial build for ALT Linux Sisyphus

* Mon Mar 19 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.2-alt0
- Initial build
