Name: eresi
Version: 0.83
Release: alt3

Summary: The ERESI Reverse Engineering Software Interface

License: GPL
Url: http://www.eresi-project.org
Group: File tools

ExclusiveArch: x86_64 i586

# Source-git: https://github.com/thorkill/eresi.git
Source: %name-%version.tar

Patch: 0001-fix-underlinking-when-linking-with-Wl-as-needed.patch
Patch1: eresi-fix-glibc-2.28.patch

BuildRequires: libssl-devel

# circle dependency libstderesi <->librevm
%set_verify_elf_method relaxed

%description
The ERESI Reverse Engineering Software Interface
* Analysis on nearly all types of sections
* Cool disasm/resolving engine with libelfsh and libasm
* Raw read/write capability into ELF32 AND ELF64 objects
* Modify ELF header, PHT, SHT, GOT, CTORS, DTORS, .dynamic, PAX bits
* Modify symbol table, dynamic symbol table and relocation tables
* Remove or reconstruct SHT
* Real interactive and scripting modes
* Many kind of section injection [even working in non-exec environments]
* Control flow graphs with graphviz output (i386): see modflow
* ELFsh Module support and ELFsh internal API
* Quiet output for tiny screens and shellcript friendship
* Experimental ET_EXEC relocation and remapping feature (INTEL)
* Full ET_REL injection into ET_EXEC (INTEL / SPARC / ALPHA)
* PLT infection (INTEL, SPARC, ALPHA, MIPS)
* ALTPLT technique (INTEL, SPARC, ALPHA)

%prep
%setup
%patch -p1
%patch1 -p1

%__subst "s|termcap|tinfo|g" ./configure

%build
#./configure --enable-32-64 \
./configure \
%ifarch x86_64
	--enable-64 \
	--enable-m64 \
%else
	--enable-32 \
%endif
	%nil
#	--libasm-ia32
#	--enable-readline
#	--enable-ncurses

%make_build

%install
make DESTDIR=%buildroot/%prefix LIBPATH=%buildroot%_libdir/ install || :

find %buildroot -type l -delete
find %buildroot -name '*.a' -delete

#%ifarch x86_64
#ln -s elfsh64 %buildroot%_bindir/elfsh
#%else
#ln -s elfsh32 %buildroot%_bindir/elfsh
#%endif


#rm -f %buildroot%_libdir/libe2dbg*.so
rm -fv %buildroot%_libdir/libgdbwrap*.so
rm -rfv %buildroot%_includedir/
rm -fv %buildroot%_bindir/eresi-config*
rm -fv %buildroot%_bindir/kedbg*

#check
#cd testsuite
#make

%files
%_bindir/etrace*
%_bindir/e2dbg*
%_bindir/elfsh*
#_bindir/kedbg*
%_bindir/evarista*
%_libdir/lib*.so
%_man1dir/eresi.*

%changelog
* Thu Dec 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.83-alt3
- fix build

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.83-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Jul 06 2018 Vitaly Lipatov <lav@altlinux.ru> 0.83-alt2
- fix underlinking

* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 0.83-alt1
- initial release for ALT Sisyphus
