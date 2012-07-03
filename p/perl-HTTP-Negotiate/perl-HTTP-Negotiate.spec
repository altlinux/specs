%define dist HTTP-Negotiate
Name: perl-%dist
Version: 6.01
Release: alt1

Summary: choose a variant to serve
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-HTTP-Message perl-devel

%description
This module provides a complete implementation of the HTTP content
negotiation algorithm specified in draft-ietf-http-v11-spec-00.ps
chapter 12.  Content negotiation allows for the selection of a preferred
content representation based upon attributes of the negotiable variants
and the value of the various Accept* header fields in the request.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- 6.00 -> 6.01

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
