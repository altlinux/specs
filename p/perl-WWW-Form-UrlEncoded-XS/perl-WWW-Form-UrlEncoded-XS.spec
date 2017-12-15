%define _unpackaged_files_terminate_build 1
%define module_name WWW-Form-UrlEncoded-XS
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Exporter.pm) perl(JSON.pm) perl(Module/Build/Tiny.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.24
Release: alt1.1
Summary: XS implementation of parser and builder for application/x-www-form-urlencoded
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/WWW-Form-UrlEncoded-XS

Source0: http://www.cpan.org/authors/id/K/KA/KAZEBURO/%{module_name}-%{version}.tar.gz

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README.md
%perl_vendor_archlib/W*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1.1
- rebuild with new perl 5.26.1

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2.1.1
- rebuild with new perl 5.24.1

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2.1
- to Sisyphus

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- rebuild with perl 5.22

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- regenerated from template by package builder

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- regenerated from template by package builder

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.20-alt2
- rebuild to get rid of unmets

* Mon Nov 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- regenerated from template by package builder

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- initial import by package builder

