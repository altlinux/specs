%define module File-Flat
%define m_distro File-Flat
%define m_name File::Flat
%define m_author_id ADAMK
%define _enable_test 1

Name: perl-File-Flat
Version: 1.04
Release: alt1.1

Summary: File::Flat - Implements a flat filesystem

Group: Development/Perl
License: Artistic
Url: http://search.cpan.org/~adamk/File-Flat-1.00/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/A/AD/ADAMK/File-Flat-1.04.tar.gz

# Automatically added by buildreq on Sun Jul 22 2007
BuildRequires: perl-File-Copy-Recursive perl-File-Remove perl-File-Slurp perl-Module-Install perl-prefork perl-Test-ClassAPI

%description
File::Flat implements a flat filesystem. A flat filesystem is a
filesystem in which directories do not exist. It provides an abstraction
over any normal filesystem which makes it appear as if directories do
not exist. In effect, it will automatically create directories as
needed. This is create for things like install scripts and such, as you
never need to worry about the existance of directories, just write to a
file, no matter where it is.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt2
- fix directory ownership violation

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt1
- new version 1.00 (with rpmrb script)
- update buildreq, fix Url, fix Source URL, add doc files

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt1
- first build for ALT Linux Sisyphus
