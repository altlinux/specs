%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/ParseXS.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Number/Delta.pm) perl(Test/Requires.pm) perl(Time/HiRes.pm) perl(XSLoader.pm) perl(YAML/Tiny.pm)
# END SourceDeps(oneline)
%define module_name Time-Moment
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.42
Release: alt1.1
Summary: Represents a date and time of day with an offset from UTC
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/C/CH/CHANSEN/%{module_name}-%{version}.tar.gz

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/T*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1.1
- rebuild with new perl 5.24.1

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt2
- regenerated from template by package builder

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- regenerated from template by package builder

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1.1
- rebuild with perl 5.22

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- regenerated from template by package builder

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.21-alt2
- rebuild to get rid of unmets

* Mon Nov 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- regenerated from template by package builder

* Mon Nov 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- regenerated from template by package builder

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- regenerated from template by package builder

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- regenerated from template by package builder

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- regenerated from template by package builder

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- initial import by package builder

