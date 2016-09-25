%define _unpackaged_files_terminate_build 1
%define dist MooseX-Role-Parameterized
Name: perl-%dist
Version: 1.09
Release: alt1

Summary: Roles with composition parameters
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Role-Parameterized-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-Module-Install perl-Moose perl-Test-Fatal perl(Test/Requires.pm) perl(Test/Requires.pm) perl(CPAN/Meta/Check.pm) perl(namespace/autoclean.pm)

%description
Roles are composable units of behavior.  They are useful for factoring out
functionality common to many classes from any part of your class hierarchy.
See Moose::Cookbook::Roles::Recipe1 for an introduction to Moose::Role.

While combining roles affords you a great deal of flexibility, individual
roles have very little in the way of configurability.  Core Moose provides
-alias for renaming methods and -excludes for ignoring methods.  These
options are primarily for resolving role conflicts.  Depending on how much
of a purist you are, these options are solely for resolving role conflicts.
See Moose::Cookbook::Roles::Recipe2 for more about -alias and -excludes.

Because roles serve many different masters, they usually provide only the
least common denominator of functionality.  To empower roles further, more
configurability than -alias and -excludes is required.  Perhaps your role
needs to know which method to call when it is done processing.  Or what
default value to use for its url attribute.

Parameterized roles offer a solution to these (and other) kinds of problems.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/MooseX*

%changelog
* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2.1
- rebuild to restore role requires

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2
- NMU: fixed build

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- initial revision
