%define _unpackaged_files_terminate_build 1

Name:           perl-Mojo-SQLite
Version:        3.009
Release:        alt1
Summary:        Tiny Mojolicious wrapper for SQLite
License:        Artistic 2.0
Group:		Development/Perl
URL:            https://metacpan.org/release/Mojo-SQLite/
Source0:        	http://www.cpan.org/authors/id/D/DB/DBOOK/Mojo-SQLite-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(Module/Build.pm) perl(SQL/Abstract/Pg.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires: 	perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Term/ReadLine.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Mojo/Base.pm)
BuildRequires:  perl(Mojo/Collection.pm)
BuildRequires:  perl(Mojo/EventEmitter.pm)
BuildRequires:  perl(Mojo/File.pm)
BuildRequires:  perl(Mojo/IOLoop.pm)
BuildRequires:  perl(Mojo/JSON.pm)
BuildRequires:  perl(Mojo/Loader.pm)
BuildRequires:  perl(Mojo/Util.pm)
BuildRequires:  perl(SQL/Abstract.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(Module/Metadata.pm)
BuildRequires:  perl(Mojolicious/Lite.pm)
BuildRequires:  perl(Test/Mojo.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(URI/db.pm)
BuildRequires:  perl(Pod/Coverage/TrustPod.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)

%description
Mojo::SQLite is a tiny wrapper around DBD::SQLite that makes SQLite a lot
of fun to use with the Mojolicious real-time web framework. Use all SQL
features SQLite has to offer, generate CRUD queries from data structures,
and manage your database schema with migrations.

%prep
%setup -q -n Mojo-SQLite-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md README examples
%perl_vendorlib/Mojo*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 3.009-alt1
- automated CPAN update

* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 3.008-alt1
- automated CPAN update

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 3.007-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 3.006-alt1
- automated CPAN update

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 3.005-alt1
- automated CPAN update

* Thu Jul 23 2020 Igor Vlasenko <viy@altlinux.ru> 3.004-alt1
- automated CPAN update

* Mon Oct 07 2019 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1
- automated CPAN update

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.002-alt1
- automated CPAN update

* Thu Jun 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.001-alt2
- fixed BR: perl(strict)

* Tue Nov 20 2018 Alexandr Antonov <aas@altlinux.org> 3.001-alt1
- initial build for ALT
