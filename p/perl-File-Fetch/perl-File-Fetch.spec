%define dist File-Fetch
Name: perl-%dist
Version: 0.32
Release: alt1

Summary: A generic file fetching mechanism
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011 (-bi)
BuildRequires: perl-IPC-Cmd perl-Locale-Maketext perl-Locale-Maketext-Lexicon

%description
File::Fetch is a generic file fetching mechanism.  It allows you to fetch
any file pointed to by a "ftp", "http", "file", or "rsync" uri by a number
of different means.

%prep
%setup -q -n %dist-%version

%build
# disable live tests
export PERL_CORE=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/File

%changelog
* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.32-alt1
- 0.14 -> 0.32

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt2
- fix directory ownership violation

* Fri Jun 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt1
- new version 0.14 (with rpmrb script)
- update buildreq

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- new version 0.10 (with rpmrb script)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- first build for ALT Linux Sisyphus
