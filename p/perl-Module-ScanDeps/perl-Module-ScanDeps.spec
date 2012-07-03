%define dist Module-ScanDeps
Name: perl-%dist
Version: 1.05
Release: alt1

Summary: Recursively scan Perl programs for dependencies
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Module-Build perl-Module-Pluggable perl-Term-Cap perl-Test-Pod perl-parent perl-threads perl-unicore

%description
An application of Module::ScanDeps is to generate executables from
scripts that contains necessary modules; this module supports two
such projects, PAR and App::Packer.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS Changes README
%_bindir/scandeps.pl
%perl_vendor_privlib/Module

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.04 -> 1.05
- disabled build dependency on perl-Module-Install

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 0.96 -> 1.04

* Mon Apr 05 2010 Alexey Tourbin <at@altlinux.ru> 0.96-alt1
- 0.89 -> 0.96

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 0.89-alt1
- 0.83 -> 0.89

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 0.83-alt1
- 0.51 -> 0.83

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 0.51-alt1
- initial revision
