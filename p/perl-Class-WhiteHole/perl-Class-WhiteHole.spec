%define dist Class-WhiteHole
Name: perl-%dist
Version: 0.04
Release: alt2

Summary: Base class to treat unhandled method calls as errors
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-devel

%description
Its possible to accidentally inherit an AUTOLOAD method. Often this
will happen if a class somewhere in the chain uses AutoLoader or defines
one of their own. This can lead to confusing error messages when method
lookups fail.

Sometimes you want to avoid this accidental inheritance. In that case,
inherit from Class::WhiteHole. All unhandled methods will produce normal
Perl error messages.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Class

%changelog
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt

* Wed Jul 06 2005 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
