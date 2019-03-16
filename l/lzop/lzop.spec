Name: lzop
Version: 1.04
Release: alt1

Summary: LZO fast file compressor
License: GPL-2.0-or-later
Group: Archiving/Compression
Url: https://www.lzop.org/
# https://www.lzop.org/download/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: liblzo2-devel

%description
lzop is a file compressor similar to gzip.  Its main advantages over
gzip are much higher compression and decompression speed (at the cost
of some compression ratio).

%prep
%setup

%build
%define docdir %_docdir/%name
%configure --docdir=%docdir
%make_build

%install
%makeinstall_std
rm %buildroot%docdir/{%name.*,COPYING}

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files
%docdir/
%_bindir/lzop
%_man1dir/lzop.1*

%changelog
* Sat Mar 16 2019 Dmitry V. Levin <ldv@altlinux.org> 1.04-alt1
- 1.03 -> 1.04.

* Mon Jan 16 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.03-alt3
- Fixed build with gcc 6.

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2
- rebuilt as plain src.rpm

* Fri Dec 17 2010 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.02rc1 -> 1.03

* Mon Oct 04 2010 Alexey Tourbin <at@altlinux.ru> 1.02-alt1.1
- rebuilt

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.01 -> 1.02rc1
- built with liblzo2

* Wed Jun 20 2007 Igor Zubkov <icesik@altlinux.org> 1.01-alt2.1
- NMU
- rebuild (closes #9697)

* Mon Oct 20 2003 Andrey Brindeew <abr@altlinux.ru> 1.01-alt2
- Summary placement fix

* Tue May 13 2003 Andrey Brindeew <abr@altlinux.ru> 1.01-alt1
- 1.01

* Fri Jan 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1.00-alt3
- Rebuilt in new environment.

* Tue Aug 20 2002 Andrey Brindeew <abr@altlinux.ru> 1.00-alt2
- Updated BuildRequires

* Tue Aug 20 2002 Andrey Brindeew <abr@altlinux.ru> 1.00-alt1
- First build for ALT Linux

