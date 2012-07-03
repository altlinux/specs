%define dist POE-Component-FastCGI
Name: perl-%dist
Version: 0.19
Release: alt1

Summary: POE FastCGI server
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-CGI perl-POE perl-devel

%description
This module provides an interface between the FastCGI protocol
and POE. This means that it is possible to effectively proxy a
POE server behind a webserver that supports FastCGI.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_privlib/POE

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.18 -> 0.19

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.1
- NMU for unknown reason

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 0.1-alt1
- first build for ALT Linux Sisyphus
