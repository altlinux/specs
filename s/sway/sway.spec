Name:		sway
Version:	0.12
Release:	alt2

Summary:	i3wm drop-in replacement for Wayland

Url:		http://swaywm.org/
License:	MIT
Group:		Graphical desktop/Other

Packager:	Vladimir D. Seleznev <vseleznv@altlinux.org>

Source:		%name-%version.tar.gz
Source1:	README.ALT
Source2:	pam

PreReq:		/etc/tcb
BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Tue Feb 28 2017
# optimized out: asciidoc cmake-modules docbook-dtds docbook-style-xsl fontconfig glib2-devel libcairo-devel libgdk-pixbuf libgio-devel libgpg-error libinput-devel libjson-c libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-server libwayland-server-devel libxcbutil-image libxkbcommon-devel pkg-config python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-xml wayland-devel xml-common xsltproc
BuildRequires: asciidoc-a2x cmake libcap-devel libgdk-pixbuf-devel libjson-c-devel libpam-devel libpango-devel libpcre-devel libwayland-cursor-devel libwayland-egl-devel libwlc0-devel time
Requires:	%name-data
Requires(post):	/sbin/setcap

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
cp %SOURCE1 .
cp %SOURCE2 .

%build
%cmake \
	-DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
	-DPCRE_INCLUDE_DIR=%_includedir/pcre \
	#
%cmake_build

%install
%cmakeinstall_std
install -pm2640 -D pam %buildroot%_sysconfdir/pam.d/swaylock

%post
/sbin/setcap cap_sys_ptrace=eip %_bindir/%name

%files
%doc LICENSE
%doc README.md
%doc README.ALT
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/security.d
%attr(0640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/swaylock
%config(noreplace) %_sysconfdir/%name/config
%config(noreplace) %_sysconfdir/%name/security.d/00-defaults
%_bindir/sway
%attr(2711,root,chkpwd) %_bindir/swaylock
%_bindir/swaybar
%_bindir/swaybg
%_bindir/swaygrab
%_bindir/swaymsg
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_datadir/wayland-sessions/sway.desktop

%files data
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Wed Mar 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12-alt2
- added swaylock.
- fixed post requires type.
- removed control file.

* Sat Mar 11 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12-alt1
- 0.12
- fixed: set CAP_SYS_PTRACE to sway binary
- upstream changes:
 + %%_sysconfdir/%%name/security config is no longer used by sway
 + added security configs dir: %%_sysconfdir/%%name/security.d

* Tue Feb 28 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.11-alt1
- 0.11
- fixed: system configs are noreplace now

* Sat Oct 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.10-alt1
- 0.10

* Thu Sep 22 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9-alt1
- Initial build

