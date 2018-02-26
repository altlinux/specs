%define dist Config-Tiny
Name: perl-%dist
Version: 2.14
Release: alt1

Summary: Read/Write .ini style files with as little code as possible
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 26 2011
BuildRequires: perl-devel

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
* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 2.14-alt1
- 2.12 -> 2.14

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Jan 19 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- new version 2.12 (with rpmrb script)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt1
- first build for ALT Linux Sisyphus
