%define dist Moose
Name: perl-%dist
Version: 2.0400
Release: alt1

Summary: A postmodern object system for Perl 5
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# avoid dependency on perl-devel
%add_findreq_skiplist */Test/Moose*

# XXX Can't locate object method "new" via package "Moose::Meta::Attribute"
%add_findreq_skiplist */Moose/Meta/TypeCoercion.pm
# XXX The 'add_attribute' method cannot be called on an immutable instance
%add_findreq_skiplist */Moose/Meta/TypeConstraint/Parameterizable.pm
%add_findreq_skiplist */Moose/Util/TypeConstraints.pm
# XXX Can't locate object method "initialize" via package "Class::MOP::Class"
%add_findreq_skiplist */Class/MOP.pm

Provides: perl-Class-MOP = %version
Obsoletes: perl-Class-MOP < %version

# Automatically added by buildreq on Wed Nov 16 2011 (-bi)
BuildRequires: perl-Algorithm-C3 perl-DateTime perl-Devel-GlobalDestruction perl-Eval-Closure perl-Filter-Simple perl-HTTP-Message perl-IO-String perl-Locale-US perl-MRO-Compat perl-Module-Refresh perl-Params-Coerce perl-Regexp-Common perl-Sub-Name perl-Task-Weaken perl-Test-Deep perl-Test-Fatal perl-Test-Output perl-Test-Requires perl-namespace-clean

%description
Moose is an extension of the Perl 5 object system.

The main goal of Moose is to make Perl 5 Object Oriented programming
easier, more consistent and less tedious. With Moose you can to think
more about what you want to do and less about the mechanics of OOP.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/moose-*
%perl_vendor_archlib/Class
%perl_vendor_archlib/Moose*
%perl_vendor_autolib/Moose
%perl_vendor_archlib/Test
%perl_vendor_archlib/metaclass.pm
%perl_vendor_archlib/oose.pm

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 2.0400-alt1
- 2.0205 -> 2.0400
- disabled dependency on perl-devel

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 2.0205-alt1
- 1.24 -> 2.0205
- built for perl-5.14
- provides and obsoletes perl-Class-MOP

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.21 -> 1.24

* Sun Jan 09 2011 Alexey Tourbin <at@altlinux.ru> 1.21-alt1
- 1.08 -> 1.21

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1.1
- rebuilt with perl 5.12
- dropped MooseX-* builddeps to resolve cyclic deps

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 1.07-alt1
- 1.03 -> 1.07

* Sun May 16 2010 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.01 -> 1.03

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- 0.99 -> 1.01
- fixed module packaging

* Thu Mar 18 2010 Mikhail Pokidko <pma@altlinux.org> 0.99-alt1
- version up

* Tue Feb 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.98-alt1
- Version up.

* Thu Nov 19 2009 Mikhail Pokidko <pma@altlinux.org> 0.93-alt1
- Version up. Closes: 22330

* Mon Oct 20 2008 Mikhail Pokidko <pma@altlinux.org> 0.59-alt1
- version up

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 0.54-alt2
- sisyphus_check

* Fri Aug 01 2008 Mikhail Pokidko <pma@altlinux.org> 0.54-alt1
- version up

* Thu May 15 2008 Mikhail Pokidko <pma@altlinux.org> 0.44-alt1
- first build for ALT Linux Sisyphus

