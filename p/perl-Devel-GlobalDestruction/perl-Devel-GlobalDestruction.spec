%define dist Devel-GlobalDestruction
Name: perl-%dist
Version: 0.04
Release: alt2

Summary: Expose the flag which marks global destruction
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# New global variable ${^GLOBAL_PHASE}
Requires: perl-base >= 1:5.14
BuildRequires: perl-base >= 1:5.14

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Sub-Exporter perl-devel

%description
Perl's global destruction is a little tricky to deal with WRT finalizers
because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happenning you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if global
destruction is in effect.

%prep
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Devel

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.14
- now noarch

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt2.1
- rebuilt with perl 5.12

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.02-alt2
- fixed directory packaging

* Mon Oct 20 2008 Mikhail Pokidko <pma@altlinux.org> 0.02-alt1
- initial build for ALT Linux Sisyphus

