%define real_name DBIx-Class-Helpers

Name: perl-%real_name
Version: 2.037000
Release: alt1

Summary: Simplify the common case stuff for DBIx::Class

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/W/WE/WESM/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-DBIx-Class perl-DBIx-Class-Candy perl-DBIx-Introspector
BuildRequires: perl-Carp-Clan perl-Lingua-EN-Inflect perl-Sub-Exporter-Progressive
BuildRequires: perl-Text-Brew perl-namespace-clean perl-Module-Runtime
BuildRequires: perl-Safe-Isa perl-Moo perl-Try-Tiny
BuildRequires: perl-DBD-SQLite perl-DateTime-Format-SQLite
BuildRequires: perl-Test-Deep perl-Test-Fatal perl-Test-Roo perl-aliased

%description
DBIx::Class::Helpers is a collection of modules to simplify the common
case stuff for DBIx::Class, providing a set of reusable components and
result-set helpers.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/DBIx*

%changelog
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 2.037000-alt1
- initial build for Sisyphus
