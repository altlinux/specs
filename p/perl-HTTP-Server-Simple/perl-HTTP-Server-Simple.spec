%define dist HTTP-Server-Simple
Name: perl-%dist
Version: 0.44
Release: alt1

Summary: Lightweight HTTP server
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-CGI perl-Module-Install perl-Test-Pod perl-Test-Pod-Coverage

%description
HTTP::Server::Simple is a very simple standalone HTTP daemon with no non-core
module dependencies. It's ideal for building a standalone http-based UI to
your existing tools.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.43 -> 0.44

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt2
- fix directory ownership violation

* Fri Jun 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt1
- new version 0.34 (with rpmrb script) (fix bug #15985)

* Fri Jun 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.33-alt1
- new version 0.33 (with rpmrb script)
- update requires

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt1
- first build for ALT Linux Sisyphus
