Name: telegram-qt5
Summary: Qt library for Telegram network

%define libtelegramqt5 lib%name

Version: 0.1.0
Release: alt1%ubt
Group: System/Libraries
License: LGPLv2.1
URL: https://github.com/Kaffeine/telegram-qt
Source0: telegram-qt5-%version.tar
buildRequires(pre): rpm-build-ubt
BuildRequires: libssl-devel qt5-base-devel qt5-declarative-devel zlib-devel
BuildRequires: cmake

%description
%summary.

%package -n %libtelegramqt5
Summary: Qt library for Telegram network
Group: System/Libraries
Requires: libqt5-core
Requires: libqt5-network
Requires: openssl

%description -n %libtelegramqt5
%summary.

%package -n %libtelegramqt5-devel
Summary:    Development headers and pkg-config for TelegramQt library
Group:      Development/KDE and QT
%description -n %libtelegramqt5-devel
%summary.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n %libtelegramqt5
%_libdir/libtelegram-qt5.so.*

%files -n %libtelegramqt5-devel
%_libdir/libtelegram-qt5.so
%_includedir/telegram-qt5/
%_libdir/cmake/TelegramQt5/

%changelog
* Fri Apr 20 2018 Oleg Solovyov <mcpain@altlinux.org> 0.1.0-alt1%ubt
- initial build for ALT

