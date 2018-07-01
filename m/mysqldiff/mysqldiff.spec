Name: mysqldiff
Version: 0.60
Release: alt1

Summary: Comparing the schema (table structures) of two MySQL databases

License: Public domain
Group: Development/Databases
Url: http://adamspiers.org/computing/mysqldiff/

# Source-git: https://github.com/aspiers/mysqldiff
Source: %name-%version.tar

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 08 2011
# optimized out: MySQL-client perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-YAML-Tiny perl-devel perl-podlators
BuildRequires: perl-File-Slurp perl-Module-Build perl-JSON-PP

BuildRequires: perl-Dist-Zilla perl-App-cpanminus perl-String-ShellQuote

%description
MySQL-Diff is suite of Perl modules and accompanying
CLI script for comparing the schema (table structures) of two MySQL databases.

%prep
%setup

%build
dzil build
#perl_vendor_build

%install
dzil install --install-command="cpanm --local-lib=%buildroot/%_prefix ."

# FIXME
mv %buildroot%_prefix/lib %buildroot%_datadir
mv %buildroot%_prefix/man %buildroot%_datadir/

%files
%_bindir/%name
%perl_vendor_privlib/MySQL/Diff/
%perl_vendor_privlib/MySQL/Diff.pm
%_man1dir/*
%_man3dir/*

%changelog
* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.60-alt1
- new version 0.60 (with rpmrb script) (ALT bug 35108)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.43-alt2
- fix build

* Tue Nov 08 2011 Vitaly Lipatov <lav@altlinux.ru> 0.43-alt1
- initial build for ALT Linux Sisyphus
