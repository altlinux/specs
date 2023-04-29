%define _unpackaged_files_terminate_build 1
%define dist Pod-Parser
Name: perl-%dist
Version: 1.66
Release: alt1

Summary: Modules for parsing/translating POD format documents
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MAREKR/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-IO-String perl-devel perl-podlators perl(Pod/Checker.pm)

# for compatibility: about 40 packages used to have indirect
# dependency on perl-podlators through Pod-Parser
Requires: perl-podlators

%description
B<Pod::Find> provides a set of functions to locate POD files.  Note that
no function is exported by default to avoid pollution of your namespace,
so be sure to specify them in the B<use> statement if you need them:

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* CHANGES
%_bindir/pod*
%_man1dir/*
%perl_vendor_privlib/Pod

%changelog
* Sat Apr 29 2023 Igor Vlasenko <viy@altlinux.org> 1.66-alt1
- automated CPAN update

* Mon May 23 2022 Igor Vlasenko <viy@altlinux.org> 1.65-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.63-alt1
- automated CPAN update

* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1
- automated CPAN update

* Wed Oct 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.61-alt2
- added Requires: perl-podlators for compatibility:
  about 40 packages have indirect build dependency
  on perl-podlators through Pod-Parser

* Sun Oct 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.61-alt1
- automated CPAN update

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 1.51-alt1
- 1.38 -> 1.51

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.38-alt1
- initial revision, for perl-5.12
