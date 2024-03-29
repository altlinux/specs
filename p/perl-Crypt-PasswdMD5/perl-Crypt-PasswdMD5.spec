%define _unpackaged_files_terminate_build 1
%define module Crypt-PasswdMD5
%define m_distro Crypt-PasswdMD5
%define m_name Term::ReadPassword
%define m_author_id unknown
%define _enable_test 1

Name: perl-Crypt-PasswdMD5
Version: 1.42
Release: alt1

Summary: Perl Crypt-PasswdMD5

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/R/RS/RSAVAGE/%{module}-%{version}.tgz

BuildRequires: perl-devel perl(Module/Build.pm)

%description
the unix_md5_crypt() provides a crypt()-compatible interface to the rather new MD5-based crypt() function found in modern operating systems.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changelog.ini Changes
%dir %perl_vendor_privlib/Crypt
%perl_vendor_privlib/Crypt/*.pm

%changelog
* Sat Jul 16 2022 Igor Vlasenko <viy@altlinux.org> 1.42-alt1
- automated CPAN update

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- automated CPAN update

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt3
- Build repaired

* Mon Sep 01 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2
- Build repaired

* Fri Jun 29 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1
- Initial for Sisyphus
