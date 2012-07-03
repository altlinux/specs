%define dist ExtUtils-F77
Name: perl-%dist
Version: 1.17
Release: alt1

Summary: Simple interface to F77 libs
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: gcc-fortran perl-devel

%description
Simple interface to F77 libs.  Used to be in perl-PDL, but isn't anymore.

This module tries to figure out how to link C programs with
Fortran subroutines on your system. Basically one must add a list
of Fortran runtime libraries. The problem is their location
and name varies with each OS/compiler combination!

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

: show configuration
perl -Mblib -MExtUtils::F77 -e1

: try to compile hello world
cat <<__EOF__ >hello.f
      PROGRAM HELLO
      DO 10, I=1,10
      PRINT *,'Hello World'
10    CONTINUE
      STOP
      END
__EOF__

%define _g77() perl -Mblib -MExtUtils::F77 -e 'print ExtUtils::F77::%1()' |tail -1
`%{_g77 compiler}` hello.f
./a.out

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/ExtUtils

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.17-alt1
- 1.15 -> 1.17

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.14 -> 1.15
- patched for gfortran

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.14-alt4.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Oct 31 2003 Alexey Tourbin <at@altlinux.ru> 1.14-alt4
- g77-flags.patch:
  + support for shared libraries added (fixes libg2c detection)
  + use perl/gcc optimization flags
- hello world compilation test added to unsure things work
- additional spec conventions enforcement

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.14-alt3
- rebuild with new perl

* Mon Jun 25 2001 AEN <aen@logic.ru> 1.14-alt1
- rebuild with new perl

* Fri Jun 20 2001 Grigory Milev <week@altlinux.ru> 1.14-alt1
- new version (1.14)

* Fri Jun 15 2001 Grigory Milev <week@altlinux.ru> 1.13-alt1
- Spec rewritten for compatibility with new policy

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 1.13-3mdk
- build release.

* Tue Aug  1 2000 Alexander Skwar <ASkwar@DigitalProjects.com> 1.13-2mdk
- Added requirement for a Fortran77 compiler as this package makes no
  sense without one

* Mon Jul 31 2000 Alexander Skwar <ASkwar@DigitalProjects.com> 1.13-1mdk
- First Mandrake package
- This used to be in PDL

# end of file
