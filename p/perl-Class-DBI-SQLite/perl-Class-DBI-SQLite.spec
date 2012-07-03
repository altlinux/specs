%define dist Class-DBI-SQLite
Name: perl-%dist
Version: 0.11
Release: alt2

Summary: Extension to Class::DBI for SQLite
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Class-DBI perl-DBD-SQLite perl-devel

# this dependency cannot be detected automatically
Requires: perl-DBD-SQLite

%description
Class::DBI::SQLite is an extension to Class::DBI for DBD::SQLite.
It allows you to populate an auto-incremented row id after insert.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Class*

%changelog
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt2
- rebuilt

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.09 -> 0.11

* Mon Aug 29 2005 Alexey Tourbin <at@altlinux.ru> 0.09-alt2
- added dependency on perl-DBD-SQLite

* Fri Jul 15 2005 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- initial revision
