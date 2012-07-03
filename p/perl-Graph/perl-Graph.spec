%define module Graph

Name: perl-Graph
Version: 0.94
Release: alt2.1

Summary: Graph - Perl module for dealing with graphs
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/J/JH/JHI/Graph-%version.tar.gz

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Mon Aug 09 2010
BuildRequires: perl-Storable perl-Test-Pod perl-Test-Pod-Coverage
BuildRequires: perl-Math-Complex

%description
Perl module for dealing with graphs, the abstract data structures.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Aug 09 2010 Victor Forsiuk <force@altlinux.org> 0.94-alt2
- Fix FTBFS by updating BuildRequires.

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Apr 21 2008 Michael Bochkaryov <misha@altlinux.ru> 0.84-alt1
- first build for ALT Linux Sisyphus

