Name: riscvemu
Version: 20170806
Release: alt1
License: MIT
Url: http://bellard.org/riscvemu/
Group: Emulators
Summary: A system emulator for the RISC-V architecture
Source: %name-%version.tar.gz

# Automatically added by buildreq on Mon Oct 16 2017
# optimized out: glibc-kernheaders-x86 libgpg-error python-base
BuildRequires: glibc-kernheaders-generic libSDL-devel libcurl-devel libssl-devel

%description
RISCVEMU is a system emulator for the RISC-V architecture. Its purpose
is to be small and simple while being complete. Among its features the
support of 128 bit addressing and 128 bit floating point makes it ready
for the future !

Main features:

RISC-V system emulator supporting the RV128IMAFDQC base ISA (user level
ISA version 2.1, priviledged architecture version 1.9.1) including:
32/64/128 bit integer registers
32/64/128 bit floating point instructions (using the SoftFP Library)
Compressed instructions
Private extension to change the integer register width (XLEN) dynamically
VirtIO console, network, block device and 9P filesystem
HTIF console
Small code, easy to modify, no external dependancies
Javascript demo running 64 bit Linux.

%prep
%setup
sed -i 's/-Werror //' Makefile
%ifarch %ix86
sed -i '/^PROGS+=riscvemu128/s/^/#/' Makefile
%endif

%build
%make_build

%install
install -d %buildroot%_bindir %buildroot%_datadir
install riscvemu riscvemu[0-9]*[0-9] %buildroot%_bindir/

%files
%doc readme.* netinit.sh
%_bindir/*

%changelog
* Thu Sep 28 2017 Fr. Br. George <george@altlinux.ru> 20170806-alt1
- Autobuild version bump to 20170806

* Fri Jan 20 2017 Fr. Br. George <george@altlinux.ru> 20170112-alt1
- Initial build for ALT

