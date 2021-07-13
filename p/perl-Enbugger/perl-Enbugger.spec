%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(B/Utils.pm) perl(Config.pm) perl(Devel/NYTProf.pm) perl(Devel/Trepan/Core.pm) perl(Devel/ebug/Backend.pm) perl(Devel/ptkdb.pm) perl(English.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(XSLoader.pm) perl(constant.pm) perl(perl5db.pl)
# END SourceDeps(oneline)
%define module_version 2.016
%define module_name Enbugger
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.016
Release: alt7
Summary: "Enables the debugger at runtime"
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/Enbugger

Source0: http://cpan.org.ua/authors/id/J/JJ/JJORE/%{module_name}-%{module_version}.tar.gz

%description
From summary: %summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description scripts
scripts for %module_name

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README LICENSE Changes TODO
%perl_vendor_archlib/E*
%perl_vendor_autolib/*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 2.016-alt7
- to Sisyphus as perl-XXX dep

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 2.016-alt6
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.016-alt5
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 2.016-alt4.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.016-alt4
- rebuild with perl 5.26

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 2.016-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.016-alt2.1
- rebuild with perl 5.22

* Sun Dec 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.016-alt2
- rebuild to get rid of unmets

* Sat May 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.016-alt1
- initial import by package builder

