Name: bandwidth
Version: 1.11.2
Release: alt1

Summary: Artificial benchmark for measuring memory bandwidth
Group: System/Kernel and hardware
License: GPL-2.0
Url: https://zsmith.co/%name.html

Packager: Michael Shigorin <mike@altlinux.org>

Source: https://zsmith.co/archives/%name-%version.tar.gz
Patch: %name-1.11.2-alt-ix86.patch

BuildRequires(pre): rpm-macros-generic-compat
BuildRequires: nasm

ExclusiveArch: %ix86 x86_64 %arm aarch64

%ifarch %ix86
Provides: bandwidth32 = %version
Obsoletes: bandwidth32 <= 0.15
%endif

%define namearch %name%__isa_bits

%description
bandwidth, is an artificial benchmark primarily for measuring memory
bandwidth on x86 and x86_64 based computers, useful for identifying
weaknesses in a computer's memory subsystem, in the bus architecture,
in the cache architecture and in the processor itself.

bandwidth also tests some libc functions and, under GNU/Linux, it
attempts to test framebuffer memory access speed if the framebuffer
device is available.

bandwidth supports:

32- and 64-bit x86 GNU/Linux
Raspberry pi 4 ARM running 64-bit Raspberry Pi OS
Raspberry pi 3/4 ARM running 32-bit Raspberry Pi OS
64-bit x86 Windows
64-bit x86 Mac OS
64-bit M1 Mac OS
Thus it supports four processor architectures:

i386
x86_64
ARM 64-bit (aarch64)
ARM 32-bit (aarch32)


bandwidth is a benchmark to estimate the memory bandwidth of
a system, including main memory, L2 cache, framebuffer memory,
and string library performance.

%prep
%setup
%patch
find ./ -type f -print0 | xargs -r0 chmod -x --
sed -i 's/\(^CFLAGS.*$\)/\1 %(getconf LFS_CFLAGS)/' OOC/Makefile

%build
%ifarch %ix86
    %make_build -f Makefile-linux-i386 %namearch
%endif
%ifarch x86_64
    %make_build -f Makefile-linux-%_arch %namearch
%endif
%ifarch %arm aarch64
    %make_build -f Makefile-arm%__isa_bits %namearch
%endif

%install
# ...so that %_bindir/%name is real file in both packages
install -pDm755 %namearch %buildroot%_bindir/%namearch
ln -s %namearch %buildroot%_bindir/%name

%files
%doc README.txt
%_bindir/%namearch
%_bindir/%name

%changelog
* Fri Apr 15 2022 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- 1.11.2 (new %%url)
- added aarch64 to ExclusiveArch
- fixed License tag

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 0.26c-alt1
- 0.26c:
  + fixes an issue with AMD processors

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 0.25a-alt1
- 0.25a (thanks force@)
  + upstream merged arches, added arm support

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.16-alt1
- 0.16
- NB: 0.15 brought assembly core and diverged between arches
  (this package is 64-bit only)

* Thu Aug 16 2007 Michael Shigorin <mike@altlinux.org> 0.13-alt1
- built for ALT Linux
- spec based on Dag Wieers' 0.12-1

* Sat Jul 28 2007 Dag Wieers <dag@wieers.com> - 0.12-1 - +/
- Initial package. (using DAR)
