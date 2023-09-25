%define _unpackaged_files_terminate_build 1
%define module Parse-PlainConfig
%define intmodule Parse-PlainConfig
%define m_name Parse::PlainConfig

Name: perl-%module
Version: 3.06
Release: alt1

Summary: Plain Config parser
License: GPLv2+
Group: Development/Perl
BuildArch: noarch
Url: %CPAN %module
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: http://www.cpan.org/authors/id/C/CO/CORLISS/%{module}/Parse-PlainConfig-%{version}.tar.gz

# Automatically added by buildreq on Mon Oct 06 2003
BuildRequires: perl-devel perl(Paranoid.pm) perl(Text/ParseWords.pm) perl(Text/Tabs.pm) perl(Class/EHierarchy.pm)

%description
Parse::PlainConfig provides OO objects which can parse and generate human-readable configuration files.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGELOG
%perl_vendor_privlib/Parse*

%changelog
* Mon Sep 25 2023 Igor Vlasenko <viy@altlinux.org> 3.06-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 3.05-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.03-alt1
- automated CPAN update

* Fri May 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.02-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.01-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.06-alt1
- New version

* Thu Dec 21 2006 Sergei Epiphanov <serpiph@altlinux.ru> 1.7a-alt1
- Built for Sisyphus
