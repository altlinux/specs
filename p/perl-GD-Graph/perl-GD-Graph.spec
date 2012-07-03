%define dist GDGraph
Name: perl-GD-Graph
Version: 1.44
Release: alt2
Epoch: 1

Summary: Create charts using GD
Group: Development/Perl
License: GPL or Artistic

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-GD-Text perl-devel

%description
This is GDGraph, a package to generate charts, using Lincoln Stein's
GD.pm. See the documentation for some history and more information.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/GD

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 1:1.44-alt2
- rebuilt

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Sep 30 2008 Afanasov Dmitry <ender@altlinux.org> 1.44-alt1
- back to 1.44 release due to unmets

* Mon Sep 29 2008 Afanasov Dmitry <ender@altlinux.org> 1.4401-alt1
- pick orphaned package and specify Packager
- 1.4401 release
- fix BuildRequires
- remove Requires due to hope in automatic search

* Sat Mar 25 2006 Andrey Brindeew <abr@altlinux.org> 1.4307-alt1
- 1.4307 release

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.43-alt7.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt7
- Summary tag was fixed.

* Wed Aug 13 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt6
- BuildArch was changed to `noarch'.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt5
- Fixed BuildRequires list using buildreq

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt4
- Applied patch from at@

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt3
- Fixed Requires list.

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt2
- {,Build}Reqires lists updated.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt1
- First build for ALTLinux.


