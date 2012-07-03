%define dist Email-Date-Format
Name: perl-%dist
Version: 1.002
Release: alt2

Summary: Produce RFC 2822 date strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Test-Pod

%description
This module provides a simple means for generating an RFC 2822 compliant
datetime string.  (In case you care, they're not RFC 822 dates, because
they use a four digit year, which is not allowed in RFC 822.)

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
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.002-alt2
- rebuilt

* Tue Jun 17 2008 Alexey Tourbin <at@altlinux.ru> 1.002-alt1
- initial revision (for new MIME::Lite)
