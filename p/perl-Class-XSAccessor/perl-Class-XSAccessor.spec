%define dist Class-XSAccessor
Name: perl-%dist
Version: 1.12
Release: alt2

Summary: Generate fast XS accessors without runtime compilation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel perl-threads

%description
Class::XSAccessor implements fast read, write and read/write accessors in XS.
Additionally, it can provide predicates such as "has_foo()" for testing
whether the attribute "foo" is defined in the object.
It only works with objects that are implemented as ordinary hashes.
Class::XSAccessor::Array implements the same interface for objects
that use arrays for their internal representation.

%prep
%setup -q -n %dist-%version

%build
export XSUBPP_NO_STATIC_XS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Class
%perl_vendor_autolib/Class

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.12-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Fri Feb 25 2011 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt2
- fixed build

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.05 -> 1.11

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1.1
- rebuilt with perl 5.12

* Sun Jan 31 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1
- NMU: New version 1.05

* Thu Oct 22 2009 Michael Bochkaryov <misha@altlinux.ru> 1.03-alt1
- initial build for ALT Linux Sisyphus
