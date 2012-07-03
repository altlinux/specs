%define dist Class-StateMachine
Name: perl-%dist
Version: 0.18
Release: alt1

Summary: Define classes for state machines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 27 2011 (-bi)
BuildRequires: perl-MRO-Define perl-Package-Stash perl-Sub-Name perl-devel perl-parent

%description
Class::StateMachine lets define, via the "OnState" attribute, methods
that are dispatched depending on an internal "state" property.

%prep
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class

%changelog
* Thu Oct 27 2011 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- 0.12 -> 0.18

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 0.12-alt1
- first build for ALT Linux Sisyphus

