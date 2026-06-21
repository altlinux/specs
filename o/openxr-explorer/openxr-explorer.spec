%define _unpackaged_files_terminate_build 1

Name:    openxr-explorer
Version: 1.7
Release: alt1

Summary: Cross-platform OpenXR explorer and runtime switcher with CLI/GUI
License: MIT
Group:   System/Libraries
URL:     https://github.com/maluoi/openxr-explorer

Source: %name-%version.tar
Patch0: openxr-explorer-1.7-use-system-deps.patch
Patch1: openxr-explorer-1.7-set-wm-class.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: openxr-devel nlohmann-json-devel libxcb-devel libxcbutil-keysyms-devel
BuildRequires: libxcbutil-cursor-devel libX11-devel libglvnd-devel libGLEW-devel
BuildRequires: ImageMagick-tools

%description
OpenXR Explorer is a handy debug tool for OpenXR developers. It allows for easy
switching between OpenXR runtimes, shows lists of the runtime's supported extensions,
and allows for inspection of common properties and enumerations, with direct links
to relevant parts of the OpenXR specification!

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# Desktop entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%name.desktop <<EOF
[Desktop Entry]
Name=OpenXR Explorer
Comment=Cross-platform OpenXR explorer and runtime switcher with CLI/GUI
Exec=openxr-explorer
Icon=openxr-explorer
StartupWMClass=openxr-explorer
Terminal=false
Type=Application
Categories=Development;Utility;
EOF

# Extract the largest icon from the upstream .ico file and generate the icon set
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
best_idx=$(magick src/openxrexplorer/oxr-explorer-icon.ico -format '%p %w %h\n' info: \
           | awk '{print $1, $2*$3}' | sort -k2,2n | tail -1 | cut -d' ' -f1)
magick "src/openxrexplorer/oxr-explorer-icon.ico[$best_idx]" \
    %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
for res in 16 32 48 128 256; do
    mkdir -p %buildroot%_iconsdir/hicolor/${res}x${res}/apps/
    magick %buildroot%_iconsdir/hicolor/64x64/apps/%name.png -resize ${res}x${res} \
        %buildroot%_iconsdir/hicolor/${res}x${res}/apps/%name.png
done

%files
%doc LICENSE README.md
%_bindir/openxr-explorer
%_bindir/xrsetruntime
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sun Jun 21 2026 Sergey Palcheh <minergenon@altlinux.org> 1.7-alt1
- Initial build for Sisyphus

