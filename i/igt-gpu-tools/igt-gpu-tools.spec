%define _unpackaged_files_terminate_build 1

Name: igt-gpu-tools
Version: 1.28
Release: alt1

Summary: IGT gpu tools and tests
License: MIT
Group: Development/Debug

Url: https://gitlab.freedesktop.org/drm/igt-gpu-tools
Source: %name-%version.tar

Provides: intel-gpu-tools = %EVR
Obsoletes: intel-gpu-tools < %EVR

ExclusiveArch: %ix86 x86_64

Requires: intel-gen4asm = %EVR

BuildRequires: rpm-build-perl
BuildRequires: perl-Pod-Usage
BuildRequires: python3-dev
BuildRequires: meson flex
BuildRequires: libdrm-devel
BuildRequires: libpciaccess-devel
BuildRequires: libkmod-devel
BuildRequires: libproc2-devel
BuildRequires: libunwind-devel
BuildRequires: libdw-devel
BuildRequires: libpixman-devel
BuildRequires: libcairo-devel
BuildRequires: libudev-devel
BuildRequires: libxmlrpc-devel
BuildRequires: libgsl-devel
BuildRequires: libalsa-devel
BuildRequires: libcurl-devel
BuildRequires: libXv-devel
BuildRequires: libXrandr-devel
BuildRequires: liboping-devel
BuildRequires: libdb4-devel
BuildRequires: libgdbm-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libjson-c-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: python3-module-docutils

%description
IGT GPU Tools is a collection  of tools for development and testing of
the DRM drivers. There are many  macro-level test suites that get used
against  the  drivers,  including   xtest,  rendercheck,  piglit,  and
oglconform, but failures from those can  be difficult to track down to
kernel  changes,  and many  require  complicated  build procedures  or
specific testing  environments to  get useful results.  Therefore, IGT
GPU  Tools  includes  low-level   tools  and  tests  specifically  for
development and testing of the DRM Drivers.

%package -n intel-gen4asm
Summary: Intel 965 assembly language compiler
License: MIT
Group: Development/Tools

%description -n intel-gen4asm
intel-gen4asm is  a program  to compile an  assembly language  for the
Intel 965 Express Chipset.  It has been used to construct programs for
textured video in the 2d driver.

%package devel
Summary: GTK development suite for igt-gpu-tools
License: MIT
Group: Development/C

%description devel
%summary

%package devel-doc
Summary: GTK development documentation for igt-gpu-tools
License: MIT
BuildArch: noarch
Group: Development/Documentation

%description devel-doc
%summary

%prep
%setup

# fix: warning: "_FORTIFY_SOURCE" redefined
sed -i -e 's/_FORTIFY_SOURCE=2/_FORTIFY_SOURCE=3/' meson.build

%build
%meson
%meson_build
%meson_build igt-gpu-tools-doc

%install
%meson_install

%files
%doc README.md COPYING NEWS
%_bindir/*
%_libdir/*.so.*
%_man1dir/*
%_libexecdir/igt-gpu-tools
%_datadir/igt-gpu-tools
%exclude %_bindir/intel-gen4asm
%exclude %_bindir/intel-gen4disasm

%files devel
%_libdir/*.so
%_includedir/i915-perf
%_pkgconfigdir/i915-perf.pc

%files devel-doc
%_datadir/gtk-doc/html/igt-gpu-tools

%files -n intel-gen4asm
%doc assembler/README assembler/TODO assembler/doc/examples/
%_bindir/intel-gen4asm
%_bindir/intel-gen4disasm
%_pkgconfigdir/intel-gen4asm.pc

%changelog
* Fri Oct 13 2023 Egor Ignatov <egori@altlinux.org> 1.28-alt1
- new version 1.28
- change packaging scheme

* Fri Mar 03 2023 Egor Ignatov <egori@altlinux.org> 1.27.1-alt1
- new version 1.27.1
- clean up spec

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

