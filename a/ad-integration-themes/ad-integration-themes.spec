Name: ad-integration-themes
Version: 3.0
Release: alt1

Summary: Icon themes for AD integration BaseAlt projects
License: GPLv3+
Group:   Other
Url:     https://gitlab.basealt.space/knyazevsr/ad-integration-themes

Source: %name-%version.tar
BuildArch: noarch

%description
Themes pack for BaseAlt Active Directory integration projects
like ADMC, GPUI and other.

%prep
%setup

%install
mkdir -p %buildroot%_iconsdir/%name
cp -R scalable/ index.theme %buildroot%_iconsdir/%name

%files
%doc LICENSE README.md
%_iconsdir/%name

%changelog
* Wed Aug 20 2025 Semyon Knyazev <samael@altlinux.org> 3.0-alt1
- Move icon theme files to parent directory
- Change parent theme from Papirus to gnome
- Change domain info item and computer icon

* Tue Jun 03 2025 Semyon Knyazev <samael@altlinux.org> 2.0-alt1
- Removed themes ad-integration-line/duotone/color
- Changed theme name AD-integration Kora to AD-integration
- Updated AD-integration theme icons
- Renamed error and action icons

* Tue Dec 12 2023 Semyon Knyazev <samael@altlinux.org> 1.0-alt1
- Append AD-integration color, AD-integration duotone, AD-integration line
  and Kora AD-integration themes. These were tested only in ADMC context and
  can be expanded for other projects (like GPUI).
