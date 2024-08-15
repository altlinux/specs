Name: xmp
Version: 4.2.0
Release: alt1

Summary: Extended Module Player for MOD/S3M/XM/IT/etc
License: GPL-2.0+
Group: Sound

Url: https://github.com/libxmp/xmp-cli
Source: %name-%version.tar

BuildRequires: pkgconfig
BuildRequires: pkgconfig(alsa) >= 1
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(libxmp) >= 4.4

%description
The Extended Module Player is a command-line mod player for Unix-like
systems that plays over 90 mainstream and obscure module formats from
Amiga, Atari, Acorn, Apple IIgs, C64, and PC, including Protracker
(MOD), Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse
Tracker (IT) files.

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING README
%dir %_sysconfdir/xmp/
%config(noreplace) %_sysconfdir/xmp/*.conf
%_bindir/xmp
%_man1dir/xmp.1*

%changelog
* Thu Dec 28 2023 Artem Kurashov <saahriktu@altlinux.org> 4.2.0-alt1
- New version (4.2.0).
- .spec cleanup.

* Tue May 23 2023 Artem Kurashov <saahriktu@altlinux.org> 4.1.0-alt2
- Fix Autoimports/Sisyphus versions conflict.

* Fri May 05 2023 Artem Kurashov <saahriktu@altlinux.org> 4.1.0-alt1
- Initial package.
