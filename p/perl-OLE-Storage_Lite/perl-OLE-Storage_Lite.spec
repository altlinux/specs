%define module OLE-Storage_Lite

Name: perl-%module
Version: 0.19
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Simple Class for OLE document interface
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/OLE/%module-%version.tar.gz

# Automatically added by buildreq on Mon Nov 29 2010
BuildRequires: perl-devel

BuildArch: noarch

%description
This module allows you to read and write an OLE-Structured file. The module
will work on the majority of Windows, UNIX and Macintosh platforms.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/OLE
%doc sample/*

%changelog
* Mon Nov 29 2010 Victor Forsiuk <force@altlinux.org> 0.19-alt2
- Fix build after perl 5.12 upgrade.

* Tue Dec 01 2009 Victor Forsyuk <force@altlinux.org> 0.19-alt1
- 0.19

* Thu Jun 19 2008 Victor Forsyuk <force@altlinux.org> 0.17-alt1
- 0.17

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- 0.15

* Fri Jul 27 2007 Victor Forsyuk <force@altlinux.org> 0.14-alt2
- Spec cleanups.

* Sun Feb 13 2005 Alexey Morozov <morozov@altlinux.org> 0.14-alt1
- New version (0.14)
- BuildReq's fixed 

* Thu Aug 26 2004 Alexey Morozov <morozov@altlinux.org> 0.13-alt1
- nw version (0.13)

* Thu Feb 26 2004 Alexey Morozov <morozov@altlinux.org> 0.11-alt1
- Initital ALTLinux build
