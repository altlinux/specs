Name: pixiewps
Version: 1.4.2
Release: alt1
Summary: WiFi WPS security audit tool
Group: Security/Networking
License: GPLv3
URL: https://github.com/wiire/pixiewps
Source: %name-%version.tar.gz
Conflicts: NetworkManager
Packager: Gremlin from Kremlin <gremlin@altlinux.org>

# Most build environments safely override this
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
%summary

%prep
%setup

%build
%make_build

%install
umask 022
mkdir -p %buildroot/%_bindir %buildroot%_man1dir
install -m 0755 %name %buildroot/%_bindir/
install -m 0644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Jan 08 2018 Gremlin from Kremlin <gremlin@altlinux.org> 1.4.2-alt1
- updated to 1.4.2

* Fri Sep 01 2017 Gremlin from Kremlin <gremlin@altlinux.org> 1.2.3-alt2
- Conflicts: NetworkManager

* Thu Aug 31 2017 Gremlin from Kremlin <gremlin@altlinux.org> 1.2.3-alt1
- initial build
