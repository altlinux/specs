Name: intel-gpu-tools
Version: 1.3
Release: alt1

Summary: tools for debugging the Intel graphics driver
License: MIT
Group: Development/Debug

# http://cgit.freedesktop.org/xorg/app/intel-gpu-tools/
Url: http://01.org/linuxgraphics/
Source: %name-%version.tar

# Automatically added by buildreq on Sat Jun 08 2013
# optimized out: fontconfig libdrm-devel libwayland-client libwayland-server pkg-config python-base
BuildRequires: glib2-devel libcairo-devel libpciaccess-devel

# dropped by buildreq but still required
BuildRequires: xorg-util-macros

ExclusiveArch:  %ix86 x86_64

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
%doc %_mandir/*/*

%changelog
* Sat Jun 08 2013 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- built for ALT Linux based on opensuse and debian packages

