%define module_version 1.0003
%define module_name POSIX-Regex
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Devel/CheckLib.pm) perl(Exporter.pm) perl(ExtUtils/Constant.pm) perl(ExtUtils/MakeMaker.pm) perl(Test.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0003
Release: alt2.1.1.1
Summary: unknown
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JE/JETTERO/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/P*
%perl_vendor_autolib/*

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0003-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.0003-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0003-alt2.1
- rebuild with new perl 5.20.1

* Wed Oct 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.0003-alt2
- moved to Sisyphus (for Benchmark-Perl-Formance update)

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.0003-alt1
- initial import by package builder

