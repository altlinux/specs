%define _unpackaged_files_terminate_build 1
%define module_name MooX-Role-Parameterized
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/MoreUtils.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(autodie.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.300
Release: alt1
Summary: MooX::Role::Parameterized - roles with composition parameters
Group: Development/Perl
License: mit
URL: https://github.com/peczenyj/MooX-Role-Parameterized

Source0: http://www.cpan.org/authors/id/P/PA/PACMAN/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changelog README.md examples
%perl_vendor_privlib/M*

%changelog
* Tue Jan 02 2024 Igor Vlasenko <viy@altlinux.org> 0.300-alt1
- automated CPAN update

* Sun Mar 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.082-alt2
- to Sisyphus as DBIx-Class-DeploymentHandler dep

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.082-alt1.1
- rebuild to restore role requires

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.082-alt1
- regenerated from template by package builder

* Tue Dec 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Mon Oct 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

