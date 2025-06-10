Name:    envision
Version: 3.0.1
Release: alt1

Summary: Envision is a GUI to setup and run either Monado or WiVRn
License: AGPL-3.0
Group:   Games/Other
Url:     https://gitlab.com/gabmus/envision

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: meson cmake git-core
BuildRequires: glib2-devel libgio-devel libgtk4-devel libvte3-devel libappstream-glib
BuildRequires: libssl-devel libadwaita-devel openxr-devel
Requires: monado-vulkan-layers

ExclusiveArch: x86_64

%description
Envision is a graphical app that acts as an orchestrator to get a full
Monado or WiVRn setup up and running with a few clicks.
Envision attempts to construct a working runtime with both a native
OpenXR and an OpenVR API, provided by OpenComposite, for client
aplications to utilize.
Please note the OpenVR implementation is incomplete and contains only
what's necessary to run most games for compatibility.

Be very careful while in VR using this app!

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
meson setup build -Dprefix="%buildroot/build/localprefix" -Dprofile=development
ninja -C build

%install
ninja -C build install
mv %buildroot/build/localprefix/ %buildroot%_prefix/
rm -rf %buildroot%_desktopdir/mimeinfo.cache
rm -rf %buildroot%_iconsdir/hicolor/icon-theme.cache

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/%name/
%_datadir/metainfo/org.gabmus.envision.Devel.appdata.xml
%_desktopdir/org.gabmus.envision.Devel.desktop
%_iconsdir/hicolor/scalable/apps/org.gabmus.envision.Devel.svg
%_iconsdir/hicolor/symbolic/apps/org.gabmus.envision.Devel-symbolic.svg

%changelog
* Mon Mar 24 2025 Sergey Palcheh <minergenon@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus

