Name:     sddm-config-editor
Version:  0.1
Release:  alt1.20170916%ubt

Summary:  SDDM Configuration Editor
License:  ASL 2.0
Group:    Graphical desktop/KDE
Url:      https://github.com/hagabaka/sddm-config-editor

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++
BuildRequires: qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Widgets)

%description
%summary

%prep
%setup
sed -i 's|/etc/sddm.conf|%_sysconfdir/X11/sddm/sddm.conf|g' \
       cpp/controller.cpp ruby/sddm-config-editor
sed -i 's|Exec=sddm-config-editor|Exec=xdg-su -c sddm-config-editor|g' \
       data/sddm-config-editor.desktop

%build
pushd cpp
export PATH=%_qt5_bindir:$PATH
%qmake_qt5
%make_build
popd

%install
pushd cpp
%makeinstall_std INSTALL_ROOT=%buildroot
popd

%files
%_bindir/%name
%_desktopdir/%name.desktop
%doc README.md

%changelog
* Sun Feb 18 2018 Anton Midyukov <antohami@altlinux.org> 0.1-alt1.20170916%ubt
- Initial build for Sisyphus
