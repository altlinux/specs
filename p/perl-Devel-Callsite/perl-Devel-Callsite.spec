%define module_name Devel-Callsite
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(B.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0.1
Release: alt4
Summary: Get caller return OP address and Perl interpreter context
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/R/RO/ROCKY/%{module_name}-%{version}.tar.gz

%description
The *callsite()* function returns the the OP address of the caller, a.number, one level up from where it was called. It's useful for
functions that need to uniquely know where they were called, such as
*Every::every()*; see the Every manpage. Or it can be used to pinpoint a location with finer granularity than a line number. In conjunction with
an OP tree disassembly you can know exactly where the caller is
located in the Perl source.

The *context()* function returns the interpreter context as a number.
This is a fairly unique number together with the call site.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Artistic gpl-2.0.txt Changes
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt4
- to Sisyphus as perl-Devel-Trepan dep

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt3
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2.1
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 1.0.1-alt1.1
- rebuild with perl 5.28.1

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- regenerated from template by package builder

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3
- rebuild with perl 5.26

* Sat Oct 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- updated summary

* Mon Mar 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt2
- rebuild to get rid of unmets

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

