Name: bluez-tools
Version: 0.2.0
Release: alt1.git20161212

Summary: A set of tools to manage Bluetooth devices for Linux
License: GPLv2+
Group: Networking/Other
URL: https://github.com/khvzak/bluez-tools
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar

BuildRequires: glib2-devel libgio-devel libreadline-devel
Requires: bluez

%description
This was a GSoC'10 project to implement a new command line tools for
bluez (Bluetooth stack for Linux).  It is currently an active open
source project.

The project is implemented in C and uses the D-Bus interface of bluez.

The project is still a work in progress, and not all APIs from Bluez
have been implemented as a part of bluez-tools.  The APIs which have
been implemented in bluez-tools are adapter, agent, device, network
and obex.  Other APIs, such as interfaces for medical devices,
pedometers and other specific APIs have not been ported to bluez-tools.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog README
%_bindir/*
%_man1dir/*.1*

%changelog
* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 0.2.0-alt1.git20161212
- Initial build for Sisyphus
