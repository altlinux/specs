Name: gdb-multiarch
Version: 18.1
Release: alt1

Summary: A GNU source-level debugger for C, C++ and other languages
License: GPLv3+
Group: Development/Debuggers
URL: https://www.sourceware.org/gdb/
VCS: git://sourceware.org/git/binutils-gdb

%define targets arm-none-eabi aarch64-none-elf riscv32-none-elf
%define replaces() %(for p in %{*}; do printf 'Provides: %%s-gdb = %%s\\nObsoletes: %%s-gdb\\n' $p %version-%release $p;done)
%replaces %targets

Source: %name-%version.tar

BuildRequires: gcc-c++ flex makeinfo python3-devel
BuildRequires: libtinfo-devel libreadline-devel libgmp-devel
BuildRequires: libexpat-devel liblzma-devel libmpfr-devel zlib-devel

%description
GDB is a full featured, command driven debugger.  GDB allows you to
trace the execution of programs and examine their internal state at
any time.  The debugger is most effective when used together with a
supported compiler, such as those from the GNU Compiler Collection.
This package contains GDB built with python support for the following
bare-metal targets: %targets

%prep
%setup
echo '%version-%release (%distribution)' > gdb/version.in

%build
mkdir obj; cd obj
../configure    --enable-targets=arm-none-eabi,aarch64-none-elf,riscv32-none-elf \
                --prefix=%_prefix \
                --with-python=python3 \
                --with-gdb-datadir=%_datadir/gdb-multiarch \
                --with-system-gdbinit-dir=%_sysconfdir/gdbinit.multiarch.d \
                --with-lzma \
                --with-system-readline \
                --with-system-zlib \
                --without-libunwind \
                --enable-plugins \
                --disable-tui \
                --disable-sim \
                --disable-gdbserver \
                --disable-gas \
                --disable-binutils \
                --disable-ld \
                --disable-gold \
                --disable-gprof \
                --disable-gprofng \
                --disable-debuginfod

%make_build

%install
%makeinstall_std -C obj

# This build coexists with the distro gdb/gdb-common/binutils packages:
# rename the essentials, drop the files they already own.
mv %buildroot%_bindir/gdb %buildroot%_bindir/gdb-multiarch
mv %buildroot%_bindir/gdb-add-index %buildroot%_bindir/gdb-multiarch-add-index

# Host-process helpers are out of scope for a cross debugger.
rm %buildroot%_bindir/{gcore,gstack}

# Docs and development files are provided by gdb-common/libgdb-devel.
rm -r %buildroot%_infodir
rm -r %buildroot%_mandir
rm -r %buildroot%_includedir
rm -r %buildroot%_datadir/locale

# unwanted static libraries
rm -rf %buildroot%_libexecdir

# Target vendor init scripts, not useful here.
rm %buildroot%_datadir/gdb-multiarch/system-gdbinit/elinos.py
rm %buildroot%_datadir/gdb-multiarch/system-gdbinit/wrs-linux.py
rmdir %buildroot%_datadir/gdb-multiarch/system-gdbinit

# Used by linux target backends
rm -rf %buildroot%_datadir/gdb-multiarch/syscalls

# System-wide defaults, sourced automatically by this binary only.
mkdir -p %buildroot%_sysconfdir/gdbinit.multiarch.d
cat > %buildroot%_sysconfdir/gdbinit.multiarch.d/00-osabi.gdb <<'EOF'
# Sourced from %_sysconfdir/gdbinit.multiarch.d by gdb-multiarch only.
# Files here must carry a recognized extension (.gdb, .py, .scm) or GDB
# silently skips them; plain GDB commands go in *.gdb files, executed
# in lexicographic order before any ~/.config/gdb/gdbinit.
# This build targets bare metal; pin the OS ABI so syscall names and
# ABI conventions are not Linux ones.  Safe to adjust site-wide here.
set osabi none
EOF

%check
./obj/gdb/gdb --batch \
        -ex 'python import gdb; print("python-ok")' \
        -ex quit

%files
%doc COPYING* gdb/NEWS README.ALT
%config(noreplace) %_sysconfdir/gdbinit.multiarch.d/00-osabi.gdb
%_bindir/gdb-multiarch
%_bindir/gdb-multiarch-add-index
%_datadir/gdb-multiarch

%changelog
* Wed Oct 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 18.1-alt1
- 18.1 released

* Wed May 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 16.3-alt1
- 16.3 released

* Thu Mar 06 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 16.2-alt1
- 16.2 released

* Tue Oct 22 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 15.2-alt1
- 15.2 released

* Fri Mar 22 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 14.2-alt1
- 14.2 released

* Thu Jun 01 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.2-alt1
- 13.2 released

* Thu Mar 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.1-alt1
- 13.1 released

* Fri Feb  3 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.1-alt1
- initial
