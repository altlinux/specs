Name:    nemu
Version: 3.3.1
Release: alt1

Summary: Ncurses UI for QEMU
License: BSD-2-Clause
Group:   Other
URL:     https://github.com/nemuTUI/nemu
VCS:     https://github.com/nemuTUI/nemu

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libarchive-devel
BuildRequires: libdbus-devel
BuildRequires: libgraphviz-devel
BuildRequires: libjson-c-devel
BuildRequires: libncursesw-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: libxml2-devel

%description
nEMU is text-based user interface application for hypervisor QEMU, based
on ncurses5 library.

%prep
%setup

%build
%cmake \
	-DNM_WITH_NETWORK_MAP=ON \
	-DNM_WITH_DBUS=ON \
	-DNM_WITH_REMOTE=ON \
	-DNM_WITH_USB=ON
%cmake_build

%install
%cmake_install

%files
%doc *.md CHANGES LICENSE
%_bindir/nemu
%_bindir/ntty
%_man1dir/nemu.1.xz
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/*.mo
%_datadir/bash-completion/completions/nemu
%_datadir/zsh/site-functions/_nemu
%_datadir/nemu/scripts/*
%_datadir/nemu/templates/*

%changelog
* Tue Nov 05 2024 Ilya Sorochan <k0tran@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus (Closes #51597).
