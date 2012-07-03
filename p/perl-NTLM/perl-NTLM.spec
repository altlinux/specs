%define module NTLM

Name: perl-%module
Version: 1.09
Release: alt1

Summary: An NTLM authentication Perl module
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/N/NB/NBEBOUT/NTLM-1.09.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 10 2011
BuildRequires: perl-Digest-HMAC perl-Test-Pod

%description
This module implements the NTLM authentication mechanism. It can be used to
perform NTLM style authentication for any desired protocol.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Authen

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 1.08-alt1
- 1.08

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jun 19 2008 Victor Forsyuk <force@altlinux.org> 1.05-alt1
- 1.05

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 1.04-alt1
- 1.04, implemented NTLMv2.

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 1.03-alt1
- Initial build.
