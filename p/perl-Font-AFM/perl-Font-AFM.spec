## SPEC file for Perl module Font::AFM

Name: perl-Font-AFM
Version: 1.20
Release: alt1.1

Summary: Perl interface to Adobe Font Metrics files

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~gaas/Font-AFM/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Font-AFM
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

%description
This module implements the Font::AFM class. Objects of this
class are initialised from an AFM-file and allows you to obtain
information about the font and the metrics of the various glyphs
in the font.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
%__subst 's@^#!/usr/local/bin/perl@#!/usr/bin/perl@' make_metrics
chmod a-x make_metrics

%files
%doc Changes make_metrics
%perl_vendor_privlib/Font*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.20-alt1
- New version
- Picked up from orphaned

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.19-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun May 09 2004 Alexey Tourbin <at@altlinux.ru> 1.19-alt1
- 1.18 -> 1.19 (documentation fixes)

* Fri Oct 17 2003 Alexey Tourbin <at@altlinux.ru> 1.18-alt1
- inital revision (this module is required by HTML::Format)
