
Name: xorg-drv-vmmouse
Version: 13.1.0
Release: alt1

Summary: VMWare mouse input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Requires: XORG_ABI_XINPUT = %get_xorg_abi_xinput

Source: %name-%version.tar

BuildRequires(Pre): xorg-sdk xorg-util-macros

# Automatically added by buildreq on Fri Jul 22 2016 (-bi)
# optimized out: elfutils libpciaccess-devel libpixman-devel perl pkg-config python-base python-modules python3 python3-base rpm-build-python3 ruby ruby-stdlibs xorg-dri3proto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-presentproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xineramaproto-devel xorg-xproto-devel xz
#BuildRequires: glibc-devel-static libudev-devel python-module-google python3-dev rpm-build-ruby xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-sdk
BuildRequires: glibc-devel libudev-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel

%description
Xorg input driver for VMWare mouse.

%prep
%setup -q
%autoreconf

%build
%configure \
    --with-xorg-module-dir=%_x11modulesdir \
    --disable-static \
    --disable-silent-rules \
    --with-xorg-conf-dir='%_xorgsysconfigdir' \
    --with-udev-rules-dir='%_udevrulesdir' \
    #

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_udevrulesdir/*vmmouse*.rules
%_xorgsysconfigdir/*vmmouse*.conf
%_bindir/*vmmouse*
%_x11modulesdir/input/*vmmouse*.so
%_man1dir/*vmmouse*.*
%_man4dir/*vmmouse*.*

%changelog
* Fri Jul 22 2016 Sergey V Turchin <zerg@altlinux.org> 13.1.0-alt1
- initial build
