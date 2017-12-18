%define _unpackaged_files_terminate_build 1
%define dist File-Fetch
Name: perl-%dist
Version: 0.56
Release: alt1

Summary: A generic file fetching mechanism
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BI/BINGOS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011 (-bi)
BuildRequires: perl-IPC-Cmd perl-Locale-Maketext perl-Locale-Maketext-Lexicon

%description
File::Fetch is a generic file fetching mechanism.  It allows you to fetch
any file pointed to by a "ftp", "http", "file", or "rsync" uri by a number
of different means.

%prep
%setup -q -n %{dist}-%{version}

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
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Thu Nov 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

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
