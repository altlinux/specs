# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define app_id io.github.mpc_qt.mpc-qt

Name:     mpc-qt
Version:  26.01
Release:  alt1

Summary:  A clone of Media Player Classic reimplemented in Qt
License:  GPL-2.0
Group:    Video

URL:      https://github.com/mpc-qt/mpc-qt
VCS:      https://github.com/mpc-qt/mpc-qt.git

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: libmpv-devel

%description
Media Player Classic Home Cinema (mpc-hc) is considered by many to be the
quintessential media player for the Windows desktop.
Media Player Classic Qute Theater (mpc-qt) aims to reproduce most of the
interface and functionality of mpc-h.

%prep
%setup
%patch -p1
rm -rf mpv-dev

%build
%cmake -DMPCQT_VERSION=%version
%cmake_build

%install
%cmake_install
rm -r %buildroot%_defaultdocdir/%name

%files
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/%app_id.metainfo.xml
%doc LICENSE README.md DOCS/ipc.md

%changelog
* Tue Mar 17 2026 Polina Poidenko <polipoki@altlinux.org> 26.01-alt1
- New version 26.01.

* Mon Jul 21 2025 Anton Midyukov <antohami@altlinux.org> 25.07-alt1
- New version 25.07.
- Revert mpc-qt.desktop: remove MimeType and X-KDE-Protocols.

* Mon Dec 23 2024 Anton Midyukov <antohami@altlinux.org> 24.12-alt2
- mpc-qt.desktop: remove MimeType and X-KDE-Protocols

* Sat Dec 14 2024 Anton Midyukov <antohami@altlinux.org> 24.12-alt1
- New version 24.12.

* Mon Jul 15 2024 Anton Midyukov <antohami@altlinux.org> 24.06-alt1
- New version 24.06

* Mon Jan 01 2024 Anton Midyukov <antohami@altlinux.org> 23.12-alt1
- New version 23.12
- build with qt6

* Thu Feb 16 2023 Anton Midyukov <antohami@altlinux.org> 23.02-alt1
- New version 23.02

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
