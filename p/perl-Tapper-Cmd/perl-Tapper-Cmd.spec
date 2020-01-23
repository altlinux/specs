%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm) perl(DateTime/Format/SQLite.pm)

# TODO: fix and adapt to ALT
%add_findreq_skiplist %perl_vendor_privlib/auto/Tapper/Cmd/Init/testplans/topic/*
%add_findreq_skiplist %perl_vendor_privlib/auto/Tapper/Cmd/Init/hello-world/01-executing-tests/*

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Tapper-Cmd
%define upstream_version 5.0.10

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    5.0.11
Release:    alt1

Summary:    Tapper - Backend functions for CLI and Web
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/T/TA/TAPPER/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Cwd.pm)
BuildRequires: perl(DBI.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Copy/Recursive.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(Hash/Merge/Simple.pm)
BuildRequires: perl(Kwalify.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Net/OpenSSH.pm)
BuildRequires: perl(Perl6/Junction.pm)
BuildRequires: perl(Tapper/Base.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Reports/DPath/TT.pm)
BuildRequires: perl(Tapper/Schema.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Tapper/Schema/TestrunDB.pm)
BuildRequires: perl(Template.pm)
BuildRequires: perl(Template/Plugin/Autoformat.pm)
BuildRequires: perl(Template/Plugin/EnvHash.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Text/Autoformat.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(YAML/XS.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Tapper backend functions for the command line and the Web.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
# Cancelling for now due to test failures.
%__make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README
%{perl_vendor_privlib}/*


%changelog
* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 5.0.11-alt1
- automated CPAN update

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.10-alt1_1
- update by mgaimport

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.10-alt1
- automated CPAN update

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.9-alt1
- automated CPAN update

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.8-alt1_1
- update by mgaimport

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.8-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.7-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.6-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.8-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.8-alt1_2
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.8-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.8-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

