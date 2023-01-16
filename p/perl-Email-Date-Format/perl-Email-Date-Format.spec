%define _unpackaged_files_terminate_build 1
%define dist Email-Date-Format
Name: perl-%dist
Version: 1.008
Release: alt1

Summary: Produce RFC 2822 date strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Test-Pod perl(Capture/Tiny.pm)

%description
This module provides a simple means for generating an RFC 2822 compliant
datetime string.  (In case you care, they're not RFC 822 dates, because
they use a four digit year, which is not allowed in RFC 822.)

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email

%changelog
* Mon Jan 16 2023 Igor Vlasenko <viy@altlinux.org> 1.008-alt1
- automated CPAN update

* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.007-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 1.006-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1
- automated CPAN update

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.002-alt2
- rebuilt

* Tue Jun 17 2008 Alexey Tourbin <at@altlinux.ru> 1.002-alt1
- initial revision (for new MIME::Lite)
