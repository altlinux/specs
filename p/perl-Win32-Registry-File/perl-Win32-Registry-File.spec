%define module Win32-Registry-File
%define m_name Win32::Registry::File

Name: perl-%module
Version: 1.10
Release: alt4.1.1

Packager: Andrey Brindeew <abr@altlinux.ru>

Summary: Perl interface to MS-Windows registry files
License: GPL or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/%module/

Source: http://www.cpan.org/authors/id/A/AV/AVATAR/%module-%version.tar.gz
BuildArch: noarch

BuildPreReq: perl-Tie-IxHash >= 1.21

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-Tie-IxHash perl-devel

%description
This package provides easy access to MS-Windows style .ini
files, Unreal style extended .ini files (where multiple values
can be associated with a single key), as well as registry
files with automatic conversion from native Perl to Windows
registry data encoding and vice versa.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Win32*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.10-alt4.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.10-alt4.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Oct 06 2003 Andrey Brindeew <abr@altlinux.ru> 1.10-alt4
- Both Packager & Summary tags was updated
- Url tag was added

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.10-alt3
- rebuild with new perl

* Mon Oct 21 2002 Stanislav Ievlev <inger@altlinux.ru> 1.10-alt2
- rebuild with gcc3
- added packager tag.

* Mon Jun 10 2002 Sir Raorn <raorn@altlinux.ru> 1.10-alt1
- Built for Sisyphus
