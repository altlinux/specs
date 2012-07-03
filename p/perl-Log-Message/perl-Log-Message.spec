%define dist Log-Message
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: A generic message logging mechanism
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Module-Load perl-Params-Check perl-devel

%description
This module enables you to do generic message logging throughout programs
and projects.  Every message will be logged with stacktraces, timestamps
and so on.  You can use built-in handlers immediately, or after the fact
when you inspect the error stack.  It is highly configurable and let's you
even provide your own handlers for dealing with messages.

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
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- 0.02 -> 0.04

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.01-alt2
- fix directory ownership violation

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus
