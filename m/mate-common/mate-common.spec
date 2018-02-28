Name: mate-common
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: MATE common build files
License: GPLv3+
Group: Development/Tools
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

%description
Common scripts and macros to develop with MATE

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_datadir/aclocal/*
%_datadir/%name
%_man1dir/*

%changelog
* Wed Feb 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
