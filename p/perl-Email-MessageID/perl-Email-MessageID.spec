%define dist Email-MessageID
Name: perl-%dist
Version: 1.402
Release: alt1

Summary: Generate world unique message-ids
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Email-MessageID-1.402.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 28 2010
BuildRequires: perl-Email-Address perl-Test-Pod perl-Test-Pod-Coverage

%description
Message-ids are optional, but highly recommended, headers that identify
a message uniquely. This software generates a unique message-id.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.402-alt1
- automated CPAN update

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.401-alt1
- 1.35 -> 1.401

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- initial revision
