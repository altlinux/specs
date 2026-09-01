Name:    volt-gui
Version: 2.1.0
Release: alt1

Summary: A graphical control panel for Vulkan games on Linux
License: GPL-3.0-only
Group:   System/Configuration/Hardware
URL:     https://github.com/pythonlover02/volt-gui

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust rpm-build-python3
BuildRequires: libxcb-devel
Requires: python3-module-pyside6

%description
volt-gui is a graphical control panel for Vulkan games on Linux. Settings are
applied by volt, a Vulkan implicit layer written in Rust, so they work on
every Vulkan driver: RADV, ANV, NVK, AMDVLK, the NVIDIA proprietary driver.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
# Rust: launcher, probe binary and the Vulkan implicit layer shared object
%rust_install -t %_bindir volt volt-probe
install -Dm755 target/release/libvolt.so %buildroot%_libdir/libvolt.so

# Vulkan implicit layer manifest. The loader resolves a relative library_path
# against the manifest's own directory, so point it at the absolute install path.
install -Dm644 VkLayer_volt.json \
    %buildroot%_datadir/vulkan/implicit_layer.d/VkLayer_volt.json
sed -i 's#"library_path": "libvolt.so"#"library_path": "%_libdir/libvolt.so"#' \
    %buildroot%_datadir/vulkan/implicit_layer.d/VkLayer_volt.json

# Python GUI: flat imports, run the entry point directly from its directory
mkdir -p %buildroot%_datadir/volt-gui
cp -p volt-gui/*.py %buildroot%_datadir/volt-gui/
cat > %buildroot%_bindir/volt-gui <<'EOF'
#!/bin/sh
exec python3 %_datadir/volt-gui/volt-gui.py "$@"
EOF
chmod 755 %buildroot%_bindir/volt-gui

# Desktop entry (no icon: upstream ships only screenshots, not an app icon)
install -Dm644 /dev/stdin %buildroot%_datadir/applications/volt-gui.desktop <<EOF
[Desktop Entry]
Type=Application
Name=volt-gui
Comment=Graphical control panel for Vulkan game settings
Exec=volt-gui
Terminal=false
Categories=Utility;
Keywords=vulkan;vsync;gpu;gaming;
StartupNotify=true
StartupWMClass=volt-gui
EOF

%files
%doc LICENSE README.md
%_bindir/volt
%_bindir/volt-probe
%_bindir/volt-gui
%_libdir/libvolt.so
%_datadir/vulkan/implicit_layer.d/VkLayer_volt.json
%dir %_datadir/volt-gui
%_datadir/volt-gui/*.py
%_datadir/applications/volt-gui.desktop

%changelog
* Mon Aug 31 2026 Sergey Palcheh <minergenon@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Thu Aug 27 2026 Sergey Palcheh <minergenon@altlinux.org> 2.0.3-alt1
- new version 2.0.3

* Tue Aug 25 2026 Sergey Palcheh <minergenon@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus
