%define _unpackaged_files_terminate_build 1
%define dist File-BaseDir
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: Use the Freedesktop.org base directory specification
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/K/KI/KIMRYAN/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl(IPC/System/Simple.pm) perl(File/Which.pm)

%description
This module can be used to find directories and files as specified
by the Freedesktop.org Base Directory Specification. This specifications
gives a mechanism to locate directories for configuration, application
data and cache data. It is suggested that desktop applications for e.g.
the Gnome, KDE or Xfce platforms follow this layout. However, the same
layout can just as well be used for non-GUI applications.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File

%changelog
* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt2
- fixed unpackaged directory

* Fri Feb 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.03-alt1
- remove man pages instead exclude ones

* Mon Feb 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt0.1
- New version 0.03
- Spec file cleanup

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for ALT Linux Sisyphus
