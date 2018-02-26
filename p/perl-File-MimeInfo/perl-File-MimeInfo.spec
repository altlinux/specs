%define dist File-MimeInfo
Name: perl-%dist
Version: 0.15
Release: alt3

Summary: Determine file type
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: File-MimeInfo-0.15-rt-66841.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-File-DesktopEntry perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
This module can be used to determine the mime type of a file; it's
a replacement for File::MMagic trying to implement the freedesktop
specification for using the shared mime-info database.  The package
comes with a script called 'mimetype' that can be used as a file(1)
work-alike.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/mime*
%_man1dir/mime*
%perl_vendor_privlib/File

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt3
- patch tests from rt.cpan.org #66841

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt2
- fixed unpackaged directory

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- remove man3 pages instead exclude ones

* Mon Feb 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt0.1
- New version 0.15
- Spec fila cleanup

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- first build for ALT Linux Sisyphus
