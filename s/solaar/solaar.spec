Name:           solaar
Version:        0.9.2
Release:        alt1.1

Group:          System/Configuration/Hardware
Summary:        Device manager for Logitech Unifying Receiver
URL:            http://pwr.github.io/Solaar/
BuildArch:      noarch
License:        GPLv2

Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires:  python3-module-pyudev

Requires:  	unifying-receiver-udev

# libaptindicator is not package in ALT Linux
%add_typelib_req_skiplist typelib(AppIndicator3)

Source0:        https://github.com/pwr/Solaar/archive/%{version}.tar.gz

%description
Solaar is a device manager for Logitech's Unifying Receiver
peripherals. It is able to pair/unpair devices to the receiver, and
for most devices read battery status.

It comes in two flavors, command-line and GUI. Both are able to list
the devices paired to a Unifying Receiver, show detailed info for each
device, and also pair/unpair supported devices with the receiver.

%package doc
Group:          Documentation
Summary:        Documentation for Solaar
Requires:       %name = %version-%release
BuildArch:      noarch

%description doc
This package provides documentation for Solaar, a device manager for
Logitech's Unifying Receiver peripherals.

%prep
%setup -q -n Solaar-%version

%build
%python3_build

%install
%python3_install

%files
%doc COPYING COPYRIGHT share/README
%_bindir/solaar
%_bindir/solaar-cli
%python3_sitelibdir/*
%_datadir/solaar/
%_desktopdir/solaar.desktop
%_iconsdir/hicolor/scalable/apps/solaar.svg
%config(noreplace) %_sysconfdir/xdg/autostart/solaar.desktop

%files doc
%doc docs

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Build for Sisyphus from Fedora
