Name: tabbed
Version: 0.7
Release: alt2

# http://git.altlinux.org/gears/t/tabbed.git
Source: %name-%version.tar
Url: http://tools.suckless.org/tabbed/
Summary: simple generic tabbed fronted to xembed aware applications
License: MIT
Group: Graphical desktop/Other
Patch1: 0001-tabbed-prints-the-position-number-of-the-client-befo.patch
Patch2: 0002-hides-the-tab-bar-if-only-one-tab-is-open.patch
Patch3: 0003-Support-dragging-tabs-left-and-right-with-the-mouse.patch
Patch4: 0004-interpret-nonexistent-large-position-numbers-as-the-.patch
Patch5: 0005-Introduce-runtime-font-selection.patch
BuildRequires: libXft-devel

# needed for SETPROP
Requires: sed
Requires: dmenu
Requires: xprop
Requires: xwininfo
Requires: /usr/bin/xargs

%description
Simple generic tabbed frontend to xembed-aware applications, originally
designed for surf but also usable with many other applications, i.e. st,
uzbl, urxvt and xterm

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
sed -i /^CFLAGS/s/$/\ "%optflags"/ config.mk
make

%install
make \
	DESTDIR=%buildroot \
	PREFIX=%_prefix \
	MANPREFIX=%_mandir \
	install

%files
%doc LICENSE
%doc README.ALT
%_bindir/*
%_man1dir/*

%changelog
* Wed May 10 2023 Fr. Br. George <george@altlinux.org> 0.7-alt2
- Actualize README.ALT

* Thu May 04 2023 Fr. Br. George <george@altlinux.org> 0.7-alt1
- Version up
- Update patchset

* Thu Feb 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6-alt1
- Initial build

