Name:    gpuvis
Version: 0.2
Release: alt1

Summary: GPU Trace Visualizer
License: MIT
Group:   Development/Tools
URL:     https://github.com/mikesart/gpuvis

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ cmake meson
BuildRequires: libSDL2-devel libfreetype-devel libgtk+3-devel rapidjson-devel

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
install -Dm0644 com.github.gpuvis.Gpuvis.desktop \
%buildroot%_desktopdir/com.github.gpuvis.Gpuvis.desktop

install -Dm0644 com.github.gpuvis.Gpuvis.svg \
%buildroot%_iconsdir/hicolor/scalable/apps/com.github.gpuvis.Gpuvis.svg

install -Dm0644 com.github.gpuvis.Gpuvis.metainfo.xml \
%buildroot%_datadir/metainfo/com.github.gpuvis.Gpuvis.metainfo.xml

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/com.github.gpuvis.Gpuvis.desktop
%_iconsdir/hicolor/scalable/apps/com.github.gpuvis.Gpuvis.svg
%_datadir/metainfo/com.github.gpuvis.Gpuvis.metainfo.xml

%changelog
* Thu Jun 25 2026 Sergey Palcheh <minergenon@altlinux.org> 0.2-alt1
- Initial build for Sisyphus
