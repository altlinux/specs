%define dist Proc-Daemon
Name: perl-%dist
Version: 0.14
Release: alt1

Summary: Run Perl program as a daemon process
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DE/DETI/Proc/Proc-Daemon-0.14.tar.gz

Buildarch: noarch

# Automatically added by buildreq on Mon Apr 25 2011
BuildRequires: perl-devel

%description
Proc::Daemon provides the capability for a Perl program to run
as a Unix daemon process.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Proc

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- 0.03 -> 0.10

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.03-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 0.03-alt3
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 0.03-alt2
- Minor specfile fixes.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 0.03-alt1
- First build for ALTLinux.
- new version 0.03
