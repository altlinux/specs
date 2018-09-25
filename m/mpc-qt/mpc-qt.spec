Name:     mpc-qt
Version:  18.03
Release:  alt2

Summary:  A clone of Media Player Classic reimplemented in Qt.
License:  GPL-2.0
Group:    Video
Url:      https://github.com/cmdrkotori/mpc-qt

Source:   %name-%version.tar

Patch1: %name-%version-upstream-qt5.11.patch

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
%patch1 -p1

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_defaultdocdir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name

%changelog
* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 18.03-alt2
- NMU: fixed build with Qt-5.11.

* Thu Jun 21 2018 Andrey Solodovnikov <hepoh@altlinux.org> 18.03-alt1
Initial build for Sisyphus
