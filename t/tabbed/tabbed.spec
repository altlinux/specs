Name: tabbed
Version: 0.6
Release: alt1

# http://git.altlinux.org/gears/t/tabbed.git
Source: %name-%version-%release.tar
Url: http://tools.suckless.org/tabbed/
Summary: simple generic tabbed fronted to xembed aware applications
License: MIT
Group: Graphical desktop/Other

BuildRequires: libX11-devel libXft-devel

# needed for SETPROP
Requires: /bin/sed
Requires: /bin/xargs
Requires: /usr/bin/dmenu
Requires: /usr/bin/xprop
Requires: /usr/bin/xwininfo

%description
%summary.

%prep
%setup -n %name-%version-%release

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
* Thu Feb 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6-alt1
- Initial build

