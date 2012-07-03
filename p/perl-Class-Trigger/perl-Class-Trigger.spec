%define dist Class-Trigger
Name: perl-%dist
Version: 0.14
Release: alt2

Summary: Mixin to add / call inheritable triggers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-IO-stringy perl-Test-Base

%description
Class::Trigger is a mixin class to add / call triggers (or hooks)
that get called at some points you specify.

%prep
%setup -q -n %dist-%version
rm -r inc/

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- rebuilt as plain src.rpm

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.13 -> 0.14

* Fri Mar 07 2008 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- 0.12 -> 0.13

* Tue Mar 04 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- 0.11 -> 0.12

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.09 -> 0.11

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- initial revision
