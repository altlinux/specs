Name: marss-riscv
Version: 4.1a
Release: alt1

Summary: Open source simulator for the RISC-V ISA built upon TinyEMU

License: MIT
Group: Development/Tools
Url: https://github.com/bucaps/marss-riscv

Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Jan 19 2022
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libsasl2-3 libstdc++-devel python3-base sh4
BuildRequires: gcc-c++ libSDL-devel libcurl-devel libssl-devel python3

BuildRequires: chrpath

%description
MARSS-RISCV (Micro-ARchitectural System Simulator - RISCV) is a open
source, cycle-accurate single core full-system (Linux)
micro-architectural simulator for the RISC-V ISA built upon TinyEMU
emulator by Fabrice Bellard and uses its code for all the device
emulation and configuration.

%prep
%setup
sed -i 's/-fPIC /-fPIC -g /g' src/DRAMsim3/Makefile
for C in configs/*.cfg; do
 sed -Ei 's@[[:alnum:]]+/configs/@%_datadir/%name/@g' $C
done

cat > demo.sh <<@@@
#!/bin/sh

DIR=\${1:?Usage: \$0 install-path}
mkdir -p "\$DIR"
cd "\$DIR"
wget -c https://cs.binghamton.edu/~marss-riscv/marss-riscv-images.tar.gz
tar -xvz --keep-newer-file -f marss-riscv-images.tar.gz
cd marss-riscv-images/riscv64-unknown-linux-gnu/
test -r riscv64.img || xz -d -k -T 0 riscv64.img.xz
cp %_datadir/%name/riscv64_inorder_soc.cfg ..
cd ..
marss-riscv-x64-f64 riscv64_inorder_soc.cfg
@@@

%build
%make_build -C src splitimg build_filelist all
# Build simulator with XLEN=32,64 FLEN=0,32,64
for xlen in 32 64; do
    for flen in 0 32 64; do
        %make_build -C src -B CONFIG_XLEN="$xlen" CONFIG_FLEN="$flen" marss-riscv
        mv src/marss-riscv{,-x"$xlen"-f"$flen"}
    done
done

%install
for i in splitimg build_filelist sim-stats-display; do
    install -Dm755 src/"$i" %buildroot%_bindir/$i-%name
done
for xlen in 32 64; do
    for flen in 0 32 64; do
        install -Dm755 -t %buildroot/%_bindir src/marss-riscv-x"$xlen"-f"$flen"
    done
done

install -Dm755 src/netinit.sh %buildroot/%_sbindir/netinit-%name.sh
install -Dm755 demo.sh %buildroot/%_sbindir/demo-%name.sh
install -Dm755 -t %buildroot/%_libdir src/lib*.so
install -Dm755 -t %buildroot/%_libdir src/*/lib*.so

mkdir -p %buildroot%_datadir/%name
install $(find * -name \*.ini -o -name \*.cfg) %buildroot%_datadir/%name/

chrpath -d %buildroot/%_libdir/lib*.so
chrpath -d %buildroot/%_bindir/*

%files
%_bindir/*
%_sbindir/*
%_libdir/lib*
%_datadir/%name
%doc *.md

%changelog
* Wed Jan 19 2022 Fr. Br. George <george@altlinux.ru> 4.1a-alt1
- Autobuild version bump to 4.1a

* Thu Aug 29 2019 Nikita Ermakov <arei@altlinux.org> 1.0a-alt1
- Initial build for ALT Linux Sisyphus.
