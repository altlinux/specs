%define dist Log-Message-Simple
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: Simplified interface to Log::Message
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Log-Message perl-devel

%description
This module is a simplified frontend to Log::Message, offering
most common use for logging, and easy access to the stack (in
both raw and pretty-printable form).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Log

%changelog
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- 0.06 -> 0.08

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt2
- fix directory ownership violation

* Fri Jun 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus

