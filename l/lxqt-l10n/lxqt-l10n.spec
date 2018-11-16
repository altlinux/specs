# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-l10n
Version: 0.13.0
Release: alt2

Summary: Translations of LXQt
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar
Patch: ru-translation.patch

BuildRequires: cmake rpm-macros-cmake
BuildRequires: qt5-tools-devel
BuildRequires: lxqt-build-tools

Requires: compton-conf-l10n
Requires: libfm-qt-l10n
Requires: lximage-qt-l10n
Requires: obconf-qt-l10n
Requires: pavucontrol-qt-l10n
Requires: pcmanfm-qt-l10n
Requires: qterminal-l10n
Requires: qtermwidget-l10n

BuildArch: noarch

%description
%summary

%package -n compton-conf-l10n
Summary: Translations of compton-conf
Group: Graphical desktop/Other

%description -n compton-conf-l10n
Translations of compton-conf

%package -n libfm-qt-l10n
Summary: Translations of libfm-qt
Group: Graphical desktop/Other

%description -n libfm-qt-l10n
Translations of libfm-qt

%package -n lximage-qt-l10n
Summary: Translations of lximage-qt
Group: Graphical desktop/Other

%description -n lximage-qt-l10n
Translations of lximage-qt

%package -n obconf-qt-l10n
Summary: Translations of obconf-qt
Group: Graphical desktop/Other

%description -n obconf-qt-l10n
Translations of obconf-qt

%package -n pavucontrol-qt-l10n
Summary: Translations of pavucontrol-qt
Group: Graphical desktop/Other

%description -n pavucontrol-qt-l10n
Translations of pavucontrol-qt

%package -n pcmanfm-qt-l10n
Summary: Translations of pcmanfm-qt
Group: Graphical desktop/Other

%description -n pcmanfm-qt-l10n
Translations of pcmanfm-qt

%package -n qterminal-l10n
Summary: Translations of qterminal
Group: Graphical desktop/Other

%description -n qterminal-l10n
Translations of qterminal

%package -n qtermwidget-l10n
Summary: Translations of qtermwidget
Group: Graphical desktop/Other

%description -n qtermwidget-l10n
Translations of qtermwidget

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS CHANGELOG COPYING README.md
%dir %_datadir/lxqt
%_datadir/lxqt/translations

%files -n compton-conf-l10n
%dir %_datadir/compton-conf
%_datadir/compton-conf/translations

%files -n libfm-qt-l10n
%dir %_datadir/libfm-qt
%_datadir/libfm-qt/translations

%files -n lximage-qt-l10n
%dir %_datadir/lximage-qt
%_datadir/lximage-qt/translations

%files -n obconf-qt-l10n
%dir %_datadir/obconf-qt
%_datadir/obconf-qt/translations

%files -n pavucontrol-qt-l10n
%dir %_datadir/pavucontrol-qt
%_datadir/pavucontrol-qt/translations

%files -n pcmanfm-qt-l10n
%dir %_datadir/pcmanfm-qt
%_datadir/pcmanfm-qt/translations

%files -n qterminal-l10n
%dir %_datadir/qterminal
%_datadir/qterminal/translations

%files -n qtermwidget-l10n
%dir %_datadir/qtermwidget
%_datadir/qtermwidget/translations

%changelog
* Fri Nov 16 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt2
- Update russian translation
- Divided into subpackages

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- built for sisyphus

