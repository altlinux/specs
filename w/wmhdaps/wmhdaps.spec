# vim: set ft=spec: -*- rpm-spec -*-

Name: wmhdaps
Version: 0.04
Release: alt2

Summary: Harddisk Active Protection System visualization DockApp
Group: Graphical desktop/Window Maker
License: GPL
Url: http://dockapps.org/file.php/id/297

Packager: Sir Raorn <raorn@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Tue Jan 23 2007
BuildRequires: libXext-devel libXpm-devel

%description
The goal of wmhdaps is to provide a tool for configuration of the
Harddisk Active Protection System (HDAPS) found in some R/G/T/X
thinkpad models.  HDAPS is realized as an acceleration sensor mounted
on systemboard and a userspace tool which detects based on
acceleration values from sensor shocks and freezes the harddrive(s)
until the "shock" is over.

%prep
%setup
%patch -p1

%build
pushd wmhdaps
%make_build CFLAGS="%optflags"

%install
mkdir -p %buildroot%_bindir
install -p -m755 wmhdaps/wmhdaps %buildroot%_bindir/%name

%files
%doc README Changelog
%_bindir/%name

%changelog
* Tue Jan 23 2007 Sir Raorn <raorn@altlinux.ru> 0.04-alt2
- Fix model rotaton

* Tue Jan 23 2007 Sir Raorn <raorn@altlinux.ru> 0.04-alt1
- Built for Sisyphus

