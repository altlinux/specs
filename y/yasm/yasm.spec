Name: yasm
Version: 1.1.0
Release: alt1

Summary: Rewrite of the NASM assembler under the "new" BSD License
License: BSD
Group: Development/Other

URL: http://www.tortall.net/projects/yasm/
Packager: Pavlov Konstantin <thresh@altlinux.ru>
Source: yasm-%version.tar.gz

%description 
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). Yasm
currently supports the x86 and AMD64 instruction sets, accepts NASM and GAS
assembler syntaxes, outputs binary, ELF32, ELF64, 32 and 64-bit Mach-O, RDOFF2,
COFF, Win32, and Win64 object formats, and generates source debugging
information in STABS, DWARF 2, and CodeView 8 formats.

%package -n lib%name-devel
Summary: YASM Development libraries
Group: Development/Other
Provides: lib%name-devel-static = %version-%release
Obsoletes: lib%name-devel-static < %version-%release

%description -n lib%name-devel
Development libraries for YASM.
This package contains static development files for YASM.

%prep
%setup -q

%build
%autoreconf
%configure

%make

%install
%make_install DESTDIR="%buildroot" install
ln -s ytasm %buildroot%_bindir/tasm

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/ytasm
%_bindir/tasm
%_bindir/yasm
%_bindir/vsyasm
%_man1dir/yasm.1*
%_man7dir/yasm*

%files -n lib%name-devel
%_includedir/*.h
%_includedir/libyasm/
%_libdir/*.a

%changelog
* Sat Oct 30 2010 Afanasov Dmitry <ender@altlinux.org> 1.1.0-alt1
- 1.1.0 release.
- add vsyasm: Visual Studio 2010 special frontend.

* Tue May 12 2009 Afanasov Dmitry <ender@altlinux.org> 0.8.0-alt1
- 0.8.0 release.
- install tasm as 'tasm' linked to 'ytasm'

* Sat Jun 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.6.1-alt1
- 0.6.1 release.

* Thu Mar 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.6.0-alt1
- 0.6.0 release, fixes #11114.
- Fixed URL, Summary, License: fixes #11115.

* Fri Dec 23 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.4.0-alt1
- Initial build for ALTLinux.

