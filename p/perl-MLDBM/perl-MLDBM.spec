%define dist MLDBM
Name: perl-%dist
Version: 2.04
Release: alt1

Summary: Multi-level hash structure storage for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch
Requires: perl(AnyDBM_File.pm)

# Automatically added by buildreq on Mon Apr 05 2010
BuildRequires: perl-DBM perl-FreezeThaw perl-Module-Build perl-Storable

%description
MLDBM -- the Perl module that can be used to store multidimensional
hash structures in tied hashes (including DBM files).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MLDBM*

%changelog
* Mon Apr 05 2010 Alexey Tourbin <at@altlinux.ru> 2.04-alt1
- 2.01 -> 2.04
- disabled AnyDBM_File.patch

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.01-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Nov 04 2004 Alexey Tourbin <at@altlinux.ru> 2.01-alt3
- patched to use AnyDBM_File instead of SDBM_File by default

* Mon Sep 08 2003 Alexey Tourbin <at@altlinux.ru> 2.01-alt2
- buildreq updated

* Fri Nov 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.01-alt1
- Rebuilt with new perl
- Some spec cleanup

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.00-ipl10mdk
- Specfile minor cleanup (get rid of useless arch subdirs).

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.00-ipl9mdk
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Fri Jan 26 2001 Alexander Bokovoy <ab@avilink.net> ipl8mdk
- Rebuild from scratch using MZh's spec skeleton file
