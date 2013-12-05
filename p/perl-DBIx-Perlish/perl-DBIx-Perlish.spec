%define _unpackaged_files_terminate_build 1
%define dist DBIx-Perlish
Name: perl-%dist
Version: 0.61
Release: alt1

Summary: a perlish interface to SQL databases

License: BSD
Group: Development/Perl
Url: %CPAN %dist

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/G/GR/GRUBER/DBIx-Perlish-%{version}.tar.gz

# Automatically added by buildreq on Tue Sep 09 2008 (-bi)
BuildRequires: perl-DBD-SQLite perl-Module-Install perl-PadWalker perl-Test-Pod perl-Test-Pod-Coverage

%description
The DBIx::Perlish module provides the ability to work with databases supported
by the DBI module using Perl's own syntax for four most common operations:
SELECT, UPDATE, DELETE, and INSERT.

By using DBIx::Perlish, you can write most of your database queries using a
domain-specific language with Perl syntax. Since a Perl programmer knows Perl
by definition, and might not know SQL to the same degree, this approach
generally leads to a more comprehensible and maintainable code.

The module is not intended to replace 100 percent of SQL used in your program.
There is a hope, however, that it can be used to replace a substantial portion
of it.

The DBIx::Perlish module quite intentionally neither implements nor cares about
database administration tasks like schema design and management. The plain DBI
interface is quite sufficient for that. Similarly, and for the same reason, it
does not take care of establishing database connections or handling
transactions. All this is outside the scope of this module.


%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/DBIx/Perlish*
%doc Changes README

%changelog
* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.59-alt1
- 0.56 -> 0.59

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Tue Sep 09 2008 Michael Bochkaryov <misha@altlinux.ru> 0.44-alt1
- first build for ALT Linux Sisyphus

