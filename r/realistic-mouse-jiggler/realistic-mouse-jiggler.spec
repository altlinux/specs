Name:    realistic-mouse-jiggler
Version: 0.1.7
Release: alt1

Summary: The realistic desktop mouse jiggler
License: MIT
Group:   System/Configuration/Hardware
URL:     https://www.visorcraft.com
VCS:     https://github.com/visorcraft/realistic-mouse-jiggler

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libxkbcommon-devel
Requires: ydotool

%description
Realistic Mouse Jiggler keeps desktop sessions awake by moving the cursor
with natural-looking motion. It is built for people who want a small,
predictable utility instead of a bulky background app.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

install -Dpm 0644 packaging/linux/com.visorcraft.realistic-mouse-jiggler.desktop \
    %buildroot%_desktopdir/com.visorcraft.realistic-mouse-jiggler.desktop

for size in 16 24 32 48 64 128 256 512; do
    install -Dpm 0644 assets/icons/rmj-${size}.png \
        %buildroot%_iconsdir/hicolor/${size}x${size}/apps/com.visorcraft.realistic-mouse-jiggler.png
done

%files
%doc LICENSE README.md
%_bindir/realistic-mouse-jiggler
%_desktopdir/com.visorcraft.realistic-mouse-jiggler.desktop
%_iconsdir/hicolor/*/apps/com.visorcraft.realistic-mouse-jiggler.png

%changelog
* Thu Jul 02 2026 Sergey Palcheh <minergenon@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus
