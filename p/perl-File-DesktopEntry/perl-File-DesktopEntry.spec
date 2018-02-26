%define dist File-DesktopEntry
Name: perl-%dist
Version: 0.04
Release: alt2

Summary: Object to handle .desktop files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-File-BaseDir perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
This module is used to work with .desktop files.  The format of these files
is specified by the freedesktop "Desktop Entry" specification.  This module
can parse these files but also knows how to run the applciations defined by
these files.

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
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- fixed unpackaged directory

* Fri Feb 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- remove man pages instead exclude ones

* Mon Feb 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.04-alt0.1
- New version 0.04
- Spec file cleanup

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for ALT Linux Sisyphus
