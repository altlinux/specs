Name: xiccd
Version: 0.2.2
Release: alt1

Summary: X color profile daemon
License: %gpl3plus
Group: Graphics

URL: https://github.com/agalakhov/xiccd
# https://github.com/agalakhov/xiccd.git
Source: %name-%version.tar
Source1: xiccd.desktop
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libX11-devel libXrandr-devel glib2-devel libcolord-devel

Requires: colord

%description
xiccd is a simple bridge between colord and X.
It does the following tasks:
 * Enumerates displays and register them in colord;
 * Creates default ICC profiles based on EDID data;
 * Applies ICC profiles provided by colord;
 * Maintains user's private ICC storage directory.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/xdg/autostart/xiccd.desktop

%files
%config(noreplace) %_sysconfdir/xdg/autostart/*.desktop
%_bindir/%name

%changelog
* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Initial build.

