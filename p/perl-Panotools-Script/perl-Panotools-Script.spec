%define dist Panotools-Script
Name: perl-%dist
Version: 0.26
Release: alt1

Summary: Panorama Tools scripting
License: GPLv2+
Group: Graphics
Packager: Dmitry Derjavin <dd@altlinux.org>
Requires: zenity

URL: %CPAN %dist
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires: perl-devel perl-libwww perl-Image-ExifTool perl-Image-Size perl-Storable perl-Magick perl-GraphViz perl-Math-Complex perl-Pod-Parser

%description
A perl module and utilities for reading, writing and manipulating
hugin script files. http://hugin.sourceforge.net/

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
#/bin/mv %buildroot%_usr/man/man1 %buildroot%_mandir/

%files
%doc Changes README
%_bindir/*
%_man1dir/*

%perl_vendor_privlib/Panotools
#%perl_vendor_autolib/Panotools

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Sun Nov 21 2010 Dmitry Derjavin <dd@altlinux.org> 0.25-alt3
- Man pages fix for building in new ALTLinux perl environment.

* Sun Nov 21 2010 Dmitry Derjavin <dd@altlinux.org> 0.25-alt2
- BuildRequires fix for building in new ALTLinux perl environment.

* Tue Jul 27 2010 Dmitry Derjavin <dd@altlinux.org> 0.25-alt1
- initial ALTLinux build.
