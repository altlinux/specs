%define dist Alien-SDL
Name: perl-%dist
Version: 1.428
Release: alt1

Summary: Building, finding and using SDL binaries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/F/FR/FROGGS/Alien-SDL-1.428.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: libSDL-devel libsmpeg-devel perl-Archive-Extract perl-Archive-Tar perl-Archive-Zip perl-Capture-Tiny perl-Digest-SHA perl-File-Fetch perl-File-ShareDir perl-File-Which perl-Locale-Maketext-Lexicon perl-Module-Build perl-Text-Patch

%description
Alien::SDL can be used to detect and get configuration settings from an
installed SDL and related libraries.  Based on your platform it offers the
possibility to download and install prebuilt binaries or to build SDL & co.
from source codes.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build --with-sdl-config

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Alien

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.428-alt1
- automated CPAN update

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 1.425-alt1
- initial revision
