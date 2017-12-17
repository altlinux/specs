%define _unpackaged_files_terminate_build 1
%define dist Gnome2-VFS

Name: perl-%dist
Version: 1.083
Release: alt1.1

Summary: Gnome2-VFS Perl module
License: LGPLv2.1+
Group: Development/Perl

Url: %CPAN %dist
Source0: http://www.cpan.org/authors/id/X/XA/XAOC/%{dist}-%{version}.tar.gz

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
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	NEWS README examples ChangeLog.pre-git copyright.pod
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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.083-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.083-alt1
- automated CPAN update

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1.3
- enabled test

* Fri Feb 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1.2.1
- rebuild with new perl 5.24.1

* Fri Feb 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1.2
- disabled test during 5.24.1 upgrade

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1.1
- rebuild with new perl 5.20.1

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.081-alt3
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.081-alt2
- rebuilt for perl-5.16

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

