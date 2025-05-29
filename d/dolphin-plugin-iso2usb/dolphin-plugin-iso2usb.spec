%define _name iso2usb

Name: dolphin-plugin-iso2usb
Version: 20250529
Release: alt1

Summary: Dolphin service menu to write ISO images to USB driver using "isoimagewriter"

License: CC-BY
Group:   Graphical desktop/KDE

URL:     https://store.kde.org/p/1186355
VCS:	 https://store.kde.org/p/1186355

BuildArch: noarch

Source: %name-%version.tar

Patch: iso2usb-20250529-alt-fixes.patch

Requires: isoimagewriter

%description
%summary.

%prep
%setup

%patch -p0

%build
%install
install -D %_name.desktop %buildroot%_datadir/kio/servicemenus/%_name.desktop

%files
%_datadir/kio/servicemenus/%_name.desktop

%changelog
* Thu May 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250529-alt1
- Initial build for ALT Linux.
- Added russian language.
