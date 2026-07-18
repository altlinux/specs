%define module asa

Name: perl-%module
Version: 1.04
Release: alt1

Summary: Lets your class/object say it works like something else

Group: Development/Perl
License: GPL-1.0-or-later OR Artistic-1.0-clause
Url: %CPAN %module
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETHER/%module-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel /proc

%description
The asa pragma lets your class/object say it works like something else,
without inheriting from it.  This is useful for adapting non-Moose classes
to roles that expect a specific base class, by declaring the relationship
at compile time.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/asa.pm

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt1
- initial build for ALT Sisyphus


