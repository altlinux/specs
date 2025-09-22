# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/icons to altlinux branch 

%define _unpackaged_files_terminate_build 1

Name: icon-theme-alt-atomic
Version: 0.2
Release: alt1

Summary: Icon theme for ALT Atomic
Group: Graphics
License: CC-BY-SA-4.0
Url: https://atomic.alt-gnome.ru/
Vcs: https://altlinux.space/alt-atomic/icons.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: %_bindir/rsvg-convert

%description
%summary.

%package onyx
Summary: ALT Atomic Onyx theme
Group: Graphics

BuildArch: noarch

Requires: icon-theme-morewaita
Requires: icon-theme-adwaita
Requires: icon-theme-adwaita-legacy
Requires: alt-atomic-icons

%description onyx
%summary.

%package -n alt-atomic-icons
Summary: ALT Atomic icons
Group: Graphics

BuildArch: noarch

Requires: icon-theme-hicolor

%description -n alt-atomic-icons
%summary.

%prep
%setup

%build
./create_png
%meson
%meson_build

%install
%meson_install

%files onyx
%_iconsdir/ALTAtomicOnyx

%files -n alt-atomic-icons
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg

%changelog
* Thu Sep 11 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.2-alt1
- Fixed logo visual issues.
- Deleted subpackage with logos.

* Thu Aug 21 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1-alt1
- Initial build.
