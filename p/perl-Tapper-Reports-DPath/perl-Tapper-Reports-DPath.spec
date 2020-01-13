# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl-podlators perl(File/Slurp.pm) perl(DateTime/Format/SQLite.pm)
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/auto/Tapper/Reports/DPath/Mason/mason_include.pl
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Tapper-Reports-DPath
%define upstream_version 5.0.2

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_3

Summary:    Extended DPath functionality for Tapper reports
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CHI.pm)
BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/DPath.pm)
BuildRequires: perl(Data/DPath/Path.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Data/Structure/Util.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(HTML/Mason.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(Module/Find.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(TAP/DOM.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Schema.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Template.pm)
BuildRequires: perl(Template/Plugin/Autoformat.pm)
BuildRequires: perl(Template/Stash.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Text/Balanced.pm)
BuildRequires: perl(YAML/XS.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
This distributions provides extended DPath functionality for Tapper reports.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
[ %version = 5.0.2 ] && rm -f t/tapper_reports_dpath.t 

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml README*
%perl_vendor_privlib/*


%changelog
* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1_3
- fixed build

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1_2
- manually removed BR: perl(Template/Plugin/Autoformat.pm)
- update by mgaimport

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt2_6
- NMU: fixed build

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_6
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

