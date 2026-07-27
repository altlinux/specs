Name:    espanso
Version: 2.4.0
Release: alt1

Summary: A Privacy-first, Cross-platform Text Expander
License: GPL-3.0-only
Group:   Text tools
URL:     https://espanso.org
VCS:     https://github.com/espanso/espanso

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: libssl-devel libX11-devel libXtst-devel libxkbcommon-devel
BuildRequires: libwxGTK3.2-devel libwayland-client-devel wayland-protocols
BuildRequires: rpm-macros-systemd
Requires: %name-common = %EVR
Requires: espanso-backend = %EVR

ExcludeArch: %ix86

%description
A Privacy-first, Cross-platform Text Expander

What is a Text Expander?
text expander is a program that detects when you type a specific keyword and
replaces it with something else. This is useful in many ways:

Save a lot of typing, expanding common sentences
Create system-wide code snippets
Execute custom scripts
Use emojis
System-wide 'autocorrect' specific to you

%package common
Summary: Common files for Espanso
Group: Text tools
%add_findreq_skiplist %_bindir/espanso

%description common
Common files (desktop entry and icon) for Espanso.

%package x11
Summary: Espanso X11 backend
Group: Text tools
Provides: espanso-backend = %EVR
Requires: %name-common = %EVR

%description x11
X11 backend for Espanso text expander.

%package wayland
Summary: Espanso Wayland backend
Group: Text tools
Provides: espanso-backend = %EVR
Requires: %name-common = %EVR
Requires: wl-clipboard

%description wayland
Wayland backend for Espanso text expander.

%prep
%setup
%setup -a1
%rust_prep

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
        ./vendor/*/.cargo-checksum.json

%build
# X11 build (default features: modulo, native-tls)
%rust_build
cp target/release/espanso target/release/espanso-x11

# Wayland build
%rust_build --no-default-features --features modulo,native-tls,wayland
cp target/release/espanso target/release/espanso-wayland

%install
install -Dm 755 target/release/espanso-x11 %buildroot%_bindir/espanso-x11
install -Dm 755 target/release/espanso-wayland %buildroot%_bindir/espanso-wayland

install -Dm 644 espanso/src/res/linux/espanso.desktop %buildroot%_desktopdir/espanso.desktop
install -Dm 644 espanso/src/res/linux/icon.png %buildroot%_pixmapsdir/espanso.png
sed -i 's/^Icon=icon$/Icon=espanso/' %buildroot%_desktopdir/espanso.desktop

cat > %buildroot%_bindir/espanso <<'EOF'
#!/bin/sh
# Espanso wrapper: auto-select backend based on session type
if [ -n "$WAYLAND_DISPLAY" ] && [ -x /usr/bin/espanso-wayland ]; then
    exec /usr/bin/espanso-wayland "$@"
elif [ -x /usr/bin/espanso-x11 ]; then
    exec /usr/bin/espanso-x11 "$@"
elif [ -x /usr/bin/espanso-wayland ]; then
    exec /usr/bin/espanso-wayland "$@"
else
    echo "Error: no espanso backend installed (espanso-x11 or espanso-wayland)" >&2
    exit 1
fi
EOF
chmod 755 %buildroot%_bindir/espanso

sed 's|{{{espanso_path}}}|/usr/bin/espanso-x11|' \
    espanso/src/res/linux/systemd.service > espanso-x11.service

sed 's|{{{espanso_path}}}|/usr/bin/espanso-wayland|' \
    espanso/src/res/linux/systemd.service > espanso-wayland.service

install -Dm 644 espanso-x11.service %buildroot%_userunitdir/espanso-x11.service
install -Dm 644 espanso-wayland.service %buildroot%_userunitdir/espanso-wayland.service

%files

%files common
%doc LICENSE README.md
%_bindir/espanso
%_desktopdir/espanso.desktop
%_pixmapsdir/espanso.png

%files x11
%_bindir/espanso-x11
%_userunitdir/espanso-x11.service

%files wayland
%_bindir/espanso-wayland
%_userunitdir/espanso-wayland.service

%post x11
%systemd_user_post espanso-x11.service

%preun x11
%systemd_user_preun espanso-x11.service

%post wayland
%systemd_user_post espanso-wayland.service

%preun wayland
%systemd_user_preun espanso-wayland.service

%changelog
* Mon Jul 27 2026 Sergey Palcheh <minergenon@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Tue Jul 14 2026 Sergey Palcheh <minergenon@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus
