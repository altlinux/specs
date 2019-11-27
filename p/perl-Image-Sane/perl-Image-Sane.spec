%define _unpackaged_files_terminate_build 1
%define module_name Image-Sane

Name: perl-Image-Sane
Version: 5
Release: alt1

Summary: Perl extension for the SANE (Scanner Access Now Easy) Project

Group: Development/Perl
License: perl
Url: %CPAN %module_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://mirror.yandex.ru/mirrors/cpan/authors/id/R/RA/RATCLIFFE/%module_name-%version.tar
Patch: Image-Sane-4-fix-586-flags.patch

# BEGIN SourceDeps(oneline):
BuildRequires: libsane-devel perl(English.pm) perl(Exception/Class.pm) perl(Exporter.pm) perl(ExtUtils/Depends.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/PkgConfig.pm) perl(Readonly.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Test/Requires.pm) perl(Try/Tiny.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)

BuildRequires: rpm-build-perl perl-devel perl-podlators

%description
These Perl bindings for the SANE (Scanner Access Now Easy) Project
allow you to access SANE-compatible scanners in a Perlish and
object-oriented way, freeing you from the casting and memory management in C,
yet remaining very close in spirit to original API.

Find out more about SANE at http://www.sane-project.org.
%prep
%setup -n %module_name-%version
%patch -p2

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_archlib/I*
%perl_vendor_autolib/*

%changelog
* Wed Nov 27 2019 Igor Vlasenko <viy@altlinux.ru> 5-alt1
- new version

* Fri Sep 20 2019 Igor Vlasenko <viy@altlinux.ru> 4-alt1
- new version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt4.1
- rebuild with new perl 5.28.1

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt4
- rebuild on aarch64

* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt3
- initial build for ALT Sisyphus

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- rebuild with perl 5.26

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- initial import by package builder

