%global origname TelegramQML

Name: telegramqml
Version: 2.0.0
Release: alt4

Summary: Telegram API tools for QtQml and Qml
License: GPLv3+
Group:   System/Configuration/Other

Url: https://github.com/Aseman-Land/TelegramQML
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %origname-%version.tar

# Cherry-picked patches from upstream
#Patch:	TelegramQML-2.0.0-Add-SharedPointer-Qml.patch

Patch0001: 0001-Add-support-for-secret-chats-on-the-DialogListModel.patch
Patch0002: 0002-Fix-the-passHash-bug.patch
Patch0003: 0003-Fix-no-return-in-nonvoid-function.patch
Patch0004: 0004-Add-SharedPointer-Qml-component-to-use-TelegramShare.patch

BuildRequires(pre): rpm-macros-qt5 rpm-macros-qt5-webengine

# Automatically added by buildreq on Fri Apr 21 2017
# optimized out: gcc-c++ libGL-devel libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-qml libqt5-quick libqt5-sql libqt5-xml libstdc++-devel python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-webchannel-devel qt5-xmlpatterns-devel
BuildRequires: libqtelegram-ae-devel libssl-devel python3-module-zope qt5-3d-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-quickcontrols2-devel qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel zlib-devel

BuildRequires: libssl-devel python3-module-zope qt5-3d-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-quickcontrols2-devel qt5-sensors-devel qt5-serialport-devel qt5-speech-devel
BuildRequires: qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel zlib-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webengine-devel
%endif

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: libssl-devel
BuildRequires: qt5-multimedia-devel

%description
%summary.

%prep
%setup -n %origname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%add_optflags -Wno-narrowing
%qmake_qt5

%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std


%files
%doc LICENSE
%_qt5_qmldir/TelegramQml/

%changelog
* Thu Sep 16 2021 Michael Shigorin <mike@altlinux.org> 2.0.0-alt4
- avoid webengine where unavailable

* Tue Apr 13 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt3
- Fixed FTBFS with -Wno-narrowing.

* Tue Feb 05 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Rebuild with libqtelegram-ae-devel (Closes: #35990).

* Fri Apr 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.0.0-3
- Backport couple of patches from upstream

* Sun Jul 24 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.0.0-2
- Trivial fixes

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.0.0-1
- Initial package

