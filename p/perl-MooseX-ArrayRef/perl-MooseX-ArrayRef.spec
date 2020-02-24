%define module_version 0.005
%define module_name MooseX-ArrayRef
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(ExtUtils/MakeMaker.pm) perl(Moose.pm) perl(Moose/Exporter.pm) perl(Moose/Role.pm) perl(Moose/Util/MetaRole.pm) perl(Scalar/Util.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.005
Release: alt2
Summary: blessed arrayrefs with Moose
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/MooseX-ArrayRef

Source0: http://cpan.org.ua/authors/id/T/TO/TOBYINK/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
Objects implemented with arrayrefs rather than hashrefs are often faster than
those implemented with hashrefs. Moose's default object implementation is
hashref based. Can we go faster?

Simply `use MooseX::ArrayRef' instead of `use Moose', but note the
limitations in the section below.

The current implementation is mostly a proof of concept, but it does mostly
seem to work.

=begin private

=item init_meta

=end private


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE COPYRIGHT examples
%perl_vendor_privlib/M*

%changelog
* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- to Sisyphus as perl-Sub-HandlesVia dep

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1.1
- rebuild to restore role requires

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- initial import by package builder

