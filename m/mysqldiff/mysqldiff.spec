Name: mysqldiff
Version: 0.43
Release: alt1

Summary: Comparing the schema (table structures) of two MySQL databases

License: Public domain
Group: Development/Databases
Url: http://adamspiers.org/computing/mysqldiff/

# https://github.com/aspiers/mysqldiff
Source: %name-%version.tar

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 08 2011
# optimized out: MySQL-client perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-YAML-Tiny perl-devel perl-podlators
BuildRequires: perl-File-Slurp perl-Module-Build

%description
MySQL-Diff is suite of Perl modules and accompanying
CLI script for comparing the schema (table structures) of two MySQL databases.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/%name
%perl_vendor_privlib/MySQL/


%changelog
* Tue Nov 08 2011 Vitaly Lipatov <lav@altlinux.ru> 0.43-alt1
- initial build for ALT Linux Sisyphus
