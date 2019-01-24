# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Spec.pm) perl(POSIX.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_name POSIX-1003

Name: perl-POSIX-1003
Version: 0.99_07
Release: alt1.1

Summary: POSIX::1003, alternative for POSIX in core

Group: Development/Perl
License: perl
Url: %CPAN %module_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://cpan.org/authors/id/M/MA/MARKOV/%module_name-%version.tar.gz

BuildRequires: rpm-build-perl perl-devel perl-podlators

# test t/50glob.t check /etc/a* (more than 2)
BuildRequires: alternatives atop

%description
%summary

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO ChangeLog README
%perl_vendor_archlib/P*
%perl_vendor_autolib/*

%changelog
* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.99_07-alt1.1
- rebuild with new perl 5.28.1

* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.99_07-alt1
- new version 0.99_07 (with rpmrb script)

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

