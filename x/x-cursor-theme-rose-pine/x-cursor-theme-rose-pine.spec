%define theme rose-pine

Name: x-cursor-theme-%theme
Version: 1.1.0
Release: alt1
License: GPL-3.0

Summary: Rose Pine Cursor theme

Group: System/X11

Url: https://github.com/rose-pine/cursor

BuildArch: noarch

# Source-url: https://github.com/rose-pine/cursor/releases/download/v1.1.0/BreezeX-RosePine-Linux.tar.xz
Source: rose-pine-%version.tar
# Source1-url: https://github.com/rose-pine/cursor/releases/download/v%version/BreezeX-RosePineDawn-Linux.tar.xz
Source1: rose-pine-dawn-%version.tar

%description
%summary.

%package dawn
Summary: Rose Pine Dawn Cursor theme
Group: System/X11

%description dawn
%summary.

%prep
%setup -a1 -n %theme-%version

%install
install -d %buildroot%_iconsdir/%theme

cp -r cursors *.theme %buildroot%_iconsdir/%theme/

install -d %buildroot%_iconsdir/%theme-dawn
cp -r dawn/* %buildroot%_iconsdir/%theme-dawn/

%files
%_iconsdir/%theme

%files dawn
%_iconsdir/%theme-dawn

%changelog
* Wed Jun 04 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.1.0-alt1
- Initial build
