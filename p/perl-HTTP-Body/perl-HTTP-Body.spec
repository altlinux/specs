%define module HTTP-Body

Name: perl-%module
Version: 1.12
Release: alt1

Summary: %module - HTTP Body Parser
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/G/GE/GETTY/HTTP-Body-1.12.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Mar 17 2010
BuildRequires: perl-Module-Install perl-Test-Deep perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

%description
HTTP Body Parser.

%prep
%setup -n %module-%version

%build
export TEST_POD=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTTP

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Mar 17 2010 Victor Forsiuk <force@altlinux.org> 1.07-alt1
- 1.07

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Apr 23 2008 Michael Bochkaryov <misha@altlinux.ru> 1.03-alt1
- updated to 1.03 version

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 0.6-alt1
- first build for ALT Linux Sisyphus

