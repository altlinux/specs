%define _unpackaged_files_terminate_build 1

Name: wallpapers-alt-regular
Version: 0.4.5
Release: alt1

Summary: Background images for the ALT Regular
License: CC-BY-SA-4.0
Group: Graphical desktop/Other
Url: https://github.com/alt-gnome-team/alt-regular-backgrounds
Vcs: https://github.com/alt-gnome-team/alt-regular-backgrounds.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
This packages contains wallpapers from the ALT Regular community.

%package gnome
Summary: Background images for the ALT Regular GNOME
Group: Graphical desktop/GNOME

%description gnome
This package contains wallpapers from the ALT Regular community.
Wallpapers are placed in the GNOME standard path.

%package kde
Summary: Background images for the ALT Regular KDE
Group: Graphical desktop/KDE

%description kde
This package contains wallpapers from the ALT Regular community.
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
%_datadir/backgrounds/alt-regular-gnome/
%_datadir/gnome-background-properties/alt-regular-gnome-*.xml

%files kde
%_datadir/wallpapers/alt-regular-kde-*

%changelog
* Thu Feb 20 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.4.5-alt1
- Initial build.

