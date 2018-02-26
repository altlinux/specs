%define dist Gnome2-VFS

Name: perl-%dist
Version: 1.081
Release: alt1.2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Gnome2-VFS Perl module
License: LGPLv2.1+
Group: Development/Perl

Url: %CPAN %dist
Source: http://www.cpan.org/modules/by-module/Gnome2/%dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: gnome-vfs-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Glib-devel perl-podlators

%package devel
Summary: Gnome2-VFS Perl module (development files)
License: LGPLv2.1+
Group: Development/Perl
Requires: %name = %version-%release
Requires: gnome-vfs-devel
# Gnome2/VFS/Install/Files.pm:deps
Requires: perl-Glib-devel

%description
This module allows you to use the GNOME Virtual File System library
(libgnomevfs for short) from Perl.

%description devel
This module allows you to use the GNOME Virtual File System library
(libgnomevfs for short) from Perl.

This package contains Gnome2-VFS development files and documentation
for developers (overview of internals and internal API reference).

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	NEWS README examples
%dir	%perl_vendor_archlib/Gnome2
	%perl_vendor_archlib/Gnome2/VFS.pm
	%perl_vendor_autolib/Gnome2/VFS

%files	devel
%dir 	%perl_vendor_archlib/Gnome2
%dir	%perl_vendor_archlib/Gnome2/VFS
%doc	%perl_vendor_archlib/Gnome2/VFS/*.pod
	%perl_vendor_archlib/Gnome2/VFS/Install

%doc	%perl_vendor_archlib/Gnome2/VFS/Async
%doc	%perl_vendor_archlib/Gnome2/VFS/DNSSD
%doc	%perl_vendor_archlib/Gnome2/VFS/Directory
%doc	%perl_vendor_archlib/Gnome2/VFS/Mime
%doc	%perl_vendor_archlib/Gnome2/VFS/Monitor
%doc	%perl_vendor_archlib/Gnome2/VFS/Resolve

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.081-alt1.2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.081-alt1.1
- rebuilt with perl 5.12

* Fri Oct 09 2009 Victor Forsyuk <force@altlinux.org> 1.081-alt1
- 1.081

* Tue Aug 16 2005 LAKostis <lakostis at altlinux.ru> 1.022-alt1
- 1.022.
- cleanup -devel.

* Wed Mar 16 2005 LAKostis <lakostis at altlinux.ru> 1.003-alt1.1
- cleanup buildreq/requires.

* Sun Mar 07 2005 LAkostis <lakostis at altlinux.ru> 1.003-alt1
- manual pages not packaged (use perldoc)
- first build for Sisyphus.

