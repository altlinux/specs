%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: fstl
Version: 0.11.1
Release: alt1

Summary: Fast STL file viewer
License: MIT
Group: Engineering
Url: https://github.com/fstl-app/fstl

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5)

%description
fstl is a viewer for .stl files commonly used in stereolithography,
rapid prototyping, 3D printing and CAM.

It is optimized to quickly load and render very high-polygon models.

%prep
%setup
sed -i "s/Categories=.*/Categories=Science;Engineering;/" xdg/fstlapp-fstl.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

install -Dm 0644 xdg/fstlapp-fstl.desktop -t %buildroot%_desktopdir

for sz in 16x16 22x22 32x32 48x48 64x64 128x128 256x256
do
  install -Dm 0644 xdg/icons/fstlapp-fstl_${sz}.png  %buildroot%_iconsdir/hicolor/${sz}/apps/fstlapp-fstl.png
done

%files
%doc README.md
%_bindir/fstl
%_desktopdir/fstlapp-fstl.desktop
%_iconsdir/hicolor/*/apps/fstlapp-fstl.png

%changelog
* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus
