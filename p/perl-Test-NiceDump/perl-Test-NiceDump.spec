%define module_name Test-NiceDump
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dump.pm) perl(Data/Dump/Filtered.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Pod/Coverage/TrustPod.pm) perl(Pod/Wordlist.pm) perl(Safe/Isa.pm) perl(Test/Builder.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Test/Spelling.pm) perl(overload.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0.1
Release: alt2
Summary: let's have a nice and human readable dump of our objects!
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DA/DAKKAR/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module uses the section on "`Data::Dump::Filtered'" and a set of sensible
filters to dump test data in a more readable way.

For example, the section on "`DateTime'" objects get printed in the full ISO
8601 format, and the section on "`DBIx::Class::Row'" objects get printed as
hashes of their inflated columns.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/T*

%changelog
* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2
- to Sisyphus as perl-Net-Stomp dep

* Thu Jul 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- updated by package builder

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- initial import by package builder

