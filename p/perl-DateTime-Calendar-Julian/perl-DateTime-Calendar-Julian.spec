%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime.pm) perl(DateTime/Locale.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_name DateTime-Calendar-Julian
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.107
Release: alt1
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/W/WY/WYANT/%{module_name}-%{version}.tar.gz
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
%doc Changes README
%perl_vendor_privlib/D*

%changelog
* Wed Feb 02 2022 Igor Vlasenko <viy@altlinux.org> 0.107-alt1
- automated CPAN update

* Tue Oct 05 2021 Igor Vlasenko <viy@altlinux.org> 0.106-alt1
- automated CPAN update

* Mon Sep 06 2021 Igor Vlasenko <viy@altlinux.org> 0.105-alt1
- automated CPAN update

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0.104-alt2
- fixed build

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 0.104-alt1
- automated CPAN update

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 0.103-alt1
- automated CPAN update

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.102-alt1
- automated CPAN update

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.101-alt1
- automated CPAN update

* Sat Dec 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.100-alt1
- automated CPAN update

* Sun Jan 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- to Sisyphus as biber dep

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

