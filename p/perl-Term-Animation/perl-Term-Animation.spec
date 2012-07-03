%define dist Term-Animation
Name: perl-%dist
Version: 2.6
Release: alt1

Summary: ASCII sprite animation framework
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 24 2011
BuildRequires: perl-Curses perl-devel

%description
This module provides a framework to produce sprite animations using
ASCII art. Each ASCII 'sprite' is given one or more frames, and placed
into the animation as an 'animation object'. An animation object can
have a callback routine that controls the position and frame of the
object. The module can also do collision detection between entities.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README MIGRATION
%dir %perl_vendor_privlib/Term
%dir %perl_vendor_privlib/Term/Animation
%perl_vendor_privlib/Term/Animation.pm
%perl_vendor_privlib/Term/Animation/Entity.pm

%changelog
* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 2.6-alt1
- 2.4 -> 2.6

* Thu Jan 04 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4-alt1
- 2.4

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.3-alt1
- 2.3

* Mon Sep 19 2005 Andrey Rahmatullin <wrar@altlinux.ru> 2.1-alt1
- initial build
