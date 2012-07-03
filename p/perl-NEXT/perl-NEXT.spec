%define dist NEXT
Name: perl-%dist
Version: 0.65
Release: alt1

Summary: A pseudo-class NEXT that allows method redispatch
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Dec 19 2010
BuildRequires: perl-devel

%description
NEXT.pm adds a pseudoclass named NEXT to any program that uses it.
If a method m calls $self->NEXT::m(), the call to m is redispatched
as if the calling method had not originally been found.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/NEXT.pm

%changelog
* Sun Dec 19 2010 Alexey Tourbin <at@altlinux.ru> 0.65-alt1
- 0.64 -> 0.65

* Sat Jun 20 2009 Alexey Tourbin <at@altlinux.ru> 0.64-alt1
- 0.62 -> 0.64

* Wed Apr 08 2009 Alexey Tourbin <at@altlinux.ru> 0.62-alt1
- 0.60 -> 0.62

* Fri Dec 17 2004 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- initial revision (split off from perl-base)
