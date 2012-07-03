%define module Mail-DomainKeys

Name: perl-%module
Version: 1.0
Release: alt1.1

Summary: A perl implementation of DomainKeys
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/%module/
Source: http://www.cpan.org/modules/by-module/Mail/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Dec 15 2006
BuildRequires: perl-Crypt-OpenSSL-RSA perl-devel perl-MailTools perl-Net-DNS

%description
Mail::DomainKeys is a perl implementation of Yahoo's mail signature protocol.

This library allows one to sign and verify signatures as per per draft 03 of
the DomainKeys specification.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot/.perl.req
rm -rf %buildroot%perl_vendor_archlib

%files
%doc README THANKS
%perl_vendor_privlib/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- 1.0

* Fri Dec 15 2006 Victor Forsyuk <force@altlinux.org> 0.88-alt1
- 0.88

* Wed Sep 06 2006 Victor Forsyuk <force@altlinux.ru> 0.86-alt1
- 0.86

* Tue Nov 15 2005 Victor Forsyuk <force@altlinux.ru> 0.80-alt1
- Initial build.
