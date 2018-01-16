%define _unpackaged_files_terminate_build 1
%define dist HTML-Lint
Name: perl-%dist
Version: 2.30
Release: alt1

Summary: Check for HTML errors in a string or file
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PE/PETDANCE/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 26 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

%description
HTML::Lint checks a string or file for HTML errors. It comes with
Test::More-style wrapper, Test::HTML::Lint.

%prep
%setup -q -n %{dist}-%{version}
# https://rt.cpan.org/Ticket/Display.html?id=108007
[ %version == 2.22 ] && rm t/12-html_fragment_ok.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%_bindir/weblint
%perl_vendor_privlib/HTML
%perl_vendor_privlib/Test

%changelog
* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.30-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.26-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1
- automated CPAN update

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
