%define dist qa-rpmelfsym
Name: perl-%dist
Version: 0.11
Release: alt2

Summary: Faster rpmelfsym(1) and bad_elf_symbols implementation
License: GPLv2+
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

# Automatically added by buildreq on Mon Oct 10 2011 (-bi)
BuildRequires: perl-File-LibMagic perl-devel perl-qa-cache

%description
no description

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# MakeMaker sucks (and I don't know how to tweak it)
rm %buildroot%perl_vendor_archlib/qa/*.pl

%files
%_bindir/*.pl
%perl_vendor_archlib/qa*
%perl_vendor_autolib/qa*

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt2
- rebuilt for perl-5.14

* Sun Sep 11 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- qa/rpmelfsym.pm: implemented parallel collect_bad_elfsym routine
- bad_elf_symbols_dircmp.pl: optimized def0 usage for parallel join

* Thu Sep 08 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- changed internal data format to argz blob
- rewritten bad_elf_symbols inner loop in XS

* Sun Feb 06 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- qa/rpmelfsym.pm: ignore *.debug files under /usr/lib/debug
- bad_elf_symbols*.pl: added support for "i" indirect functions

* Tue Aug 10 2010 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- bad_elf_symbols*.pl: handle unique global symbols (Dmitry V. Levin)

* Tue Apr 07 2009 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- switched to (rpm-basename,size,mtime) caching mode
- flattened down internal data structure, for efficiency
- reverted piping to sort(1) and other optimizations proved inefficient
- optimized by saving (rpm-basename,filename) in a separate file
- optimized by eliminating huge 'sort -m' merges

* Fri Apr 03 2009 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- optimized inner loop writes for speed

* Wed Apr 01 2009 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- bad_elf_symbols*.pl: optimize by running sort(1) in background

* Sun Feb 22 2009 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- rpmelfsym.pm: fixed ELF magic check for nm(1)

* Fri Feb 20 2009 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- implemented bad_elf_symbols_dircmp.pl, for use in girar-builder

* Thu Feb 19 2009 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- rpmelfsym.pm: better handling of tmp write errors

* Wed Feb 18 2009 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- initial revision
