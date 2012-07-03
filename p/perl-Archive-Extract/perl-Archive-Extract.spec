%define dist Archive-Extract
Name: perl-%dist
Version: 0.56
Release: alt1

Summary: A generic archive extracting mechanism
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Archive-Extract-0.56.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: perl-Archive-Tar perl-Archive-Zip perl-IPC-Cmd perl-Locale-Maketext perl-Locale-Maketext-Lexicon unzip xz

%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz, .gz,
.Z, tar.bz2, .tbz, .bz2, .zip, .xz,, .txz, .tar.xz or .lzma without having
to worry how it does so, or use different interfaces for each type by using
either perl modules, or commandline tools on your system.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Archive

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.48-alt1
- 0.42 -> 0.48

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.26-alt2
- fix directory ownership violation

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 0.26-alt1
- new version 0.26 (with rpmrb script)

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0.22-alt1
- new version 0.22 (with rpmrb script)
- add Url, add doc files

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- first build for ALT Linux Sisyphus
