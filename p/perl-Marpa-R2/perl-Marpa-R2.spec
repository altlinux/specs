%define _unpackaged_files_terminate_build 1
%add_findreq_skiplist %perl_vendor_archlib/Marpa/R2/Thin/*
%add_findreq_skiplist %perl_vendor_archlib/Marpa/R2/Thin/*
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(CPAN.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Converter.pm) perl(CPAN/Version.pm) perl(Carp.pm) perl(Config.pm) perl(Config/AutoConf.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(English.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(ExtUtils/Mkbootstrap.pm) perl(Fatal.pm) perl(File/Copy.pm) perl(File/Find/Rule.pm) perl(File/Slurp.pm) perl(File/Spec.pm) perl(HTML/Entities.pm) perl(HTML/LinkExtor.pm) perl(HTML/Parser.pm) perl(IPC/Cmd.pm) perl(LWP/UserAgent.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Module/Load.pm) perl(PPI.pm) perl(Pod/Simple/Checker.pm) perl(Pod/Simple/SimpleTree.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Text/Diff.pm) perl(Time/Piece.pm) perl(URI/URL.pm) perl(WWW/Mechanize.pm) perl(XSLoader.pm)
BuildRequires: perl(YAML/XS.pm) perl(autodie.pm) perl(base.pm) perl(charnames.pm) perl(open.pm) perl(overload.pm) perl(sort.pm)
# END SourceDeps(oneline)
%define module_name Marpa-R2
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 4.000000
Release: alt1.1
Summary: Release 2 of Marpa
Group: Development/Perl
License: open_source
URL: http://savage.net.au/Marpa.html

Source0: http://www.cpan.org/authors/id/J/JK/JKEGL/%{module_name}-%{version}.tar.gz

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}
%if_with bootstrap
cd engine/read_only
%autoreconf
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%add_findreq_skiplist */Marpa/R2/HTML/Config/Compile.pm 

%files
%doc LICENSE COPYING.LESSER Changes README engine/read_only/COPYING
%perl_vendor_archlib/M*
%perl_vendor_autolib/*
%_bindir/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.000000-alt1.1
- rebuild with new perl 5.26.1

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.000000-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.000000-alt2.1.1
- rebuild with new perl 5.24.1

* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 3.000000-alt2.1
- BOOTSTRAP: autoreconf first

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 3.000000-alt2
- to Sisyphus

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 3.000000-alt1.1
- rebuild with perl 5.22

* Wed Nov 04 2015 Igor Vlasenko <viy@altlinux.ru> 3.000000-alt1
- new version

