%define _unpackaged_files_terminate_build 1

Name: keyd
Version: 2.4.0
Release: alt1.git3421ccaa

Summary: A key remapping daemon for linux.
License: MIT
Group: System/Configuration/Hardware

Url: https://github.com/rvaiya/keyd
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-build-python3

%description
Linux lacks a good key remapping solution. In order to achieve satisfactory
results a medley of tools need to be employed (e.g xcape, xmodmap) with the end
result often being tethered to a specified environment (X11). keyd attempts to
solve this problem by providing a flexible system wide daemon which remaps keys
using kernel level input primitives (evdev, uinput).

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall_std

install -Dm644 keyd.service -t %buildroot%_unitdir/
install -Dm644 keyd.quirks %buildroot%_datadir/libinput/30-keyd.quirks


%pre
/usr/sbin/groupadd -r -f keyd ||:

%files
%_bindir/keyd
%_bindir/keyd-application-mapper
%_datadir/keyd
%_datadir/libinput/30-keyd.quirks
%_unitdir/keyd.service
%_defaultdocdir/keyd
%_man1dir/*

%changelog
* Fri May 13 2022 Egor Ignatov <egori@altlinux.org> 2.4.0-alt1.git3421ccaa
- First build for ALT
