# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     mpc-qt
Version:  23.02
Release:  alt1

Summary:  A clone of Media Player Classic reimplemented in Qt.
License:  GPL-2.0
Group:    Video
Url:      https://github.com/mpc-qt/mpc-qt

Source:   %name-%version.tar

BuildRequires: qt5-tools-devel
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: libmpv-devel

%description
Media Player Classic Home Cinema (mpc-hc) is considered by many to be the
quintessential media player for the Windows desktop.
Media Player Classic Qute Theater (mpc-qt) aims to reproduce most of the
interface and functionality of mpc-h.

%prep
%setup
rm -rf mpv-dev

%build
%qmake_qt5 PREFIX=%prefix MPCQT_VERSION=%version
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%_bindir/%name
%_desktopdir/io.github.mpc_qt.Mpc-Qt.desktop
%_defaultdocdir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/metainfo/io.github.mpc_qt.Mpc-Qt.appdata.xml

%changelog
* Thu Feb 16 2023 Anton Midyukov <antohami@altlinux.org> 23.02-alt1
- - New version 23.02

* Sat Feb 26 2022 Anton Midyukov <antohami@altlinux.org> 22.02-alt1
- New version 22.02
- Update url

* Sun Nov 29 2020 Anton Midyukov <antohami@altlinux.org> 20.10-alt1
- New version 20.10
- Update url

* Mon Dec 23 2019 Anton Midyukov <antohami@altlinux.org> 19.06-alt1
- New snapshot
- Update url
- fix changelog typo

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 18.03-alt2
- NMU: fixed build with Qt-5.11.

* Thu Jun 21 2018 Andrey Solodovnikov <hepoh@altlinux.org> 18.03-alt1
- Initial build for Sisyphus
