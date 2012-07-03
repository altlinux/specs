Name: lzop
Version: 1.03
Release: alt2

Summary: LZO fast file compressor
License: GPL
Group: Archiving/Compression

URL: http://www.lzop.org
Source: lzop-%version.tar.gz

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: liblzo2-devel

%description
lzop is a file compressor similar to gzip.  Its main advantages over
gzip are much higher compression and decompression speed (at the cost
of some compression ratio).

%prep
%setup -q -n lzop-%version

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README THANKS
%_bindir/lzop
%_man1dir/lzop.1*

%changelog
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

