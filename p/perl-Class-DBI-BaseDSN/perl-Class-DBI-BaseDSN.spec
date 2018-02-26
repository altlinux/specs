%define dist Class-DBI-BaseDSN
Name: perl-%dist
Version: 1.22
Release: alt2

Summary: DSN sensitive base class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Class-DBI perl-Module-Build

%description
Class::DBI::BaseDSN acts as a placeholder for a base class which will
be switched for a specific Class::DBI extension when you specify the
dsn of the database to connect to.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class*

%changelog
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 1.22-alt2
- rebuilt

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- initial revision
