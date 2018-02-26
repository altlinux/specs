%define dist File-ShareDir
Name: perl-%dist
Version: 1.03
Release: alt2

Summary: Locate per-dist and per-module shared files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Class-Inspector perl-Pod-Escapes perl-devel

%description
The intent of File::ShareDir is to provide a companion to
Class::Inspector and File::HomeDir, modules that take a process that is
well-known by advanced Perl developers but gets a little tricky, and
make it more available to the larger Perl community.

Quite often you want or need your Perl module (CPAN or otherwise) to
have access to a large amount of read-only data that is stored on the
file-system at run-time.

On a linux-like system, this would be in a place such as /usr/share,
however Perl runs on a wide variety of different systems, and so the use
of any one location is unreliable.

Perl provides a little-known method for doing this, but almost nobody is
aware that it exists. As a result, module authors often go through some
very strange ways to make the data available to their code.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2
- rebuilt

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Fri Jan 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt1
- NMU: New version 1.01

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt2
- fix directory ownership violation

* Thu Jan 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus

