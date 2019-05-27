%define _unpackaged_files_terminate_build 1

Name: qview
Version: 2.0
Release: alt1

Summary: Practical and minimal image viewer
License: GPLv3
Group: Graphics

URL: https://github.com/jurplel/qView
Source: %name-%version.tar

BuildRequires: qt5-base-devel

%description
qView is an image viewer designed with minimalism and usability in mind.


%prep
%setup

%build
qmake-qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
rm -f %buildroot/usr/share/licenses/qview/LICENSE

%files
%_bindir/%name
%_desktopdir/qView.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%doc LICENSE

%changelog
* Mon May 27 2019 Alexander Makeenkov <amakeenk@altlinux.org> 2.0-alt1
- Initial build for ALT
