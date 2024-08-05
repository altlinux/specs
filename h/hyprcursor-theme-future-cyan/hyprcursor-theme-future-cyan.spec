%define theme future-cyan
%define themename Future-Cyan-Hyprcursor_Theme

Name: hyprcursor-theme-%theme
Version: 20240718
Release: alt1
License: GPL-3.0-or-later

Summary: Future-cursor for Hyprcursor

Group: Graphical desktop/Other

Url: https://gitlab.com/Pummelfisch/future-cyan-hyprcursor

BuildArch: noarch
Source: %name-%version.tar

%description
This is an Hyprcursor theme, that was forked and ported from the
Future-cursor x-cursor theme, which itself was based on capitaine-cursors.

%prep
%setup

%install
install -d %buildroot%_iconsdir/%themename
cp -r %themename/hyprcursors %buildroot%_iconsdir/%themename
cp %themename/manifest.hl %buildroot%_iconsdir/%themename

%files
%doc README.md LICENSE
%_iconsdir/%themename/

%changelog
* Mon Aug 05 2024 Kirill Unitsaev <fiersik@altlinux.org> 20240718-alt1
- Initial build
