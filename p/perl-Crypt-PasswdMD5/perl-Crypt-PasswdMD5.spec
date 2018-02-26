%define module Crypt-PasswdMD5
%define m_distro Crypt-PasswdMD5
%define m_name Term::ReadPassword
%define m_author_id unknown
%define _enable_test 1

Name: perl-Crypt-PasswdMD5
Version: 1.3
Release: alt3

Summary: Perl Crypt-PasswdMD5

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %m_distro-%version.tar.gz

BuildRequires: perl-devel

%description
the unix_md5_crypt() provides a crypt()-compatible interface to the rather new MD5-based crypt() function found in modern operating systems.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%dir %perl_vendor_privlib/Crypt
%perl_vendor_privlib/Crypt/*.pm

%changelog
* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt3
- Build repaired

* Mon Sep 01 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2
- Build repaired

* Fri Jun 29 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1
- Initial for Sisyphus
