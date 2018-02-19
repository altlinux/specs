%define _unpackaged_files_terminate_build 1
%define dist IPC-Cmd
Name: perl-%dist
Version: 1.00
Release: alt1

Summary: Finding and running system commands made easy
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BI/BINGOS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-IPC-Run perl-Module-Load-Conditional perl-devel

%description
IPC::Cmd allows you to run commands platform independently,
interactively if desired, but have them still work.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/IPC

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- automated CPAN update

* Sat Nov 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.88-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- automated CPAN update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.82-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.72-alt1
- 0.70 -> 0.72

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.70-alt1
- 0.56 -> 0.70

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Apr 10 2010 Kirill Maslinsky <kirill@altlinux.org> 0.56-alt1
- 0.56
- drop perl-IPC-Cmd-noload.patch

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt2
- fix directory ownership violation

* Sun Mar 30 2008 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1
- new version 0.40 (with rpmrb script)
- disable Win32 runtime detection
- disable tests, build without perl-Module-Load-Conditional

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0.36-alt1
- new version 0.36 (with rpmrb script)
- fix Url, Source URL, add doc files

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.24-alt1
- first build for ALT Linux Sisyphus
