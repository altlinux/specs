BuildRequires: perl-podlators
%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define module_name URI-UTF8-Punycode
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.05
Release: alt2.1
Summary: Punycode conversion of UTF-8 string.
Group: Development/Perl
License: gpl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/T/TW/TWINKLE/%{module_name}-%{version}.tar.gz
Patch: URI-UTF8-Punycode-1.05-perl5.26-add_test_dynamic.patch

%description
%summary

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %name


%prep
%setup -q -n %{module_name}-%{version}
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_archlib/U*
%perl_vendor_autolib/*

%files scripts
%_bindir/*
%_man1dir/*


%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2.1
- rebuild with new perl 5.26.1

* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2
- fix for perl5.26 (patch0)

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3.1
- rebuild with new perl 5.24.1

* Sat Sep 24 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3
- to Sisyphus

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 1.00-alt2
- rebuild to get rid of unmets

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial import by package builder

