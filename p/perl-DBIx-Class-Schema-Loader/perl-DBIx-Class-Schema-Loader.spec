%define dist DBIx-Class-Schema-Loader
Name: perl-%dist
Version: 0.07012
Release: alt1

Summary: Dynamic definition of a DBIx::Class::Schema
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Carp-Clan perl-Class-Unload perl-DBD-SQLite perl-Data-Dump perl-Pod-Parser perl-SQL-Abstract perl-String-CamelCase perl-String-ToIdentifier-EN perl-Task-Weaken perl-Test-Exception perl-Test-Pod perl-Test-Warn

%description
DBIx::Class::Schema::Loader automates the definition of a
DBIx::Class::Schema by scanning database table definitions and
setting up the columns, primary keys, and relationships.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/dbicdump
%perl_vendor_privlib/DBIx

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.07012-alt1
- 0.07002 -> 0.07012

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 0.07002-alt1
- 0.07001 -> 0.07002

* Sun Aug 22 2010 Alexey Tourbin <at@altlinux.ru> 0.07001-alt1
- 0.06001 -> 0.07001

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.06001-alt1
- 0.04005 -> 0.06001
- packaged %_bindir/dbicdump

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.04005-alt1.1
- NMU for unknown reason

* Fri Jun 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.04005-alt1
- 0.04005 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.03009-alt1
- first build for ALT Linux Sisyphus

