%define _unpackaged_files_terminate_build 1
%define module_name MooX-TypeTiny
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Moo.pm) perl(Sub/Quote.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Type/Tiny.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002002
Release: alt1
Summary: Optimized type checks for Moo + Type::Tiny
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module optimizes the Moo manpage type checks when used with the Type::Tiny manpage to perform
better.  It will automatically apply to isa checks and coercions that use
Type::Tiny.  Non-Type::Tiny isa checks will work as normal.

This is done by inlining the type check in a more optimal manner that is
specific to Type::Tiny rather than the general mechanism Moo usually uses.

With this module, setters with type checks should be as fast as an equivalent
check in the Moose manpage.

It is hoped that eventually this type inlining will be done automatically,
making this module unnecessary.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/M*

%changelog
* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.002002-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.001004-alt2
- to Sisyphus as perl-Sub-HandlesVia dep

* Fri Jan 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.001004-alt1
- updated by package builder

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.001003-alt1.1
- rebuild to restore role requires

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.001003-alt1
- regenerated from template by package builder

* Sat Nov 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.001002-alt1
- regenerated from template by package builder

* Mon Oct 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1
- initial import by package builder

