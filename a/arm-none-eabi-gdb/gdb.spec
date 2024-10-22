Name: arm-none-eabi-gdb
Version: 15.2
Release: alt1

Summary: A GNU source-level debugger for C, C++ and other languages
License: GPLv3+
Group: Development/Debuggers
Url: https://www.sourceware.org/gdb/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ flex makeinfo
BuildRequires: libtinfo-devel libreadline-devel libgmp-devel libexpat-devel liblzma-devel libmpfr-devel zlib-devel

%description
GDB is a full featured, command driven debugger.  GDB allows you to
trace the execution of programs and examine their internal state at
any time.  The debugger is most effective when used together with a
supported compiler, such as those from the GNU Compiler Collection.
This package contains GDB built for arm-none-eabi target.

%define target arm-none-eabi
%define _libexecdir /usr/libexec

%prep
%setup
echo '%version-%release (%distribution)' > gdb/version.in

%build
mkdir obj-%target; cd obj-%target
../configure    --target=%target \
                --prefix=%_prefix \
                --with-gdb-datadir=%_libexecdir/%target/share/gdb \
                --with-gnu-ld \
                --with-lzma \
                --with-system-readline \
                --with-system-zlib \
                --without-libunwind \
                --enable-plugins \
                --disable-tui \
                --disable-sim \
                --disable-gas \
                --disable-binutils \
                --disable-ld \
                --disable-gold \
                --disable-gprof \
                --disable-debuginfod \
                --without-auto-load-safe-path

%make_build

%install
%makeinstall_std -C obj-%target
mkdir -p %buildroot%_libexecdir/%target/share/gdb/auto-load

%files
%doc COPYING* gdb/NEWS
%_bindir/%target-gdb
%_libexecdir/%target/share/gdb/auto-load

%changelog
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
