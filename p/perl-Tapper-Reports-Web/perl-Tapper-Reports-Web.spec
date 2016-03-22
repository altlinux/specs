# we have it in autoimports, but it requires a huge tree of deps
%filter_from_requires /^perl.BenchmarkAnything.Storage.Frontend.Lib.pm./d

%add_findreq_skiplist */Tapper/Reports/Web.pm */auto/Tapper/Reports/Web/tapper.psgi
%add_findreq_skiplist %_bindir/tapper_reports_web_fastcgi_live.pl
%add_findreq_skiplist %_bindir/tapper_reports_web_fastcgi_public.pl
%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Catalyst/DispatchType/Regex.pm) perl(Catalyst/Plugin/Redirect.pm)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm) perl(HTML/Mason/Interp.pm) perl(Catalyst/Action/RenderView.pm) perl(Locale/Maketext.pm) perl(Tapper/Base.pm) perl(Catalyst/Plugin/Redirect.pm)
%define upstream_name    Tapper-Reports-Web
%define upstream_version 5.0.6

Name:       perl-%{upstream_name}
Version:    5.0.6
Release:    alt1

Summary:    Tapper frontend web application based on Catalyst
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/T/TA/TAPPER/Tapper-Reports-Web-%{version}.tar.gz

BuildRequires: perl(Catalyst.pm)
BuildRequires: perl(Catalyst/Controller.pm)
BuildRequires: perl(Catalyst/Controller/HTML/FormFu.pm)
BuildRequires: perl(Catalyst/Model/DBIC/Schema.pm)
BuildRequires: perl(Catalyst/Plugin/ConfigLoader.pm)
BuildRequires: perl(Catalyst/Plugin/Session.pm)
BuildRequires: perl(Catalyst/Plugin/Session/State/Cookie.pm)
BuildRequires: perl(Catalyst/Plugin/Session/Store/File.pm)
BuildRequires: perl(Catalyst/Plugin/Static/Simple.pm)
BuildRequires: perl(Catalyst/Runtime.pm)
BuildRequires: perl(Catalyst/ScriptRunner.pm)
BuildRequires: perl(Catalyst/View/HTML/Mason.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/DPath.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(DateTime/Format/DateParse.pm)
BuildRequires: perl(DateTime/Format/Natural.pm)
BuildRequires: perl(DateTime/Format/Strptime.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(DateTime/Format/W3CDTF.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(FCGI.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Copy/Recursive.pm)
BuildRequires: perl(File/Find/Rule.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/ShareDir/Install.pm)
BuildRequires: perl(File/stat.pm)
BuildRequires: perl(FindBin.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(HTML/FromANSI.pm)
BuildRequires: perl(Hash/Merge.pm)
BuildRequires: perl(Hash/Merge/Simple.pm)
BuildRequires: perl(Module/Find.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Moose/Role.pm)
BuildRequires: perl(Perl6/Junction.pm)
BuildRequires: perl(Pod/Usage.pm)
BuildRequires: perl(Set/Intersection.pm)
BuildRequires: perl(TAP/Formatter/HTML.pm)
BuildRequires: perl(Tapper/Cmd/Precondition.pm)
BuildRequires: perl(Tapper/Cmd/Testplan.pm)
BuildRequires: perl(Tapper/Cmd/Testrun.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Tapper/Testplan/Plugins/Taskjuggler.pm)
BuildRequires: perl(Tapper/Testplan/Reporter.pm)
BuildRequires: perl(Template.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/WWW/Mechanize/Catalyst.pm)
BuildRequires: perl(XML/Feed.pm)
BuildRequires: perl(YAML.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(common/sense.pm)
BuildRequires: perl(namespace/autoclean.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Tapper frontend web application based on Catalyst.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*
/usr/bin/tapper_reports_web_cgi.pl
/usr/bin/tapper_reports_web_create.pl
/usr/bin/tapper_reports_web_fastcgi.pl
/usr/bin/tapper_reports_web_fastcgi_live.pl
/usr/bin/tapper_reports_web_fastcgi_public.pl
/usr/bin/tapper_reports_web_server.pl
/usr/bin/tapper_reports_web_test.pl
/usr/share/man/man1/tapper_reports_web_cgi.pl.1*
/usr/share/man/man1/tapper_reports_web_create.pl.1*
/usr/share/man/man1/tapper_reports_web_fastcgi.pl.1*
/usr/share/man/man1/tapper_reports_web_fastcgi_live.pl.1*
/usr/share/man/man1/tapper_reports_web_fastcgi_public.pl.1*
/usr/share/man/man1/tapper_reports_web_server.pl.1*
/usr/share/man/man1/tapper_reports_web_test.pl.1*


%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.6-alt1
- automated CPAN update
- filtered perl(BenchmarkAnything/Storage/Frontend/Lib.pm) from requires:
  optional and will bring too many deps from autoimports

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

