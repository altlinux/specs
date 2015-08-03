Name: connector-autostart
Version: 0.1
Release: alt1

Summary: autostart connector within desktop session
License: public domain
Group: Networking/Remote access

BuildArch: noarch
BuildRequires: rpm-build-xdg
Requires: connector

%define xdgdir %_xdgconfigdir/autostart

%description
%summary

%prep

%install
mkdir -p %buildroot%xdgdir
cat > %buildroot%xdgdir/connector.desktop << EOF
[Desktop Entry]
Type=Application
Name=Connector
Exec=/usr/bin/connector
EOF

%files
%xdgdir/connector.desktop

%changelog
* Mon Aug 03 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

