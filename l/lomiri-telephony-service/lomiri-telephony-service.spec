%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without check

Name: lomiri-telephony-service
Version: 0.6.1
Release: alt1

Summary: Telephony service components for Lomiri
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-telephony-service

Source: %name-%version.tar

# sync with version 0.6.1-1 from Debian unstable + fix building
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Contacts)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Feedback)
BuildRequires: libphonenumber-devel
BuildRequires: telepathy-qt5-devel
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(telepathy-farstream)
BuildRequires: pkgconfig(lomiri-history-service)
BuildRequires: pkgconfig(messaging-menu)
BuildRequires: pkgconfig(libusermetricsinput-1)
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: libtelepathy-mission-control

%if_with check
BuildRequires: ctest
BuildRequires: dbus-test-runner
BuildRequires: dconf
BuildRequires: /usr/bin/xvfb-run
BuildRequires: /usr/bin/gnome-keyring-daemon
%endif

# qt5/qml/Lomiri/Components/ListItems/qmldir qt5/qml/Lomiri/Components/Pickers/qmldir qt5/qml/Lomiri/Components/Popups/qmldir qt5/qml/Lomiri/Components/Styles/qmldir qt5/qml/Lomiri/Components/qmldir
Requires: lomiri-ui-toolkit

Requires: lomiri-sounds

%description
Telephony service components for Lomiri.

This package contains the backend components providing the telephony
features such as calling and texting, QML plugins providing the features
from the telephony service to applications and the features from the
telephony PhoneNumber to applications.

%prep
%setup
%patch -p1

%build
%cmake \
       -DQMAKE_EXECUTABLE=/usr/bin/qmake-qt5 \
       -DENABLE_COVERAGE=OFF \
%if_with check
       -DBUILD_TESTING=ON \
       -DSKIP_QML_TESTS=OFF
%else
       -DBUILD_TESTING=OFF \
       -DSKIP_QML_TESTS=ON
%endif
%cmake_build

%install
%cmake_install

%find_lang %name

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.CC-BY-SA-3 README.md TODO
%_bindir/lomiri-indicator-telephony-service
%_bindir/lomiri-ofono-setup
%_bindir/lomiri-telephony-service-approver
%_bindir/lomiri-telephony-service-handler
%_bindir/phone-gsettings-migration.py
%_qt5_qmldir/Lomiri/Telephony/PhoneNumber/PhoneNumber.js
%_qt5_qmldir/Lomiri/Telephony/PhoneNumber/PhoneNumberField.qml
%_qt5_qmldir/Lomiri/Telephony/PhoneNumber/PhoneNumberInput.qml
%_qt5_qmldir/Lomiri/Telephony/PhoneNumber/liblomiritelephonyservice-phonenumber-qml.so
%_qt5_qmldir/Lomiri/Telephony/PhoneNumber/qmldir
%_qt5_qmldir/Lomiri/Telephony/liblomiritelephonyservice-qml.so
%_qt5_qmldir/Lomiri/Telephony/qmldir
%_datadir/accountsservice/interfaces/com.lomiri.TelephonyServiceApprover.xml
%_desktopdir/lomiri-telephony-service-call.desktop
%_desktopdir/lomiri-telephony-service-sms.desktop
%_datadir/dbus-1/interfaces/com.lomiri.TelephonyServiceApprover.xml
%_datadir/dbus-1/services/com.lomiri.TelephonyServiceHandler.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.TelephonyServiceApprover.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.TelephonyServiceHandler.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.TelephonyServiceIndicator.service
%_iconsdir/hicolor/48x48/apps/lomiri-telephony-service-call.png
%_iconsdir/hicolor/48x48/apps/lomiri-telephony-service-message.png
%_iconsdir/ubuntu-mono-dark/status/16/indicator-call.svg
%_iconsdir/ubuntu-mono-dark/status/22/indicator-call.svg
%_iconsdir/ubuntu-mono-dark/status/24/indicator-call.svg
%_iconsdir/ubuntu-mono-light/status/16/indicator-call.svg
%_iconsdir/ubuntu-mono-light/status/22/indicator-call.svg
%_iconsdir/ubuntu-mono-light/status/24/indicator-call.svg
%_datadir/lomiri-telephony-service/assets/avatar-default@18.png
%_datadir/lomiri-telephony-service/assets/contact-group.svg
%_datadir/lomiri-telephony-service/assets/message_watermark.png
%_datadir/lomiri-telephony-service/protocols/ofono.protocol
%_datadir/lomiri-telephony-service/protocols/sip.protocol
%_datadir/notify-osd/icons/Humanity/scalable/status/notification-group-call.svg
%_datadir/notify-osd/icons/Humanity/scalable/status/notification-unavailable-image-call.svg
%_datadir/notify-osd/icons/Humanity/scalable/status/notification-unknown-call.svg
%_datadir/polkit-1/actions/com.lomiri.TelephonyServiceApprover.policy
%_datadir/polkit-1/rules.d/50-com.lomiri.TelephonyServiceApprover.rules
%_datadir/telepathy/clients/LomiriTelephonyServiceApprover.client
%_datadir/telepathy/clients/LomiriTelephonyServiceHandler.client
%_datadir/telepathy/clients/LomiriTelephonyServiceIndicator.client
%_var/lib/polkit-1/localauthority/10-vendor.d/50-com.lomiri.TelephonyServiceApprover.pkla

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-telephony-service.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-telephony-service.mo

%changelog
* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
