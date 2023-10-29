%define _unpackaged_files_terminate_build 1
%define module_name WWW-Form-UrlEncoded
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(WWW/Form/UrlEncoded/XS.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.26
Release: alt2
Summary: parser and builder for application/x-www-form-urlencoded
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/WWW-Form-UrlEncoded

Source0: http://www.cpan.org/authors/id/K/KA/KAZEBURO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

# repack for noarch
rm %buildroot%perl_vendor_archlib/auto/WWW/Form/UrlEncoded/XS/.keep
rmdir %buildroot%perl_vendor_archlib/auto/WWW/Form/UrlEncoded/XS
rm %buildroot%perl_vendor_archlib/auto/WWW/Form/UrlEncoded/.packlist
mkdir -p %buildroot%perl_vendor_privlib
mv %buildroot%perl_vendor_archlib/WWW %buildroot%perl_vendor_privlib/

%files
%doc Changes README.md
%perl_vendor_privlib/W*

%changelog
* Sun Oct 29 2023 Igor Vlasenko <viy@altlinux.org> 0.26-alt2
- set BuildArch: noarch

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

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

