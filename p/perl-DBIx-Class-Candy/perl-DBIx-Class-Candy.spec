%define real_name DBIx-Class-Candy

Name: perl-%real_name
Version: 0.005004
Release: alt1

Summary: Sugar for your favorite ORM, DBIx::Class

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/W/WE/WESM/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-DBIx-Class perl-Lingua-EN-Inflect perl-MRO-Compat perl-Sub-Exporter perl-namespace-clean
BuildRequires: perl-Test-Deep perl-Test-Fatal

%description
DBIx::Class::Candy provides sugar syntax for defining DBIx::Class result
classes, making the common case cleaner and more readable.

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
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 0.005004-alt1
- initial build for Sisyphus
