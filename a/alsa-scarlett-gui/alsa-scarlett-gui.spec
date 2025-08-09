Name: alsa-scarlett-gui
Version: 0.5.1
Release: alt3

Summary: ALSA Scarlett Gen 1/2/3/4/Vocaster/Clarett Control Panel
License: GPLv3+ LGPLv3+
Group: Sound

Url: https://github.com/geoffreybennett/alsa-scarlett-gui
# Source-url: https://github.com/geoffreybennett/alsa-scarlett-gui/archive/refs/tags/%version.tar.gz#/%name-%version.tar.gz
Source0: %name-%version.tar
Patch0: e2k.patch

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(openssl)

%description
A Gtk4 GUI for the ALSA controls presented by the Linux kernel Focusrite Scarlett2 USB Protocol Mixer Driver.

%prep
%setup

%ifarch %e2k
%autopatch -p1
%endif

%build
%make_build -C src PREFIX=%_prefix

%install
%make_install -C src

install -Dm 755 src/%name %buildroot%_bindir/%name
install -Dm 644 src/vu.b4.alsa-scarlett-gui.desktop %buildroot%_desktopdir/vu.b4.alsa-scarlett-gui.desktop
install -Dm 644 src/img/vu.b4.alsa-scarlett-gui.png %buildroot%_iconsdir/hicolor/256x256/apps/vu.b4.alsa-scarlett-gui.png

%files
%doc ./img ./demo ./docs ./*.md
%_bindir/%name
%_desktopdir/vu.b4.alsa-scarlett-gui.desktop
%_iconsdir/hicolor/256x256/apps/vu.b4.alsa-scarlett-gui.png

%changelog
* Sat Aug 9 2025 Anton Palguno <toxblh@altlinux.org> 0.5.1-alt3
- fix: Build e2k

* Mon Jul 14 2025 Anton Palgunov <toxblh@altlinux.org> 0.5.1-alt2
- fix: Exec path in desktop file

* Sun Jul 13 2025 Anton Palgunov <toxblh@altlinux.org> 0.5.1-alt1
- Initial build in Sisyphus.
