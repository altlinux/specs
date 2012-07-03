# SPEC file for building Perl module Crypt::TripleDES

%define real_name Crypt-TripleDES
%define version 0.24
%define release alt2

Name: perl-Crypt-TripleDES
Version: %version
Release: alt2.1

Summary: Perl module Crypt-TripleDES implements 3DES encryption
Summary(ru_RU.UTF-8): модуль Perl для реализации шифрования по алгоритму 3DES

License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/~vipul/Crypt-TripleDES/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

BuildArch: noarch

Source: %real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel

%description
This module implements 3DES encryption in ECB mode. The code is 
based on Eric Young's implementation of DES in pure perl.  It's 
quite slow because of the way  Perl handles bit operations  and 
is not recommended for use with large texts.

%description -l ru_RU.UTF-8
Данный модуль реализует алгоритм шифрования 3DES в режиме ECB. 
Код модуля  основан на реализации  DES  Eric Young'а на чистом 
Perl.  Код  весьма медленный  из-за способа  поддержки битовых 
операций в Perl и не рекомендован для использования с большими 
текстами.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc examples/deswrapper
%perl_vendor_privlib/Crypt/*.pm

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Sep 22 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.24-alt2
- Fix file list in spec

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.24-alt1
- Initial build for ALT Linux

* Tue Apr 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.24-alt0
- Initial build




