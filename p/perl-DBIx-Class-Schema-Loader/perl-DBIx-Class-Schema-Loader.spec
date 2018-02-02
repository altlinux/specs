%define _unpackaged_files_terminate_build 1
%define dist DBIx-Class-Schema-Loader
Name: perl-%dist
Version: 0.07048
Release: alt1

Summary: Dynamic definition of a DBIx::Class::Schema
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/I/IL/ILMARI/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Carp-Clan perl-Class-Unload perl-DBD-SQLite perl-Data-Dump perl-Pod-Parser perl-SQL-Abstract perl-String-CamelCase perl-String-ToIdentifier-EN perl-Task-Weaken perl-Test-Exception perl-Test-Pod perl-Test-Warn perl(DBIx/Class/IntrospectableM2M.pm) perl(Test/Differences.pm) perl(curry.pm)

%description
DBIx::Class::Schema::Loader automates the definition of a
DBIx::Class::Schema by scanning database table definitions and
setting up the columns, primary keys, and relationships.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%_bindir/dbicdump
%_man1dir/dbicdump*
%perl_vendor_privlib/DBIx

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.07048-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.07047-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.07046-alt1
- automated CPAN update

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.07045-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.07043-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07042-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.07041-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.07040-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.07039-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.07038-alt1
- automated CPAN update

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.07037-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.07036-alt1
- automated CPAN update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.07033-alt1
- automated CPAN update

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

