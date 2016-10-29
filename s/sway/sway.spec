Name:		sway
Version:	0.10
Release:	alt1

Summary:	i3wm drop-in replacement for Wayland

Url:		http://swaywm.org/
License:	MIT
Group:		Graphical desktop/Other

Packager:	Vladimir D. Seleznev <vseleznv@altlinux.org>

Source:		%name-%version.tar.gz
Source1:	control
Source2:	README.ALT

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Thu Jul 21 2016
# optimized out: asciidoc cmake-modules docbook-dtds docbook-style-xsl fontconfig glib2-devel libcairo-devel libgdk-pixbuf libgio-devel libgpg-error libinput-devel libjson-c libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-server libwayland-server-devel libxcbutil-icccm libxcbutil-image libxkbcommon-devel pkg-config python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-xml wayland-devel xml-common xsltproc
BuildRequires: asciidoc-a2x cmake libgdk-pixbuf-devel libjson-c-devel libpam-devel libpango-devel libpcre-devel libwayland-cursor-devel libwlc0-devel time
Requires:	%name-data

%package	data
Summary:	i3wm drop-in replacement for Wayland - data files
Group:		Graphical desktop/Other
BuildArch:	noarch

%define common_descr \
Sway is a drop-in replacement for the i3 window manager, but for Wayland \
instead of X11. It works with your existing i3 configuration and \
supports most of i3's features, and a few extras.

%description
%common_descr

%description	data
%common_descr

This package contains data files.

%prep
%setup
cp %SOURCE2 .

%build
%cmake \
	-DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
	-DPCRE_INCLUDE_DIR=%_includedir/pcre \
	#
%cmake_build

%install
%cmakeinstall_std
install -D %SOURCE1 %buildroot%_controldir/%name
# FIXME: swaylock
rm -- %buildroot%_sysconfdir/pam.d/swaylock
rm -- %buildroot%_bindir/swaylock
rm -- %buildroot%_man1dir/swaylock.*

%files
%doc LICENSE
%doc README.md
%doc README.ALT
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/config
%config %_controldir/%name
%_bindir/*
%_man1dir/*
%_man5dir/*
%_datadir/wayland-sessions/sway.desktop

%files data
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sat Oct 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.10-alt1
- 0.10

* Thu Sep 22 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9-alt1
- Initial build

