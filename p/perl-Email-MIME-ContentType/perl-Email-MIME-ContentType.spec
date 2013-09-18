%define _unpackaged_files_terminate_build 1
%define dist Email-MIME-ContentType
Name: perl-%dist
Version: 1.017
Release: alt1

Summary: Parse a MIME Content-Type Header
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Email-MIME-ContentType-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl(Capture/Tiny.pm)

%description
This module is responsible for parsing email content type headers
according to section 5.1 of RFC 2045. It returns a hash as above, with
entries for the discrete type, the composite type, and a hash of
attributes.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email

%changelog
* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.017-alt1
- automated CPAN update

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.015-alt2
- rebuilt as plain src.rpm

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 1.015-alt1
- 1.014 -> 1.015

* Mon Sep 01 2008 Alexey Tourbin <at@altlinux.ru> 1.014-alt1
- 1.01 -> 1.014

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision
