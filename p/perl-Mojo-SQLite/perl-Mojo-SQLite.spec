%define _unpackaged_files_terminate_build 1

Name:           perl-Mojo-SQLite
Version:        3.001
Release:        alt1
Summary:        Tiny Mojolicious wrapper for SQLite
License:        Artistic 2.0
Group:		Development/Perl
URL:            https://metacpan.org/release/Mojo-SQLite/
Source:        	%name-%version.tar

BuildArch:      noarch
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict)
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
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md LICENSE
%perl_vendorlib/Mojo*

%changelog
* Tue Nov 20 2018 Alexandr Antonov <aas@altlinux.org> 3.001-alt1
- initial build for ALT
