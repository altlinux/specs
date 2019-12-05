%define _unpackaged_files_terminate_build 1
%define module_name Perl-PrereqScanner-NotQuiteLite
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Any/Moose.pm) perl(Apache/DBI.pm) perl(CPAN/Meta/Prereqs.pm) perl(CPAN/Meta/Requirements.pm) perl(Catalyst.pm) perl(Class/Accessor.pm) perl(Class/Autouse.pm) perl(Class/Load.pm) perl(DBI.pm) perl(Data/Dump.pm) perl(Data/Section.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/MakeMaker/CPANfile.pm) perl(Function/Parameters.pm) perl(Inline.pm) perl(LWP/UserAgent.pm) perl(Mo.pm) perl(Module/CPANfile.pm) perl(Module/CoreList.pm) perl(Module/Find.pm) perl(Module/Runtime.pm) perl(Mojo/Base.pm) perl(Mojo/Loader.pm) perl(Mojolicious.pm)
BuildRequires: perl(Mojolicious/Lite.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Moose.pm) perl(MooseX/Declare.pm) perl(MooseX/Role/Parameterized.pm) perl(MooseX/Types.pm) perl(Mouse.pm) perl(Package/Variant.pm) perl(Parse/RecDescent.pm) perl(Pegex/Base.pm) perl(Plack/Builder.pm) perl(Pod/POM.pm) perl(Pod/POM/View/HTML.pm) perl(Regexp/Trie.pm) perl(Test/Class.pm) perl(Test/FailWarnings.pm) perl(Test/More.pm) perl(Test/Most.pm) perl(Test/Pod.pm) perl(Test/Requires.pm) perl(Test/UseAllModules.pm) perl(Text/Balanced.pm) perl(XXX.pm) perl(YAML/Syck.pm) perl(aliased.pm)
BuildRequires: perl(experimental.pm) perl(lib/abs.pm) perl(parent.pm) perl(prefork.pm) perl(syntax.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.9909
Release: alt1
Summary: a tool to scan your Perl code for its prerequisites
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/I/IS/ISHIGAKI/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

# no need to pull those test deps to Sisyphus:
# use Acme::CPANAuthors
rm -f t/app/use_index.t
# used Data::Phrasebook::Loader::Base Data::Phrasebook::Debug
rm -f t/compat/module_extractuse/10_basic.t
#with 'Data::Record::Serialize::Role::Base';
rm -f t/package_variant.t
#use Keyword::Declare; use Lingua::Romana::Perligata
rm -f t/scan/keyword_declare.t
#use Mojo::Log::Che;
rm -f t/scan/utf8.t
#use Object::InsideOut
rm -f t/scan/re.t
#require Pod::Simple::Wiki;
rm -f t/scan/print.t
#use Syntax::Collector
rm -f t/syntax_collector.t
#use Test::Class::Most
rm -f t/test_class_most.t
#use Test::Routine
rm -f t/moose/moose.t
#use TryCatch
rm -f t/scan/trycatch.t
#use later '...';
rm -f t/later.t
#use mixin 'Exporter';
rm -f t/mixin.t
#use only MyModule
rm -f t/only.t
#use tt 
rm -f t/scan/tt.t
#use unless
rm -f t/unless.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/P*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.9909-alt1
- automated CPAN update

* Sun Aug 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.9908-alt1
- automated CPAN update

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.9906-alt1
- automated CPAN update

* Sun May 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.9905-alt1
- automated CPAN update

* Wed Feb 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.9904-alt1
- automated CPAN update

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.9903-alt2
- to Sisyphus as Module-CPANTS-Analyse dep

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.9903-alt1
- regenerated from template by package builder

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.9902-alt1
- regenerated from template by package builder

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.9901-alt1
- regenerated from template by package builder

* Sun Nov 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- regenerated from template by package builder

* Tue Oct 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- regenerated from template by package builder

* Wed Sep 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- regenerated from template by package builder

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- regenerated from template by package builder

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- regenerated from template by package builder

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- regenerated from template by package builder

* Mon Oct 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

