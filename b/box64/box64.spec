Name: box64
Version: 0.2.0
Release: alt1

Summary: Linux Userspace x86_64 Emulator with a twist

License: MIT
Group: Emulators
Url: https://github.com/ptitSeb/box64.git

Packager: Dmitry Terekhin <jqt4@altlinux.org>

ExclusiveArch: riscv64 aarch64

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: python3

%description
Box64 lets you run x86_64 Linux programs (such as games)
on non-x86_64 Linux systems.

%ifarch riscv64
%define targets RV64
%endif
%ifarch aarch64
%define targets ARM_DYNAREC
%endif

%prep
%setup

%build
for board in %targets; do
    mkdir build
    cd build
    cmake .. -D${board}=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/usr
    %make_build
    cd ..
    mkdir "${board}/"
    cd build
    make DESTDIR="../${board}/" install
    cd ..
    rm -rf build
done

%install
for board in %targets; do
    mkdir -p %buildroot/
    cp -r ${board}/* %buildroot/
    %add_verify_elf_skiplist /usr/lib/x86_64-linux-gnu/*
    %add_findreq_skiplist /usr/lib/x86_64-linux-gnu/*
    %add_findprov_skiplist /usr/lib/x86_64-linux-gnu/*
    %add_debuginfo_skiplist /usr/lib/x86_64-linux-gnu/*
done

%files
%doc docs/*
/etc/binfmt.d/box64.conf
/etc/box64.box64rc
/usr/bin/box64
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/*


%changelog
* Tue Feb 07 2023 Dmitry Terekhin <jqt4@altlinux.org> 0.2.0-alt1
- Initial build
