%define _unpackaged_files_terminate_build 1

Name:    cinny-desktop
Version: 4.12.6
Release: alt1

Summary: Yet another matrix client for desktop
License: AGPL-3.0
Group:   Networking/Chat

URL:     https://cinny.in
VCS:     https://github.com/cinnyapp/cinny-desktop

Source0: %name-%version.tar
Source1: %name-%version-cinny.tar
Source2: %name-%version-node_modules.tar
Source3: %name-%version-cinny-node_modules.tar
Source4: %name-%version-vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: npm
BuildRequires: libdbus-devel
BuildRequires: librsvg-devel
BuildRequires: libwebkit2gtk4.1-devel

%description
Cinny is a matrix client focusing primarily on simple, elegant and secure
interface. The desktop app is made with Tauri.

%prep
%setup -a1 -a2 -a3 -a4
cd src-tauri
sed -i 's/"createUpdaterArtifacts": "v1Compatible"/"createUpdaterArtifacts": false/' \
		tauri.conf.json
%rust_prep

%build
npm run tauri -- \
	build --bundles deb -- \
	--frozen --no-default-features --features custom-protocol

%install
cp -a src-tauri/target/release/bundle/deb/Cinny_%{version}_*/data %buildroot

%files
%doc *.md
%_bindir/cinny
%_desktopdir/Cinny.desktop
%_iconsdir/hicolor/*/apps/cinny.png

%changelog
* Tue Aug 11 2026 Ilya Sorochan <k0tran@altlinux.org> 4.12.6-alt1
- Initial build.
