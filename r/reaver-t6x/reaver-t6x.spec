%define toolname reaver

Name: %toolname-t6x
Version: 1.6.3
Release: alt1
Summary: WiFi WPS security audit tool
Group: Security/Networking
License: GPLv2
URL: https://github.com/t6x/reaver-wps-fork-t6x
Source: %name-%version.tar.gz
Requires: libpcap
BuildRequires: libpcap-devel
Provides: %toolname = %version, wash = %version
Obsoletes: %toolname < 1.6
Conflicts: systemd NetworkManager

# Most build environments safely override this
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
%summary

%prep
%setup

%build
cd src
%configure
%make_build

%install
umask 022
mkdir -p %buildroot/%_bindir %buildroot%_man1dir
gzip -cd < docs/%toolname.1.gz > %buildroot%_man1dir/%toolname.1
install -m 0755 src/%toolname src/wash %buildroot/%_bindir/

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Dec 28 2017 Gremlin from Kremlin <gremlin@altlinux.org> 1.6.3-alt1
- updated to 1.6.3
- Conflicts: systemd NetworkManager

* Thu Aug 31 2017 Gremlin from Kremlin <gremlin@altlinux.org> 1.6.1-alt1
- initial build (replaces "classic" reaver)
