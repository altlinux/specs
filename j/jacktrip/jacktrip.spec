Name:    jacktrip
Version: 3.0.0
Release: alt1

Summary: JackTrip: multi-machine audio network performance over the Internet
License: MIT and GPL-3.0-or-later and LGPL-3.0-only
Group:   Sound
Url:     https://jacktrip.github.io/jacktrip
VCS:     https://github.com/jacktrip/jacktrip

Packager: Sergey Gvozdetskiy <serjigva@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: gcc-c++ help2man
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6ShaderTools)
BuildRequires: pkgconfig(Qt6Svg)
%ifarch %qt6_qtwebengine_arches
BuildRequires: pkgconfig(Qt6WebEngineCore)
%endif
BuildRequires: pkgconfig(Qt6WebSockets)
BuildRequires: pkgconfig(samplerate)
BuildRequires: python3(yaml)
BuildRequires: python3(jinja2)
BuildRequires: qt6-tools

%description
It supports any number of channels (as many as the computer/network can handle)
of bidirectional, high quality, uncompressed audio signal streaming.

%prep
%setup
subst 's/qmake6/qmake-qt6/g' ./meson.build

%build
%meson \
    -Drtaudio=enabled \
    -Dnovs=true \
    -Dwair=true \
    -Dlibsamplerate=auto

%meson_build

%install
%meson_install

%files
%doc *.md LICENSES/* docs/*
%_bindir/%name
%_datadir/metainfo/*.xml
%_desktopdir/org.%name.JackTrip.desktop
%_iconsdir/hicolor/symbolic/apps/*.svg
%_iconsdir/hicolor/scalable/apps/*.svg
%_liconsdir/*.png
%_man1dir/%name.1.*

%changelog
* Mon Apr 27 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.0.0-alt1
- 2.7.2 -> 3.0.0

* Tue Feb 10 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.7.2-alt1
- 2.7.1 -> 2.7.2

* Thu Oct 16 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.7.1-alt1
- 2.6.0 -> 2.7.1

* Wed Jun 25 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.6.0-alt1
- 2.4.1 -> 2.6.0
- added libsamplerate support

* Tue Dec 17 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.4.1-alt1
- 2.3.1 -> 2.4.1

* Wed Aug 21 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
