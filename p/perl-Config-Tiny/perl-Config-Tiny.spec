%define _unpackaged_files_terminate_build 1
%define dist Config-Tiny
Name: perl-%dist
Version: 2.20
Release: alt1

Summary: Read/Write .ini style files with as little code as possible
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-%{version}.tgz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 26 2011
BuildRequires: perl-devel perl(Module/Build.pm)

%description
Config::Tiny is a perl class to read and write .ini style configuration
files with as little code as possible, reducing load time and memory
overhead. Most of the time it is accepted that Perl applications use
a lot of memory and modules. The ::Tiny family of modules is specifically
intended to provide an ultralight alternative to the standard modules.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Config

%changelog
* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1
- automated CPAN update

* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 2.14-alt1
- 2.12 -> 2.14

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Jan 19 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- new version 2.12 (with rpmrb script)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt1
- first build for ALT Linux Sisyphus
