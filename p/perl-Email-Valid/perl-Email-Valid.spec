%define dist Email-Valid
Name: perl-%dist
Version: 0.185
Release: alt1

Summary: Check validity of Internet email addresses 
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Email-Valid-0.182-alt-req.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-MailTools perl-Net-DNS perl-Net-Domain-TLD perl-Test-Pod perl-Test-Pod-Coverage

%description
This module determines whether an email address is well-formed,
and optionally, whether a mail host exists for the domain.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.185-alt1
- 0.184 -> 0.185

* Tue Aug 09 2011 Alexey Tourbin <at@altlinux.ru> 0.184-alt2
- fixed test suite for build environment without networking

* Tue Jul 06 2010 Alexey Tourbin <at@altlinux.ru> 0.184-alt1
- 0.182 -> 0.184

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 0.182-alt1
- 0.176 -> 0.182

* Fri Aug 11 2006 Alexey Tourbin <at@altlinux.ru> 0.176-alt1
- 0.15 -> 0.176

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.15-alt1.1                           
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Aug 30 2004 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- initial revision (this module is needed for otrs)
