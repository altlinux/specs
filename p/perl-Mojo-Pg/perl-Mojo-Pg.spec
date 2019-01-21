%define _unpackaged_files_terminate_build 1
%define sname mojo-pg

Name: perl-Mojo-Pg
Version: 4.13
Release: alt1
Summary: Mojolicious PostgreSQL
License: Artistic-2.0
Group: Development/Perl
Url: http://search.cpan.org/dist/Mojo-Pg/
Source0: http://www.cpan.org/authors/id/S/SR/SRI/Mojo-Pg-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl(DBD/Pg.pm)
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(SQL/Abstract.pm)

Requires: perl(Mojolicious.pm)
Requires: perl(SQL/Abstract.pm)

%description
Mojo::Pg is a tiny wrapper around DBD::Pg that makes at
http://www.postgresql.org a lot of fun to use with the at
http://mojolicious.org real-time web framework. Perform queries blocking
and non-blocking, use all at
https://www.postgresql.org/docs/current/static/sql.html PostgreSQL has to
offer, generate CRUD queries from data structures, manage your database
schema with migrations and build scalable real-time web applications with
the publish/subscribe pattern.

%prep
%setup -q -n Mojo-Pg-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README.md examples
%perl_vendorlib/Mojo*
%perl_vendorlib/SQL/Abstract/Pg.pm
%doc Changes LICENSE README.md

%changelog
* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 4.13-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 4.12-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 4.11-alt1
- automated CPAN update

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 4.10-alt1
- automated CPAN update

* Wed Aug 08 2018 Igor Vlasenko <viy@altlinux.ru> 4.09-alt1
- automated CPAN update

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.08-alt1
- initial build for ALT
