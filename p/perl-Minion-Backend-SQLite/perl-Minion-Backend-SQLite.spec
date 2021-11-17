%define _unpackaged_files_terminate_build 1

Name:           perl-Minion-Backend-SQLite
Version:        5.0.6
Release:        alt1
Summary:        SQLite backend for Minion job queue
License:        Artistic 2.0
Group: 		Development/Perl
URL:            https://metacpan.org/release/Minion-Backend-SQLite/
Source0:        	http://www.cpan.org/authors/id/D/DB/DBOOK/Minion-Backend-SQLite-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Mojo/Base.pm)
BuildRequires:  perl(Mojo/SQLite.pm)
BuildRequires:  perl(Mojo/Util.pm)
BuildRequires:  perl(Sys/Hostname.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Minion.pm)
BuildRequires:  perl(Minion/Backend.pm)
BuildRequires:  perl(Module/Metadata.pm)
BuildRequires:  perl(Mojo/IOLoop.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)

%description
Minion::Backend::SQLite is a backend for Minion based on Mojo::SQLite. All
necessary tables will be created automatically with a set of migrations
named minion. If no connection string or :temp: is provided, the database
will be created in a temporary directory.

%prep
%setup -q -n Minion-Backend-SQLite-v%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md examples README
%{perl_vendorlib}/Minion*

%changelog
* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.org> 5.0.6-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 5.0.5-alt1
- automated CPAN update

* Wed Feb 17 2021 Igor Vlasenko <viy@altlinux.ru> 5.0.4-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1
- automated CPAN update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1
- automated CPAN update

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 4.005-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.004-alt1
- automated CPAN update

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.003-alt1
- automated CPAN update

* Thu Nov 29 2018 Alexandr Antonov <aas@altlinux.org> 4.002-alt1
- initial build for ALT
