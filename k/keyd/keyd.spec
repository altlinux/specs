%define _unpackaged_files_terminate_build 1

Name: keyd
Version: 2.5.0
Release: alt1

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
%make_build PREFIX=%prefix

%install
%makeinstall_std PREFIX=%prefix

install -Dm644 keyd.service -t %buildroot%_unitdir/

%pre
/usr/sbin/groupadd -r -f keyd ||:

%files
%_bindir/keyd
%_bindir/keyd-application-mapper
%_datadir/keyd
%_unitdir/keyd.service
%_defaultdocdir/keyd
%_man1dir/*

%changelog
* Wed Oct 09 2024 Andrey Kovalev <ded@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Wed May 24 2023 Egor Ignatov <egori@altlinux.org> 2.4.3-alt1
- new version 2.4.3

* Tue Jul 26 2022 Egor Ignatov <egori@altlinux.org> 2.4.2-alt1
- new version 2.4.2

* Mon Jun 20 2022 Egor Ignatov <egori@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Fri May 13 2022 Egor Ignatov <egori@altlinux.org> 2.4.0-alt1.git3421ccaa
- First build for ALT
