# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define module_version 0.08
%define module_name Taint-Util
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators rpm-build-licenses

Name: perl-%module_name
Version: 0.08
Release: alt7
Summary: Test for and flip the taint flag without regex matches or C<eval>
Group: Development/Perl
License: %perl_license
URL: http://search.cpan.org/dist/Taint-Util/

Source0: http://cpan.org.ua/authors/id/A/AV/AVAR/%module_name-%module_version.tar

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE ChangeLog README
%perl_vendor_archlib/T*
%perl_vendor_autolib/*

%changelog
* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 0.08-alt7
- rebuild by human.

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.08-alt6
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.08-alt5.1
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt4.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt4
- rebuild with perl 5.26

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt2
- rebuild to get rid of unmets

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt1.1
- rebuild with new perl

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

