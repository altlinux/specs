%define module Net-SMTP_auth

Name: perl-%module
Version: 0.08
Release: alt2.1

Summary: SMTP_AUTH wrapper for Net::SMTP (rfc2554)
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Net/%module-%version.tar.gz

BuildArch: noarch
# Automatically added by buildreq on Fri Jul 27 2007
BuildRequires: perl-Authen-SASL perl-devel perl-libnet

%description
This module implements a client interface to the SMTP and ESMTP protocol AUTH
service extension, enabling a perl5 application to talk to and authenticate
against SMTP servers.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Net
%exclude /.perl.req

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 27 2007 Victor Forsyuk <force@altlinux.org> 0.08-alt2
- Spec cleanups.

* Tue Jun 06 2006 Andrei Bulava <abulava@altlinux.ru> 0.08-alt1
- first build for ALT Linux Sisyphus
