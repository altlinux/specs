%define _unpackaged_files_terminate_build 1

Name: wallpapers-alt-atomic
Version: 0.1.2
Release: alt1

Summary: Background images for the ALT Atomic
License: CC-BY-NC-SA-4.0
Group: Graphical desktop/Other
URL: https://atomic.alt-gnome.ru/
VCS: https://altlinux.space/alt-atomic/backgrounds.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: %_bindir/magick
BuildRequires: %_bindir/rsvg-convert

%description
This packages contains wallpapers from the ALT Atomic Community.

%package gnome
Summary: Background images for the ALT Atomic in GNOME format
Group: Graphical desktop/GNOME

%description gnome
This package contains wallpapers from the ALT Atomic Community.
Wallpapers are placed in the GNOME standard path.

%package kde
Summary: Background images for the ALT Atomic in KDE format
Group: Graphical desktop/KDE

%description kde
This package contains wallpapers from the ALT Atomic Community.
Wallpapers are placed in the KDE standard path.

%prep
%setup
%autopatch -p1

%build
%meson -Dtarget_de=all
%meson_build

%install
%meson_install

%files gnome
%_datadir/backgrounds/alt-atomic/
%_datadir/gnome-background-properties/alt-atomic-*.xml

%files kde
%_datadir/wallpapers/alt-atomic-*

%changelog
* Sat Apr 18 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1.2-alt1
- New version: 0.1.2.
- Atomic logo made bigger.

* Mon Mar 09 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1.1-alt1
- Initial build.
