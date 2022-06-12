%define _unpackaged_files_terminate_build 1
%define dist Mojolicious-Plugin-Authentication

Name: perl-%dist
Version: 1.39
Release: alt1
Summary: A plugin to make authentication a bit easier

Group: Development/Perl
License: Perl
Url: %CPAN %dist

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/J/JJ/JJATRIA/%{dist}-%{version}.tar.gz
BuildRequires: perl-Module-Build perl-Mojolicious

%description
%summary

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
rm -f %buildroot/%perl_vendor_privlib/Mojolicious/Plugin/README.pod

%files
%doc Changes README.md
%perl_vendor_privlib/Mojolicious/Plugin/*.pm

%changelog
* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 1.39-alt1
- automated CPAN update

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 1.38-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 1.37-alt1
- automated CPAN update

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 1.36-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Sun Mar 11 2012 Eugene Prokopiev <enp@altlinux.ru> 1.21-alt1
- initail build for Sisyphus

