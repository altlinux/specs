%define dist Class-Data-Inheritable
Name: perl-%dist
Version: 0.08
Release: alt2

Summary: Inheritable, overridable class data
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Test-Pod

%description
Class::Data::Inheritable is for creating accessor/mutators to class
data.  That is, if you want to store something about your class as a
whole (instead of about a single object).  This data is then inherited
by your subclasses and can be overriden.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class*

%changelog
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 0.08-alt2
- rebuilt as plain src.rpm

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- 0.06 -> 0.08

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- 0.04 -> 0.06

* Sun Sep 25 2005 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- 0.02 -> 0.04

* Wed Jul 06 2005 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision
