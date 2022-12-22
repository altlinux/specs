Name: igt-gpu-tools
Version: 1.26
Release: alt2

Summary: tools for debugging the Intel graphics driver
License: MIT
Group: Development/Debug

# http://cgit.freedesktop.org/xorg/app/intel-gpu-tools/
Url: http://01.org/linuxgraphics/
Source: %name-%version.tar.xz

Provides: intel-gpu-tools-@version@
Obsoletes: intel-gpu-tools

ExclusiveArch: %ix86 x86_64

Requires: intel-gen4asm = %version

# Automatically added by buildreq on Wed Nov 17 2021
# optimized out: docbook-dtds docbook-style-xsl fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXau-devel libXext-devel libXrender-devel libcrypt-devel libctf-nobfd0 libelf-devel libfreetype-devel libglvnd-devel libgpg-error libgraphite2-devel libicu-devel libjson-c5 libncurses-devel libp11-kit libpng-devel libsasl2-3 libtinfo-devel libxcb-devel libxmlrpc-client ninja-build perl pkg-config python3 python3-base python3-module-Pygments sh4 xml-common xsltproc xz zlib-devel
BuildRequires: ctags flex git-core gtk-doc libXrandr-devel libXv-devel libalsa-devel libcairo-devel libcurl-devel libdb4-devel libdrm-devel libdw-devel libgdbm-devel libgsl-devel libharfbuzz-devel libjson-c-devel libkmod-devel liboping-devel libpciaccess-devel libpixman-devel libprocps-devel libudev-devel libunwind-devel libxmlrpc-devel meson python3-dev

%description
igt-gpu-tools is a package of tools for debugging the Intel graphics
driver, including a GPU hang dumping program, performance monitor,
and performance microbenchmarks for regression testing the DRM.

%package -n intel-gen4asm
Summary: Intel 965 assembly language compiler
License: MIT
Group: Development/Tools

%description -n intel-gen4asm
intel-gen4asm is a program to compile an assembly language for the Intel 965
Express Chipset.  It has been used to construct programs for textured video
in the 2d driver.

%package devel
Summary: GTK development suite for %name
License: MIT
Group: Development/C

%description devel
%summary

%package devel-doc
Summary: GTK development documentation for %name
License: MIT
BuildArch: noarch
Group: Development/Documentation

%description devel-doc
%summary

%prep
%setup

# fix FTBFS with meson>=0.60
sed -i -e '/underscorify(f)/ s/(f)/()/' lib/meson.build

%build
%meson
%meson_build
%meson_build igt-gpu-tools-doc

%install
%meson_install

%files
%_bindir/*
%_libdir/*.so.*
%_usr/lib/%name/
%_datadir/%name/
#_mandir/*/*
%exclude %_bindir/intel-gen4asm
%exclude %_bindir/intel-gen4disasm
%exclude %_pkgconfigdir/intel-gen4asm.pc

%files devel
%_libdir/*.so
%_includedir/i915-perf
%_pkgconfigdir/i915-perf.pc

%files devel-doc
%_datadir/gtk-doc/html/%name

%files -n intel-gen4asm
%_bindir/intel-gen4asm
%_bindir/intel-gen4disasm
%_pkgconfigdir/intel-gen4asm.pc
%doc assembler/README assembler/TODO assembler/doc/examples/

%changelog
* Thu Dec 22 2022 Egor Ignatov <egori@altlinux.org> 1.26-alt2
- Fix FTBFS with meson>=0.60

* Wed Nov 17 2021 Fr. Br. George <george@altlinux.ru> 1.26-alt1
- Autobuild version bump to 1.26

* Sat Jan 30 2021 Fr. Br. George <george@altlinux.ru> 1.25-alt1
- Autobuild version bump to 1.25

* Wed Dec 11 2019 Fr. Br. George <george@altlinux.ru> 1.24-alt1
- Autobuild version bump to 1.24
- Rename to igt-gpu-tools
- Switch to meson build

* Thu Sep 20 2018 Fr. Br. George <george@altlinux.ru> 1.22-alt1
- Autobuild version bump to 1.22

* Thu Sep 20 2018 Fr. Br. George <george@altlinux.ru> 1.20-alt1
- Autobuild version bump to 1.20

* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19-alt1
- Updated to upstream version 1.19

* Thu Dec 08 2016 Michael Shigorin <mike@altlinux.org> 1.17-alt2
- moved intel-gen4asm into a subpackage of its own
  (replacing the pre-existing standalone one);
  thanks week@ for pointing the file confict out

* Tue Dec 06 2016 Michael Shigorin <mike@altlinux.org> 1.17-alt1
- 1.17
- buildreq (and some BRs from rosa package, thanks)

* Sun Jan 03 2016 Michael Shigorin <mike@altlinux.org> 1.13-alt1
- 1.13

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.6-alt1
- 1.6

* Sat Jun 08 2013 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- built for ALT Linux based on opensuse and debian packages

