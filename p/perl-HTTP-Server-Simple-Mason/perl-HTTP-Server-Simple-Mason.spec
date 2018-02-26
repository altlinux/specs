%define module HTTP-Server-Simple-Mason

Name: perl-%module
Version: 0.14
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A simple mason server
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Mar 10 2010
BuildRequires: perl-HTML-Mason perl-HTTP-Server-Simple perl-Hook-LexWrap perl-Log-Agent perl-Module-Install perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

%description
HTTP::Server::Simple::Mason - An abstract baseclass for a standalone mason server.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTTP/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 0.14-alt1
- 0.14

* Wed Mar 10 2010 Victor Forsiuk <force@altlinux.org> 0.13-alt1
- 0.13

* Sun Dec 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- new version 0.11 (with rpmrb script)
- fix directory ownership violation
- disable man packaging
- change packager

* Sun Apr 13 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.09-alt1
- Build for Sisyphus (thanks to Igor Zubkov <icesik@altlinux.org>)

