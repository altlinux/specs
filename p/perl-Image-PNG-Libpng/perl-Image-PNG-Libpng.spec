%define module_name Image-PNG-Libpng

Name: perl-Image-PNG-Libpng
Version: 0.48
Release: alt2

Summary: Perl interface to libpng

Group: Development/Perl
License: perl
Url: %CPAN %module_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BK/BKB/%module_name-%version.tar

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(Scalar/Util.pm) perl(XSLoader.pm) perl(parent.pm) pkgconfig(libpng)

%description
Perl interface to libpng.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %EVR

BuildArch: noarch

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_archlib/I*
%perl_vendor_autolib/*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Wed Dec 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt2
- human build for ALT Sisyphus
- drop BR:libsowing-devel

* Sun Nov 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- updated by package builder

* Wed Oct 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- updated by package builder

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.46-alt2.1
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.46-alt1.1
- rebuild with perl 5.28.1

* Sat Sep 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- regenerated from template by package builder

* Sun Jan 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- regenerated from template by package builder

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.44-alt2
- rebuild with perl 5.26

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.43-alt2
- rebuild to get rid of unmets

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- regenerated from template by package builder

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1.1
- rebuild with perl 5.22

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- regenerated from template by package builder

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.39-alt2
- rebuild to get rid of unmets

* Wed Oct 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- regenerated from template by package builder

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- regenerated from template by package builder

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- initial import by package builder

