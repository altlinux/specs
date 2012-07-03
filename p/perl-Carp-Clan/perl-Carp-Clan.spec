%define dist Carp-Clan
Name: perl-%dist
Version: 6.04
Release: alt2

Summary: Report errors from perspective of caller of a "clan" of modules
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# previous Bit::Vector had Carp::Clan
Conflicts: perl-Bit-Vector < 6.4

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Test-Exception

%description
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself. But instead of giving
it a number of levels to skip on the calling stack, you give it a
pattern to characterize the package names of the "clan" of modules
which shall never be blamed for any error.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
%dir	%perl_vendor_privlib/Carp
	%perl_vendor_privlib/Carp/Clan.pm
%doc	%perl_vendor_privlib/Carp/Clan.pod

%changelog
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 6.04-alt2
- rebuilt as plain src.rpm

* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 6.04-alt1
- 6.03 -> 6.04

* Tue Oct 20 2009 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.00 -> 6.03

* Sun Sep 14 2008 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- 5.8 -> 6.00

* Fri Oct 13 2006 Alexey Tourbin <at@altlinux.ru> 5.8-alt1
- initial revision
