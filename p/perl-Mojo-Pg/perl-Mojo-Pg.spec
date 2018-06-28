%define _unpackaged_files_terminate_build 1
%define sname mojo-pg

Name: perl-Mojo-Pg
Version: 4.08
Release: alt1
Summary: Mojolicious PostgreSQL
License: Artistic-2.0
Group: Development/Perl
Url: http://search.cpan.org/dist/Mojo-Pg/
Source: %sname-%version.tar
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
%setup -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/Mojo*
%perl_vendorlib/SQL/Abstract/Pg.pm
%doc Changes LICENSE README.md

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.08-alt1
- initial build for ALT
