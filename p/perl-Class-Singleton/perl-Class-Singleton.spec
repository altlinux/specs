%define dist Class-Singleton
Name: perl-%dist
Version: 1.4
Release: alt2

Summary: Implementation of a "Singleton" class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-devel

%description
This is the Class::Singleton module.  A Singleton describes an object
class that can have only one instance in any system.  An example of a
Singleton might be a print spooler or system registry.  This module
implements a Singleton class from which other classes can be derived.
By itself, the Class::Singleton module does very little other than
manage the instantiation of a single object.  In deriving a class from
Class::Singleton, your module will inherit the Singleton instantiation
method and can implement whatever specific functionality is required.

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
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 1.4-alt2
- rebuilt as plain src.rpm

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 1.4-alt1
- 1.03 -> 1.4

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- initial revision
