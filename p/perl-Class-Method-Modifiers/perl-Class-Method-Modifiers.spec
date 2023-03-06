%define _unpackaged_files_terminate_build 1
%define dist Class-Method-Modifiers
Name: perl-Class-Method-Modifiers
Version: 2.15
Release: alt1

Summary: provides Moose-like method modifiers

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildRequires: perl-Pod-Escapes perl-Test-Fatal perl-Module-Build-Tiny perl(Test/CheckDeps.pm) perl(Test/Requires.pm) perl(Test/Needs.pm)

%description
Method modifiers are a convenient feature from the CLOS (Common Lisp Object
System) world.

In its most basic form, a method modifier is just a method that calls
`$self->SUPER::foo(@_)'. I for one have trouble remembering that exact
invocation, so my classes seldom re-dispatch to their base classes. Very bad!

`Class::Method::Modifiers' provides three modifiers: `before', `around', and
`after'. `before' and `after' are run just before and after the method they
modify, but can not really affect that original method. `around' is run in place
of the original method, with a hook to easily call that original method.  See
the `MODIFIERS' section for more details on how the particular modifiers work.

One clear benefit of using `Class::Method::Modifiers' is that you can define
multiple modifiers in a single namespace. These separate modifiers don't need to
know about each other. This makes top-down design easy. Have a base class that
provides the skeleton methods of each operation, and have plugins modify those
methods to flesh out the specifics.

Parent classes need not know about `Class::Method::Modifiers'. This means you
should be able to modify methods in *any* subclass. See the
Term::VT102::ZeroBased manpage for an example of subclassing with CMM.

In short, `Class::Method::Modifiers' solves the problem of making sure you call
`$self->SUPER::foo(@_)', and provides a cleaner interface for it.

As of version 1.00, `Class::Method::Modifiers' is faster in some cases than the
Moose manpage. See `benchmark/method_modifiers.pl' in the the Moose manpage
distribution.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes CONTRIBUTING
%perl_vendor_privlib/Class/Method/Modifiers.pm

%changelog
* Mon Mar 06 2023 Igor Vlasenko <viy@altlinux.org> 2.15-alt1
- automated CPAN update

* Thu Jan 19 2023 Igor Vlasenko <viy@altlinux.org> 2.14-alt1
- automated CPAN update

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Fri Oct 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.07-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 2.04-alt1
- 1.09 -> 2.04

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.09-alt1
- 1.06 -> 1.09

* Sat Jan 01 2011 Denis Smirnov <mithraen@altlinux.ru> 1.06-alt1
- initial build for ALT Linux Sisyphus

