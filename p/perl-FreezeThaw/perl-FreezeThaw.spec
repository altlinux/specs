%define dist FreezeThaw
Name: perl-%dist
Version: 0.5001
Release: alt1

%if "%version" == "0.50"
%define version 0.5001
%endif

Summary: Converting Perl structures to strings and back
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/I/IL/ILYAZ/modules/FreezeThaw-0.5001.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 22 2010
BuildRequires: perl-Math-BigInt perl-devel

%description
Converts data to/from stringified form, appropriate for
saving-to/reading-from permanent storage.

Deals with objects, circular lists, repeated appearence
of the same refence. Does not deal with overloaded stringify
operator yet.

%prep
%setup -q -n %dist-%version
chmod -c 644 FreezeThaw.pm Changes README

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/FreezeThaw.pm

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.5001-alt1
- automated CPAN update

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 0.50-alt1
- 0.45 -> 0.5001

* Sat Mar 07 2009 Alexey Tourbin <at@altlinux.ru> 0.45-alt1
- 0.43 -> 0.45

* Wed Dec 15 2004 Andrey Brindeew <abr@altlinux.org> 0.43-alt3
- perl-Math-BigInt added to BuildRequires

* Tue Oct 07 2003 Andrey Brindeew <abr@altlinux.ru> 0.43-alt2
- Added Packager tag
- Both Summary and Description tags was updated

* Fri Nov 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.43-alt1
- First build for Sisyphus

