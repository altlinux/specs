Name:    qalculate-qt
Version: 5.3.0
Release: alt1

Summary: A very versatile desktop calculator - Qt version
Group:   Office
License: GPL-2.0+

URL: https://qalculate.github.io/
VCS: https://github.com/Qalculate/qalculate-qt

Source0: %name-%version.tar

BuildRequires: qt6-base-devel
BuildRequires: qt6-tools
BuildRequires: libqalculate-devel >= %version

%description
A Qt graphical interface for Qalculate!

%prep
%setup

%build
%qmake_qt6 PREFIX=/usr
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc README.md README COPYING AUTHORS

%_bindir/qalculate-qt

%_desktopdir/io.github.Qalculate.qalculate-qt.desktop
%_iconsdir/hicolor/*/apps/qalculate-qt.png
%_iconsdir/hicolor/scalable/apps/qalculate-qt.svg

%_man1dir/qalculate-qt.1.xz
%_datadir/metainfo/io.github.Qalculate.qalculate-qt.metainfo.xml

%_datadir/qalculate-qt/translations/qalculate-qt_*.qm

%changelog
* Mon Jan 13 2025 Ilya Sorochan <k0tran@altlinux.org> 5.3.0-alt1
- Initial build.
