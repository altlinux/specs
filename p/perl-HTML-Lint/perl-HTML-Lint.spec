%define dist HTML-Lint
Name: perl-%dist
Version: 2.06
Release: alt2

Summary: Check for HTML errors in a string or file
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 26 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

%description
HTML::Lint checks a string or file for HTML errors. It comes with
Test::More-style wrapper, Test::HTML::Lint.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/weblint
%perl_vendor_privlib/HTML
%perl_vendor_privlib/Test

%changelog
* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 2.06-alt2
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.04-alt2
- fix directory ownership violation

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.04-alt1
- initial build for ALT Linux Sisyphus
