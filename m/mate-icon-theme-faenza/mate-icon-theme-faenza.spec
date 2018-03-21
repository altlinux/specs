Name: mate-icon-theme-faenza
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: Extra set of icon themes for MATE Desktop
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: mate-common

%description
Provides a complimentary set of icon themes for MATE Desktop

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
%doc AUTHORS COPYING README NEWS
%_iconsdir/mate*

%changelog
* Wed Mar 21 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
