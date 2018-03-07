%define _unpackaged_files_terminate_build 1
Epoch: 1
%define dist CGI-Simple
Name: perl-%dist
Version: 1.15
Release: alt1.1

Summary: A Simple totally OO CGI interface that is CGI.pm compliant 
License: Artistic and GPL
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MANWAR/%{dist}-%{version}.tar.gz
Patch: perl-CGI-Simple-1.112-alt-mod_perl.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Mar 16 2011 (-bi)
BuildRequires: perl-IO-stringy perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-libwww perl(Test/Exception.pm) perl(Test/NoWarnings.pm)

%description
CGI::Simple provides a relatively lightweight drop in
replacement for CGI.pm. It shares an identical OO interface to
CGI.pm for parameter parsing, file upload, cookie handling and
header generation. This module is entirely object oriented,
however a complete functional interface is available by using
the CGI::Simple::Standard module.

%prep
%setup -q -n %{dist}-%{version}
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CGI*

%changelog
* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.15-alt1.1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.115-alt1
- automated CPAN update

* Wed Mar 16 2011 Alexey Tourbin <at@altlinux.ru> 1.113-alt1
- 1.112 -> 1.113

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.112-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Apr 04 2010 Alexey Tourbin <at@altlinux.ru> 1.112-alt1
- 1.105 -> 1.112

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 1.105-alt1
- 1.105 version build
- fix directory ownership violation

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 0.079-alt1
- first build for ALT Linux Sisyphus

