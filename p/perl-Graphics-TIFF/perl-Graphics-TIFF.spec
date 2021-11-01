%define _unpackaged_files_terminate_build 1
%define module_name Graphics-TIFF

Name: perl-Graphics-TIFF
Version: 18
Release: alt1

Summary: Perl extension for the libtiff library

License: perl
Group: Development/Perl
Url: %CPAN %module_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://mirror.yandex.ru/mirrors/cpan/authors/id/R/RA/RATCLIFFE/%module_name-%version.tar

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
BuildRequires: libtiff-devel perl(English.pm) perl(Exporter.pm) perl(ExtUtils/Depends.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/PkgConfig.pm) perl(Readonly.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Test/Requires.pm) perl(XSLoader.pm) perl(base.pm) perl(IPC/Cmd.pm)

%description
The Graphics::TIFF module allows a Perl developer to access TIFF images.
Find out more about libtiff at http://www.libtiff.org.


%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/G*
%perl_vendor_autolib/*

%changelog
* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.org> 18-alt1
- new version

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 17-alt1
- new version

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 16-alt1
- new version

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 15-alt1
- new version 15 (with rpmrb script)

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 13-alt1
- new version

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 12-alt1
- new version

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 11-alt1
- new version

* Wed Apr 14 2021 Igor Vlasenko <viy@altlinux.org> 10-alt1
- new version

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 9-alt1
- new version

* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 8-alt1
- new version

* Wed Dec 02 2020 Vitaly Lipatov <lav@altlinux.ru> 7-alt2
- human build for ALT Sisyphus

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 7-alt1
- updated by package builder

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 6-alt3.1
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 6-alt2.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 6-alt2
- rebuild with perl 5.26

* Thu Aug 17 2017 Igor Vlasenko <viy@altlinux.ru> 6-alt1
- regenerated from template by package builder

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 5-alt1
- initial import by package builder

