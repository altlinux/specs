%define dist Panotools-Script
Name: perl-%dist
Version: 0.28
Release: alt2

Summary: Panorama Tools scripting
License: GPLv2+
Group: Graphics
Packager: Dmitry Derjavin <dd@altlinux.org>
Requires: zenity

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BP/BPOSTLE/Panotools-Script-%{version}.tar.gz
Patch: Panotools-Script-0.28-perl-syntax.patch
# Restore compatibility with Perl 5.26.0, CPAN RT#117275
Patch1: Panotools-Script-0.28-Escape-literal-curly-bracket-in-a-regexp.patch

BuildArch: noarch

BuildRequires: perl-devel perl-libwww perl-Image-ExifTool perl-Image-Size perl-Storable perl-Magick perl-GraphViz perl-Math-Complex perl-Pod-Parser

%description
A perl module and utilities for reading, writing and manipulating
hugin script files. http://hugin.sourceforge.net/

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1

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
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2
- fixed build with new perl 5.26

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Sun Nov 21 2010 Dmitry Derjavin <dd@altlinux.org> 0.25-alt3
- Man pages fix for building in new ALTLinux perl environment.

* Sun Nov 21 2010 Dmitry Derjavin <dd@altlinux.org> 0.25-alt2
- BuildRequires fix for building in new ALTLinux perl environment.

* Tue Jul 27 2010 Dmitry Derjavin <dd@altlinux.org> 0.25-alt1
- initial ALTLinux build.
