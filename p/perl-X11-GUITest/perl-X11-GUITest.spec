%define dist X11-GUITest
Name: perl-%dist
Version: 0.25
Release: alt2

Summary: Collection of functions for X11 GUI testing/interaction
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: libXt-devel libXtst-devel perl-devel perl-podlators

%description
This Perl package is intended to facilitate the testing of GUI
applications by means of user emulation.  It can be used to
test/interact with GUI applications; which have been built upon
the X library or toolkits (i.e., GTK+, Xt, Qt, Motif, etc.) that
"wrap" the X library's functionality.

%prep
%setup -q -n %dist-%version

# do not override default CCFLAGS
sed -i- '/CCFLAGS/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc docs/Changes
%perl_vendor_archlib/X11
%perl_vendor_autolib/X11

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.25-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.21-alt2.1
- rebuilt with perl 5.12

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 0.21-alt2
- updated BuildRequires

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.20 -> 0.21
- all patches merged upstream (cpan #13682, #13684)

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- initial revision
- License: GPL
- cvs-20041024.patch
- XK_Alt_L.patch: fall back to XK_Meta_L (cpan #13682)
- StartApp.patch: more accurate application startup (cpan #13684)
