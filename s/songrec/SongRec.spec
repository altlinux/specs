%define nameB re.fossplant.songrec

Name: songrec
Version: 0.7.4
Release: alt1

Summary: An open-source Shazam client for Linux.
License: GPL-3.0-only
Group: Sound
Url: https://github.com/marin-m/SongRec
VCS: https://github.com/marin-m/SongRec

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libalsa-devel libssl-devel pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0) libcairo-devel
BuildRequires: pkgconfig(gdk-pixbuf-2.0) pkgconfig(pango)
BuildRequires: pkgconfig(cairo-gobject) pkgconfig(atk) clang-devel
BuildRequires: pkgconfig(gtk4) libpulseaudio-devel
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(graphene-gobject-1.0) pkgconfig(libadwaita-1)

Requires: ffmpeg

%description
SongRec is an open-source Shazam client for Linux, written in Rust.
Features:
- Recognize audio from an arbitrary audio file.
- Recognize audio from the microphone.
- Usage from both GUI and command line (for the file recognition part).
- Provide an history of the recognized songs on the GUI, exportable to CSV.
- Continuous song detection from the microphone, with the ability to choose 
your input device.
- Ability to recognize songs from your speakers rather than your microphone 
(on compatible PulseAudio setups).

%prep
%setup -a1
%rust_prep

%build
%rust_build 

%install
%rust_install 

install -Dm 0644 packaging/rootfs/usr/share/icons/hicolor/scalable/apps/%{nameB}-rainbow.svg %buildroot%_iconsdir/hicolor/128x128/apps/%{nameB}-rainbow.svg
install -Dm 0644 packaging/rootfs/usr/share/icons/hicolor/scalable/apps/%nameB.svg %buildroot%_iconsdir/hicolor/128x128/apps/%nameB.svg
install -Dm 0644 packaging/rootfs/usr/share/applications/%nameB.desktop %buildroot%_datadir/applications/%nameB.desktop
install -Dm 0644 packaging/rootfs/usr/share/metainfo/%nameB.metainfo.xml %buildroot%_datadir/metainfo/%nameB.metainfo.xml

mv -v translations/locale ./
for locale in locale/*; do
 install -Dm 0644 ${locale}/LC_MESSAGES/%name.mo \
 %buildroot%_datadir/${locale}/LC_MESSAGES/%name.mo
done

%find_lang --all-name %name

%files -f %name.lang
%doc *.md LICENSE
%_bindir/%name
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/applications/%nameB.desktop
%_datadir/metainfo/%nameB.metainfo.xml

%changelog
* Sun Jun 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.4-alt1
- 0.7.3 -> 0.7.4

* Mon May 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.3-alt1
- 0.7.2 -> 0.7.3

* Thu May 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.2-alt1
- 0.7.1 -> 0.7.2

* Sun May 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- 0.6.9 -> 0.7.1

* Mon Apr 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.9-alt1
- 0.6.8 -> 0.6.9

* Sun Apr 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.8-alt1
- 0.6.7 -> 0.6.8

* Thu Mar 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.7-alt1
- 0.6.6 -> 0.6.7

* Mon Mar 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.6-alt1
- 0.6.4 -> 0.6.6

* Thu Feb 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.4-alt3
- fixed mostrar system tray icon

* Wed Feb 25 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.4-alt2
- updated to git.5ad31ba75a for new russian translate
- updated icon

* Fri Feb 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.4-alt1
- 0.6.3 -> 0.6.4

* Thu Feb 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.3-alt1
- 0.6.2 -> 0.6.3

* Mon Feb 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.2-alt1
- 0.6.1.1 -> 0.6.2

* Sun Feb 15 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.1.1-alt1
- 0.6.0 -> 0.6.1.1

* Fri Feb 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0

* Fri Jan 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5.0-alt1
- 0.4.3 -> 0.5.0

* Sun Jan 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt2
- added russian locale

* Sun Mar 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- Initial build for ALT Linux.
