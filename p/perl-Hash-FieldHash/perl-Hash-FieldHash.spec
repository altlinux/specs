%define module_version 0.14
%define module_name Hash-FieldHash
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Config.pm) perl(Data/Dumper.pm) perl(Devel/PPPort.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/ParseXS.pm) perl(Hash/Util/FieldHash/Compat.pm) perl(Module/Build.pm) perl(Mouse.pm) perl(Scalar/Util.pm) perl(Symbol.pm) perl(Test/LeakTrace.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm) perl(if.pm) perl(overload.pm) perl(parent.pm) perl(threads.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.14
Release: alt2
Summary: Lightweight field hash for inside-out objects
Group: Development/Perl
License: perl
URL: https://github.com/gfx/p5-Hash-FieldHash

Source0: http://cpan.org.ua/authors/id/G/GF/GFUJI/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md Changes example
%perl_vendor_archlib/H*
%perl_vendor_autolib/*

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- uploaded to Sisyphus as Scalar-Does deep dependency

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- update

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.12-alt3_7
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_6
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_5
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.12-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_4
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_2
- fc import

