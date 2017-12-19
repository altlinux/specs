%define _unpackaged_files_terminate_build 1
%define module_version 0.0218
%define module_name Devel-PerlySense
%add_findreq_skiplist %perl_vendor_privlib/Devel/PerlySense.pm
%add_findreq_skiplist %perl_vendor_privlib/Devel/PerlySense*.pm

# BEGIN SourceDeps(oneline):
BuildRequires: perl(App/Ack.pm) perl(Cache/Cache.pm) perl(Cache/FileCache.pm) perl(Carp.pm) perl(Class/MethodMaker.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Devel/CoverX/Covered.pm) perl(Devel/CoverX/Covered/Db.pm) perl(Exception/Class.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Corresponding.pm) perl(File/Corresponding/Config/Find.pm) perl(File/Find.pm) perl(File/Find/Rule.pm) perl(File/Path.pm) perl(File/Slurp.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(File/chdir.pm) perl(Getopt/Long.pm) perl(Graph/Easy.pm) perl(HTTP/Date.pm) perl(IO/String.pm) perl(List/MoreUtils.pm) perl(List/Util.pm) perl(Module/Pluggable.pm) perl(Moose.pm) perl(POSIX.pm) perl(PPI.pm) perl(PPI/Document.pm) perl(PPI/Dumper.pm) perl(Path/Class.pm) perl(Perl/Critic.pm) perl(Perl/Tidy.pm) perl(Pod/Text.pm) perl(Pod/Usage.pm) perl(Spiffy.pm) perl(Storable.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Text/Table.pm) perl(Time/HiRes.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm) perl(List/AllUtils.pm) perl(Tree/Parser.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.0218
Release: alt2
Summary: Perl IDE backend with Emacs frontend.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/J/JO/JOHANL/Devel-PerlySense-%{version}.tar.gz
Patch: Devel-PerlySense-0.0218-perl5.26.patch
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version
%patch -p1
rm t/PerlySense-Editor-Emacs-class-overview.t

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes LICENSE doc
%perl_vendor_privlib/D*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.0218-alt2
- fixed build with new perl 5.26

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.0218-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.0217-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.0216-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.0213-alt1
- automated CPAN update

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.0211-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.0211-alt1
- regenerated from template by package builder

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.0207-alt1
- initial import by package builder

