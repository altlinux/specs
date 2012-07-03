%define dist Config-Any
Name: perl-Config-Any
Version: 0.23
Release: alt1

Summary: Load configuration from different file formats, transparently
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/Config-Any/
Source: http://www.cpan.org/authors/id/B/BR/BRICAS/Config-Any-0.23.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 29 2010 (-bi)
BuildRequires: perl-Config-Any perl-JSON-DWIW perl-Module-Install perl-Test-Pod perl-Test-Pod-Coverage perl-YAML-Syck

%description
Config::Any provides a facility for Perl applications and
libraries to load configuration data from multiple different
file formats. It supports XML, YAML, JSON, Apache-style
configuration, Windows INI files, and even Perl code.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Config*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Wed Dec 29 2010 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- 0.19 -> 0.20

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.12 -> 0.19

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Tue Jul 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.12-alt1
- 0.12 version build
  + allow loaders to return multiple documents as an array
  + use from_json() if JSON version 2.x is available
  + code and pod cleanups
- spec file cleanup
- buildreq update

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.07-alt1
- first build for ALT Linux Sisyphus
