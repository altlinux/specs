%define marss_scripts %_datadir/marss-riscv-scripts

Name: marss-riscv
Version: 1.0a
Release: alt1

Summary: Open source simulator for the RISC-V ISA built upon TinyEMU.

License: MIT
Group: Development/Tools
Url: https://github.com/bucaps/marss-riscv

Packager: Nikita Ermakov <arei@altlinux.org>

Source: %name-%version.tar

BuildRequires: libssl-devel libSDL-devel libcurl-devel

%description
MARSS-RISCV (Micro-ARchitectural System Simulator - RISCV) is a open
source, cycle-accurate single core full-system (Linux)
micro-architectural simulator for the RISC-V ISA built upon TinyEMU
emulator by Fabrice Bellard and uses its code for all the device
emulation and configuration.

%prep
%setup

%build
pushd src >/dev/null
# Build general tools
make splitimg build_filelist stats-display
# Build simulator with XLEN=32,64 FLEN=0,32,64
for xlen in 32 64; do
    for flen in 0 32 64; do
        make -B CONFIG_XLEN="$xlen" CONFIG_FLEN="$flen" marss-riscv
        mv marss-riscv{,-x"$xlen"-f"$flen"}
    done
done
popd >/dev/null

%install
pushd src >/dev/null
for i in splitimg build_filelist stats-display; do
    %__install -Dm755 -t %buildroot/%_bindir "$i"
done
for xlen in 32 64; do
    for flen in 0 32 64; do
        %__install -Dm755 -t %buildroot/%_bindir marss-riscv-x"$xlen"-f"$flen" 
    done
done
%__install -Dm755 -t %buildroot/%_sbindir netinit.sh 
popd >/dev/null

%__install -Dm755 -t %buildroot/%marss_scripts scripts/*

%files
%_bindir/*
%_sbindir/*
%dir %marss_scripts
%marss_scripts/*
%doc README.md

%changelog
* Thu Aug 29 2019 Nikita Ermakov <arei@altlinux.org> 1.0a-alt1
- Initial build for ALT Linux Sisyphus.
