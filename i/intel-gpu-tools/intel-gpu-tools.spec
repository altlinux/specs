Name: intel-gpu-tools
Version: 1.17
Release: alt1

Summary: tools for debugging the Intel graphics driver
License: MIT
Group: Development/Debug

# http://cgit.freedesktop.org/xorg/app/intel-gpu-tools/
Url: http://01.org/linuxgraphics/
Source: %name-%version.tar

# Automatically added by buildreq on Tue Dec 06 2016
# optimized out: fontconfig libX11-devel libXext-devel libXrender-devel libwayland-client libwayland-server perl pkg-config python-base python-modules python3 python3-base xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: flex glib2-devel gtk-doc libXrandr-devel libXv-devel libcairo-devel libdrm-devel libkmod-devel libpciaccess-devel libprocps-devel libudev-devel libunwind-devel python3-dev xorg-dri2proto-devel

# dropped by buildreq but still required
BuildRequires: xorg-util-macros
BuildRequires: libdrm-devel >= 2.4.64

# 1.6+
BuildRequires: gtk-doc xorg-dri2proto-devel swig python3-dev flex

# just to be sure...
BuildRequires: bison
BuildRequires: flex
BuildRequires: python3-module-docutils
BuildRequires: python3
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xlib)
BuildRequires: pkgconfig(dri2proto)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libprocps)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libunwind)
BuildRequires: pkgconfig(pciaccess)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xv)

ExclusiveArch: %ix86 x86_64

%description
intel-gpu-tools is a package of tools for debugging the Intel graphics
driver, including a GPU hang dumping program, performance monitor,
and performance microbenchmarks for regression testing the DRM.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_usr/lib/%name/
%_datadir/%name/
#_datadir/gtk-doc/html/%name/
#_mandir/*/*

%changelog
* Tue Dec 06 2016 Michael Shigorin <mike@altlinux.org> 1.17-alt1
- 1.17
- buildreq (and some BRs from rosa package, thanks)

* Sun Jan 03 2016 Michael Shigorin <mike@altlinux.org> 1.13-alt1
- 1.13

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.6-alt1
- 1.6

* Sat Jun 08 2013 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- built for ALT Linux based on opensuse and debian packages

