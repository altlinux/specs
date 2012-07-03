Name: perl-Dancer-Plugin-Database
Version: 1.81
Release: alt1
Summary: Dancer::Plugin::Database - easy database connections for Dancer applications

Group: Development/Perl
License: Perl
Url: %CPAN Dancer-Plugin-Database

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-DBI perl-Dancer

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Dancer/Plugin/Database*
%doc Changes README 

%changelog
* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 1.81-alt1
- New version 1.81

* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 1.51-alt1
- New version 1.51

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Mon Feb 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt1
- initial build
