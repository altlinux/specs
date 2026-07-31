Name:    xr-picker
Version: 2.2.1
Release: alt1

Summary: OpenXR Runtime Picker
License: Apache-2.0 OR MIT
Group:   System/Configuration/Other
URL:     https://github.com/rpavlik/xr-picker

Source:  %name-%version.tar
Source1: %name-development-%version.tar
Patch:   xr-picker-gui-wayland-app-id.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: glib2-devel libatk-devel libgio-devel libgtk+3-devel

%description
XR Runtime Picker for OpenXR
This is a cross-platform tool to allow you to easily change your active
OpenXR runtime.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build

%install
install -Dm 755 target/release/xrpicker %buildroot%_bindir/xrpicker
install -Dm 755 target/release/xrpicker-gui %buildroot%_bindir/xrpicker-gui

for size in 24 32 48; do
    install -Dm 644 xrpicker-gui/assets/icon/icon$size.png \
        %buildroot%_datadir/icons/hicolor/${size}x${size}/apps/%name.png
done
install -Dm 644 xrpicker-gui/assets/icon/menu-open.svg \
    %buildroot%_datadir/icons/hicolor/scalable/apps/%name.svg

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/%name.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=XR Picker
Comment=Change the active OpenXR runtime
Exec=xrpicker-gui
Icon=%name
Terminal=false
Categories=Settings;
Keywords=OpenXR;VR;runtime;
EOF

%files
%doc README.md LICENSES/*.txt
%_bindir/xrpicker
%_bindir/xrpicker-gui
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.*

%changelog
* Fri Jul 31 2026 Sergey Palcheh <minergenon@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus
