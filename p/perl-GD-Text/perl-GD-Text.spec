# Tests for this module _may_ by unsuccessfull, this is normal. See README
# in sources for explanation.
%def_without test

%define dist GDTextUtil
Name: perl-GD-Text
Version: 0.86
Release: alt7

Summary: Text utilities for use with the GD drawing package
License: GPL or Artisic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-GD perl-devel

%description
This package provides three modules that make it possible to work with
internal GD fonts as well as TrueType fonts, without having to worry
about different interface functions to call. Apart from an abstract
interface to all font types and strings for GD, this library also
provides some utility in aligning and wrapping your string.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/GD

%changelog
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.86-alt7
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.86-alt6.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 08 2007 Victor Forsyuk <force@altlinux.org> 0.86-alt6
- Adopted from orphanage.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.86-alt5.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 0.86-alt5
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 0.86-alt4
- Fixed Requires & Buildarch tags.

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 0.86-alt3
- Minor specfile fixes.

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 0.86-alt2
- Included demos. TTF excluded.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 0.86-alt1
- First build for ALTLinux.
