%define dist Tie-DBI
Name: perl-%dist
Version: 1.05
Release: alt1

Summary: Tie Perl hashes to DBI relational databases
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-DBD-SQLite perl-Encode perl-devel

%description
This module allows you to tie Perl associative arrays (hashes) to SQL
databases using the DBI interface.  The tied hash is associated with
a table in a local or networked database.  One field of the table becomes
the hash key, and another becomes the value.  Once tied, all the standard
hash operations work, including iteration over keys and values.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Tie

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.04 -> 1.05

* Sun Apr 04 2010 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 1.02 -> 1.04

* Wed Jul 29 2009 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.01 -> 1.02

* Thu Mar 10 2005 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- 0.94 -> 1.01

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 0.94-alt1
- 0.93 -> 0.94
- manual pages not packaged (use perldoc)

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 0.93-alt2
- fixed URL

* Mon Sep 29 2003 Alexey Tourbin <at@altlinux.ru> 0.93-alt1
- initial revision (this module is required for full-featured perl-Template)
