Name: openmsx-catapult
Version: 19.1
Release: alt1
Summary: GUI for openMSX
License: GPL-2.0-only
Group: Emulators
Url: https://openmsx.org/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
# PATCH-FIX-OPENSUSE
Patch0: adjust-default-paths.patch
BuildRequires: gcc-c++
BuildRequires: libxml2-devel
BuildRequires: python3
BuildRequires: libwxGTK3.2-devel
Requires: openmsx

ExcludeArch: armh

%description
openMSX Catapult is an optional part (a subproject) of openMSX, the MSX
emulator that aims for perfection. With Catapult you can control openMSX via
a graphical user interface. A release of Catapult is compatible with the
current release of openMSX.

%prep
%setup
%patch0

%build
CFLAGS="%optflags" CXXFLAGS="%optflags" make %{?_smp_mflags}

%install
%make_install install INSTALL_BASE=%buildroot%_libexecdir/openMSX-Catapult
install -d -m 755 %buildroot/usr/bin
ln -sf ../lib/openMSX-Catapult/bin/catapult %buildroot%_bindir/catapult
install -d -m 755 %buildroot%_desktopdir
sed -e "s|%%INSTALL_BASE%%|%_libexecdir/openMSX-Catapult|" desktop/openMSX-Catapult.desktop >%buildroot%_desktopdir/openMSX-Catapult.desktop

%files
%doc README
%_bindir/catapult
%_libexecdir/openMSX-Catapult
%_desktopdir/openMSX-Catapult.desktop

%changelog
* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 19.1-alt1
- update to new version

* Tue May 02 2023 Artyom Bystrov <arbars@altlinux.org> 18.0-alt1
- initial build for ALT Sisyphus

* Fri Jun 24 2022 Wolfgang Bauer <wbauer@tmo.at>
- Update to version 18.0
- Remove call to %%suse_update_desktop_file, no longer needed
* Wed May 26 2021 Wolfgang Bauer <wbauer@tmo.at>
- Update to version 17.0
* Sun Oct 11 2020 Wolfgang Bauer <wbauer@tmo.at>
- initial package - 16.0
- Add adjust-default-paths.patch to match the paths used by the
  openmsx package
