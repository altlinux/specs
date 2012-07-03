# via
%define module PerlIO-via-symlink
%define m_distro PerlIO-via-symlink
%define m_name PerlIO::via::symlink
%define m_author_id unknown
%define _enable_test 1

Name: perl-%module
Version: 0.05
Release: alt2.1

Summary: PerlIO layers for create symlinks

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/PerlIO-via-symlink-%version.tar.bz2
# Automatically added by buildreq on Tue Feb 21 2006
BuildRequires: perl-PerlIO perl-devel

%description
The PerlIO layer symlink allows you to create
a symbolic link by writing to the file handle.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_privlib/PerlIO/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt2
- fix directory ownership violation

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- initial build for ALT Linux Sisyphus

