%define _unpackaged_files_terminate_build 1

Name: numix-icon-theme
Version: 25.12.15
Release: alt1

Summary: Official base icon theme from the Numix project
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://github.com/numixproject/numix-icon-theme

Source: %name-%version.tar

BuildArch: noarch

%description
The Numix icon theme is designed to look fresh, swishy and modern using
white symbols on vividly coloured background for applications and simplistic
devices, toolbars and status icons.

%prep
%setup

%build
# nothing to build here

%install
install -d %buildroot%_iconsdir

mkdir -p %buildroot%_datadir/doc/%name
cp -pr Numix %buildroot%_iconsdir/Numix
cp -pr Numix-Light %buildroot%_iconsdir/Numix-Light

%files
%doc license readme.md
%_iconsdir/Numix
%_iconsdir/Numix-Light

# prevent "find-provides: broken symbolic link" messages
%exclude %_iconsdir/Numix/16/devices/gnome-dev-media-sm.svg
%exclude %_iconsdir/Numix/16/mimetypes/application-vnd.shp.svg
%exclude %_iconsdir/Numix/16/mimetypes/application-vnd.shx.svg
%exclude %_iconsdir/Numix/22/devices/gnome-dev-media-sm.svg
%exclude %_iconsdir/Numix/22/mimetypes/application-vnd.shp.svg
%exclude %_iconsdir/Numix/22/mimetypes/application-vnd.shx.svg
%exclude %_iconsdir/Numix/24/devices/gnome-dev-media-sm.svg
%exclude %_iconsdir/Numix/24/mimetypes/application-vnd.shp.svg
%exclude %_iconsdir/Numix/24/mimetypes/application-vnd.shx.svg
%exclude %_iconsdir/Numix/32/devices/gnome-dev-media-sm.svg
%exclude %_iconsdir/Numix/32/mimetypes/application-vnd.shp.svg
%exclude %_iconsdir/Numix/32/mimetypes/application-vnd.shx.svg
%exclude %_iconsdir/Numix/48/devices/gnome-dev-media-sm.svg
%exclude %_iconsdir/Numix/48/mimetypes/application-vnd.shp.svg
%exclude %_iconsdir/Numix/48/mimetypes/application-vnd.shx.svg
%exclude %_iconsdir/Numix/64/devices/gnome-dev-media-sm.svg
%exclude %_iconsdir/Numix/64/mimetypes/application-vnd.shp.svg
%exclude %_iconsdir/Numix/64/mimetypes/application-vnd.shx.svg

%changelog
* Sat Dec 20 2025 Nikolay Strelkov <snk@altlinux.org> 25.12.15-alt1
- New version 25.12.15.

* Thu Oct 30 2025 Nikolay Strelkov <snk@altlinux.org> 25.10.26-alt1
- New version 25.10.26.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 25.10.17.2-alt1
- New version 25.10.17.2.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 25.10.14-alt1
- New version 25.10.14.

* Sun Feb 09 2025 Nikolay Strelkov <snk@altlinux.org> 25.01.31-alt1
- Initial build for Sisyphus
