%define _unpackaged_files_terminate_build 1
%def_with bootstrap
%define dist Moose
Name: perl-%dist
Version: 2.2009
Release: alt1

Summary: A postmodern object system for Perl 5
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

# avoid dependency on perl-devel
%add_findreq_skiplist */Test/Moose*

# XXX Can't locate object method "new" via package "Moose::Meta::Attribute"
%add_findreq_skiplist */Moose/Meta/TypeCoercion.pm
# XXX The 'add_attribute' method cannot be called on an immutable instance
%add_findreq_skiplist */Moose/Meta/TypeConstraint/Parameterizable.pm
%add_findreq_skiplist */Moose/Util/TypeConstraints.pm
# XXX Can't locate object method "initialize" via package "Class::MOP::Class"
%add_findreq_skiplist */Class/MOP.pm
#Can't locate object method "_can_be_made_compatible_with" via package "Class::MOP::Method::Constructor"
%add_findreq_skiplist */Class/MOP/Method/Constructor.pm

Provides: perl-Class-MOP = %version
Obsoletes: perl-Class-MOP < %version

# Automatically added by buildreq on Wed Nov 16 2011 (-bi)
BuildRequires: perl-Algorithm-C3 perl-DateTime perl-Devel-GlobalDestruction perl-Eval-Closure perl-Filter-Simple perl-HTTP-Message perl-IO-String perl-Locale-US perl-MRO-Compat perl-Module-Refresh perl-Params-Coerce perl-Regexp-Common perl-Sub-Name perl-Task-Weaken perl-Test-Deep perl-Test-Fatal perl-Test-Output perl-Test-Requires perl-namespace-clean perl-Test-CheckDeps perl-Package-DeprecationManager perl-Class-Load-XS perl-Throwable perl(Devel/StackTrace.pm) perl(ExtUtils/CBuilder.pm) perl(Test/CleanNamespaces.pm) perl(Devel/OverloadInfo.pm) perl(Test/Warnings.pm) perl(List/MoreUtils.pm) perl(Sub/Exporter.pm)

%if_without bootstrap
BuildRequires: perl-Specio
%else
%define _without_test 1
%endif

%description
Moose is an extension of the Perl 5 object system.

The main goal of Moose is to make Perl 5 Object Oriented programming
easier, more consistent and less tedious. With Moose you can to think
more about what you want to do and less about the mechanics of OOP.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md Changes.Class-MOP doc
%_bindir/moose-*
%perl_vendor_archlib/Class
%perl_vendor_archlib/Moose*
%perl_vendor_autolib/Moose
%perl_vendor_archlib/Test
%perl_vendor_archlib/metaclass.pm
%perl_vendor_archlib/oose.pm

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.2009-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.2008-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.2008-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.2006-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2005-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.2004-alt1
- automated CPAN update

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 2.1807-alt1.1.1
- unbootstrap after rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.1807-alt1.1
- rebuild with new perl 5.24.1

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.1807-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.1806-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.1605-alt1
- automated CPAN update

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 2.1604-alt2.2
- unbootstrap

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.1604-alt2.1
- rebuild with new perl 5.22.0

* Wed Nov 18 2015 Igor Vlasenko <viy@altlinux.ru> 2.1604-alt2
- fixed build for perl 5.22

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.1604-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.1603-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 2.1404-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.1403-alt1
- automated CPAN update

* Sat Dec 13 2014 Igor Vlasenko <viy@altlinux.ru> 2.1213-alt2.2
- unbootstrap

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.1213-alt2.1
- rebuild with new perl 5.20.1

* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.1213-alt2
- support for bootstrap

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.1213-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.1211-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.1210-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.1209-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 2.1208-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.1206-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.1205-alt1
- automated CPAN update

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.1204-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.1202-alt1
- automated CPAN update

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.1201-alt1
- automated CPAN update

* Thu Sep 05 2013 Vladimir Lettiev <crux@altlinux.ru> 2.1005-alt2
- add Specio build dependency

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2.1005-alt1
- 2.0603 -> 2.1005

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 2.0603-alt1
- 2.0400 -> 2.0603
- built for perl-5.16

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

