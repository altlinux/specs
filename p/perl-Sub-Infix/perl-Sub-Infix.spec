%define module_version 0.004
%define module_name Sub-Infix
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.004
Release: alt2
Summary: create a fake infix operator
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Sub-Infix

Source0: http://cpan.org.ua/authors/id/T/TO/TOBYINK/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
Sub::Infix creates fake infix operators using overloading. It doesn't
use source filters, or the Devel::Declare manpage, or any of that magic. (Though
Devel::Declare isn't magic enough to define infix operators anyway; I
know; I've tried.) It's pure Perl, has no non-core dependencies, and
runs on Perl 5.8.

The price you pay for its simplicity is that you cannot define an
operator that can be used like this:

   my $five = 2 plus 3;

Instead, the operator needs to be wrapped with real Perl operators in
one of three ways:

   my $five = 2 |plus| 3;
   my $five = 2 /plus/ 3;
   my $five = 2 <<plus>> 3;

The advantage of this is that it gives you three different levels of
operator precedence.

You can also call the function a slightly less weird way:

   my $five = plus->(2, 3);


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE COPYRIGHT Changes
%perl_vendor_privlib/S*

%changelog
* Sat Jul 29 2023 Igor Vlasenko <viy@altlinux.org> 0.004-alt2
- to Sisyphus as perl-IO-Prompter dep

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- regenerated from template by package builder

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

