Name: gtv-dvb
Version: 1.1
Release: alt1%ubt

Summary: DVB player

License: LGPLv2
Group: Video
Url: https://github.com/vl-nix/gtv

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Buildrequires(pre): rpm-build-ubt
BuildRequires: pkgconfig(gtk+-3.0) pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-plugins-base-1.0) pkgconfig(gstreamer-plugins-bad-1.0) 
Requires: v4l-utils

%description
DVB-T/T2, DVB-S/S2, DVB-C, ATSC, DTMB
Graphical user interface - Gtk+3
Audio & Video & Digital TV - Gstreamer 1.0

%prep
%setup

%build
%make_build CFLAG='%optflags' prefix=%prefix

%install
%makeinstall_std prefix=%prefix
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/*
%doc README.md LICENSE

%changelog
* Sat Dec 23 2017 Anton Midyukov <antohami@altlinux.org> 1.1-alt1%ubt
- New version 1.1

* Sun Nov 26 2017 Anton Midyukov <antohami@altlinux.org> 1.0-alt1%ubt
- Initial build for ALT Sisyphus.
