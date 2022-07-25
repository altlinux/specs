%define _unpackaged_files_terminate_build 1
%define module_name HTTP-CookieJar
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(HTTP/Date.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Time/Local.pm) perl(URI.pm) perl(lib.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
# optional recommended
# BuildRequires: perl(Mozilla/PublicSuffix.pm)

BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.014
Release: alt1
Summary: A minimalist HTTP user agent cookie jar
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/HTTP-CookieJar

Source0: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/H*

%changelog
* Mon Jul 25 2022 Igor Vlasenko <viy@altlinux.org> 0.014-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 0.012-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.008-alt2
- to Sisyphus as perl-Dancer dep

* Sat Nov 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- regenerated from template by package builder

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- initial import by package builder

