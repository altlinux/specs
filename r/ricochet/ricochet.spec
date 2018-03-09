Name: ricochet
Version: 1.1.4
Release: alt1

Summary: Anonymous peer-to-peer instant messaging

License: BSD like
Group: Networking/Instant messaging
Url: https://ricochet.im/

# Source-url: https://github.com/ricochet-im/ricochet/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5

BuildRequires: gcc-c++ libstdc++-devel
BuildRequires: libprotobuf-devel libssl-devel protobuf-compiler
BuildRequires: qt5-declarative-devel qt5-multimedia-devel qt5-quick1-devel qt5-tools-devel qt5-translations

Requires: tor

%description
Anonymous metadata-resistant instant messaging that just works.

Ricochet is an experimental kind of instant messaging that
doesn't trust anyone with your identity, your contact list, or your communications.

You can chat without exposing your identity (or IP address) to anyone
Nobody can discover who your contacts are or when you talk (metadata-free!)
There are no servers or operators that could be compromised, exposing your information.
It's cross-platform and easy for non-technical users.

%prep
%setup

%build
%qmake_qt5 DEFINES+=RICOCHET_NO_PORTABLE
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%_bindir/%name
%_desktopdir/%name.desktop
#_datadir/appdata/%name.appdata.xml
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
#_man1dir/*
%doc README.md AUTHORS.md

%changelog
* Fri Mar 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- initial build for ALT Linux Sisyphus
