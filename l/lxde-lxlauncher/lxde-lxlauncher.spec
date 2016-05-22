%define _unpackaged_files_terminate_build 1
%define origname lxlauncher
%define gtkver 2
Name: lxde-%origname
Version: 0.2.5
Release: alt1

Summary: LXLauncher is an open source clone of Asus launcher for EeePC
License: GPLv2+
Group: Graphical desktop/Other

Url: http://lxde.org
#Url: git://git.lxde.org/lxde/lxterminal.git
Source: %origname-%version.tar
Packager: LXDE Development Team <lxde at packages.altlinux.org>

Requires: lxde-freedesktop-menu
Requires: menu-cache

# Automatically added by buildreq on Wed Sep 24 2014
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libcloog-isl4 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libmenu-cache libpango-devel libstartup-notification libwayland-client libwayland-server libxcb-devel perl-Encode perl-XML-Parser pkg-config xorg-xproto-devel
BuildRequires: intltool libgtk+%gtkver-devel libmenu-cache-devel libstartup-notification-devel

BuildRequires: libfm-devel libxml2-devel
BuildPreReq: rpm-build-xdg

%description
LXLauncher is designed as an open source replacement for the
Asus Launcher included in their EeePC. It is desktop-independent
and follows freedesktop.org specs, so newly added applications will
automatically show up in the launcher, and vice versa for the removed
ones.

LXLauncher is part of LXDE, the Lightweight X11 Desktop Environment.

%prep
%setup -n %origname-%version

%build
%autoreconf
%if %gtkver==3
    %configure --enable-gtk3
%else
    %configure
%endif
%make_build

%install
%makeinstall_std
%find_lang %origname
install -dm755 %buildroot%_datadir/%origname/{backgrounds,icons}

%files -f %origname.lang
%doc AUTHORS README
%_bindir/*
%_man1dir/*
%_xdgconfigdir/menus/*.menu
%dir %_xdgconfigdir/%origname
%config(noreplace) %_xdgconfigdir/%origname/*
%_datadir/desktop-directories/lxde-*.directory
%_datadir/%origname

%changelog
* Sat May 21 2016 Anton Midyukov <antohami@altlinux.org> 0.2.5-alt1
- 0.2.5

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.2.4-alt1
- 0.2.4

* Wed Sep 24 2014 Michael Shigorin <mike@altlinux.org> 0.2.3-alt1
- initial release (based on lxde-lxpanel.spec and fedora package)

