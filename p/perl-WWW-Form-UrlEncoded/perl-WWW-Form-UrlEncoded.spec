%define module_version 0.23
%define module_name WWW-Form-UrlEncoded
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(WWW/Form/UrlEncoded/XS.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.23
Release: alt2.1
Summary: parser and builder for application/x-www-form-urlencoded
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/WWW-Form-UrlEncoded

Source0: http://cpan.org.ua/authors/id/K/KA/KAZEBURO/%{module_name}-%{module_version}.tar.gz
#BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README.md
%perl_vendor_archlib/W*
%perl_vendor_autolib/W*

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2.1
- to Sisyphus

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- rebuild with perl 5.22

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- regenerated from template by package builder

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- regenerated from template by package builder

* Mon Dec 15 2014 Cronbuild Service <cronbuild@altlinux.org> 0.19-alt2
- rebuild to get rid of unmets

* Thu May 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- initial import by package builder

