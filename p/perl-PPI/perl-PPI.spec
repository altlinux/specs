%define dist PPI
Name: perl-%dist
Version: 1.215
Release: alt2

Summary: Parse, Analyze and Manipulate Perl (without perl)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# optional, experimental
%add_findreq_skiplist */PPI/XSAccessor.pm

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Class-Inspector perl-Clone perl-File-Remove perl-IO-String perl-List-MoreUtils perl-Params-Util perl-Pod-Escapes perl-Task-Weaken perl-Test-NoWarnings perl-Test-Object perl-Test-SubCalls

%description
PPI is an acronym for the longer original module name
Parse::Perl::Isolated. And in the spirit or the silly acronym games
played by certain unnamed Open Source projects you may have heard of,
it's also a reverse acronym for "I Parse Perl".

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/PPI*

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.215-alt2
- disabled build dependency on perl-Module-Install

* Wed Mar 23 2011 Alexey Tourbin <at@altlinux.ru> 1.215-alt1
- 1.213 -> 1.215

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.213-alt1
- 1.212 -> 1.213

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 1.212-alt1
- 1.210 -> 1.212

* Thu Mar 18 2010 Alexey Tourbin <at@altlinux.ru> 1.210-alt1
- 1.203 -> 1.210

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 1.203-alt1
- 1.202_01 -> 1.203

* Sat Apr 12 2008 Alexey Tourbin <at@altlinux.ru> 1.202_01-alt1
- 1.118 -> 1.202_01

* Sun Jun 17 2007 Alexey Tourbin <at@altlinux.ru> 1.118-alt1
- 1.003 -> 1.118 (closes #11720)

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 1.003-alt1
- initial revision
