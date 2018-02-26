%define dist libintl-perl
Name: perl-libintl
Version: 1.20
Release: alt1

Summary: High-Level Interface to Uniforum Message Translation
License: LGPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-libintl-1.20-alt-locale_dir.patch

# avoid rpmdb bloat
%add_findprov_skiplist */Locale/RecodeData/*

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Encode perl-devel

%description
The module Locale::TextDomain provides a high-level interface
to Perl message translation.

%prep
%setup -q -n %dist-%version
%patch -p1

# disable linking with -lintl -liconv
sed -i- '/LIBS/d' gettext_xs/Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README
%dir	%perl_vendor_privlib/Locale
	%perl_vendor_privlib/Locale/*.pm
%doc	%perl_vendor_privlib/Locale/*.pod
%dir	%perl_vendor_privlib/Locale/Recode
	%perl_vendor_privlib/Locale/Recode/*.pm
%dir	%perl_vendor_privlib/Locale/RecodeData
	%perl_vendor_privlib/Locale/RecodeData/*.pm
	%perl_vendor_autolib/Locale

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- 1.16 -> 1.20
- built for perl-5.12

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt3.1
- rebuilt with perl 5.12

* Sun Oct 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.16-alt3
- Fix FTBFS on current Sisyphus.

* Tue Oct 24 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.16-alt1
- 1.16 version.

* Sun Apr 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.11-alt2
- requires libdb4-devel for build.
- fixed default search path for .mo files. (#6285).

* Tue Jan 18 2005 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- initial revision
