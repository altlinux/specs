%define real_name DBIx-Introspector

Name: perl-%real_name
Version: 0.001005
Release: alt1

Summary: Detect what database you are connected to

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/F/FR/FREW/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-DBI perl-Moo
BuildRequires: perl-Test-Roo perl-Test-Fatal perl-DBD-SQLite

%description
DBIx::Introspector is a tool to detect what database you are connected to,
repeating less of the "guess the database" work across modules.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/DBIx*

%changelog
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 0.001005-alt1
- initial build for Sisyphus
