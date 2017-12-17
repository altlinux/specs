# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Spec.pm) perl(POSIX.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.98
%define module_name POSIX-1003
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-POSIX-1003
Version: 0.98
Release: alt4.1

Summary: POSIX::1003, alternative for POSIX in core

Group: Development/Perl
License: perl
Url: %CPAN %module_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://cpan.org.ua/authors/id/M/MA/MARKOV/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO ChangeLog README
%perl_vendor_archlib/P*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.98-alt4.1
- rebuild with new perl 5.26.1

* Sun Oct 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt4
- initial build for ALT Sisyphus

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.98-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.98-alt2
- rebuild to get rid of unmets

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- initial import by package builder

