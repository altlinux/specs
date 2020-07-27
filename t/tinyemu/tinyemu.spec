Name: tinyemu
Version: 20191221
Release: alt1
License: MIT
Url: http://bellard.org/tinyemu/
Group: Emulators
Summary: A system emulator for the RISC-V and x86 architectures
Source: %name-%version.tar.gz
Provides: riscvemu = %EVR
Obsoletes: riscvemu <= 20170806

# Automatically added by buildreq on Mon Oct 16 2017
# optimized out: glibc-kernheaders-x86 libgpg-error python-base
BuildRequires: glibc-kernheaders-generic libSDL-devel libcurl-devel libssl-devel

%description
TinyEMU is a system emulator for the RISC-V and x86 architectures.
Its purpose is to be small and simple while being complete.

Main features:

    RISC-V system emulator supporting the RV128IMAFDQC base ISA
    (user level ISA version 2.2, priviledged architecture version 1.10)
    including:
        32/64/128 bit integer registers
        32/64/128 bit floating point instructions (using the SoftFP Library)
        Compressed instructions
        Dynamic XLEN change
    x86 system emulator based on KVM
    VirtIO console, network, block device, input and 9P filesystem
    Graphical display with SDL
    JSON configuration file
    Remote HTTP block device and filesystem
    Small code, easy to modify, few external dependancies
    Javascript version running Linux and Windows 2000.

%prep
%setup
sed -i 's/-Werror //' Makefile
%ifnarch x86_64
sed -i '/^CONFIG_INT128=y/s/^/#/' Makefile
%endif

%build
%make_build STRIP=true

%install
install -d %buildroot%_bindir
%makeinstall STRIP=true

%files
%doc readme.* netinit.sh Changelog
%_bindir/*

%changelog
* Mon Jul 27 2020 Fr. Br. George <george@altlinux.ru> 20191221-alt1
- Autobuild version bump to 20191221

* Thu Feb 28 2019 Fr. Br. George <george@altlinux.ru> 20190210-alt1
- Autobuild version bump to 20190210

* Thu Dec 06 2018 Fr. Br. George <george@altlinux.ru> 20180923-alt1
- Autobuild version bump to 20180923
- Project is renamed from riscvemu to tinyemu

* Thu Sep 28 2017 Fr. Br. George <george@altlinux.ru> 20170806-alt1
- Autobuild version bump to 20170806

* Fri Jan 20 2017 Fr. Br. George <george@altlinux.ru> 20170112-alt1
- Initial build for ALT

