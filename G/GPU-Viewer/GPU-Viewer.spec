Name:    GPU-Viewer
Version: 3.12
Release: alt1

Summary: A front-end to glxinfo, vulkaninfo, clinfo and es2_info - Linux
License: GPL-3.0
Group:   Monitoring
URL:     https://github.com/arunsivaramanneo/GPU-Viewer

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ meson
Requires: typelib(Adw)

BuildArch: noarch

%description
This project aims to capture all the important details of glxinfo, vulkaninfo
and clinfo in a GUI. The project is being developed using python 3 pygobject
with GTK4. All the important details are extracted using glxinfo/vulkaninfo/clinfo
with the combination of grep, CAT , AWK commands and displayed in the front-end.
There is no hard OpenGL Programming involved, until glxinfo, vulkaninfo and
clinfo works the GPU-viewer will also work.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/gpu-viewer
%_datadir/gpu-viewer/
%_datadir/metainfo/io.github.arunsivaramanneo.GPUViewer.metainfo.xml
%_desktopdir/io.github.arunsivaramanneo.GPUViewer.desktop
%_iconsdir/hicolor/*/apps/io.github.arunsivaramanneo.GPUViewer.png

%changelog
* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 3.12-alt1
- new version (3.12) with rpmgs script

* Wed Feb 26 2025 Sergey Palcheh <minergenon@altlinux.org> 3.10-alt1
- Initial build for Sisyphus
