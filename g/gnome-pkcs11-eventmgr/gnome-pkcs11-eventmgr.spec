# vim: set ft=spec: -*- rpm-spec -*-

Name: gnome-pkcs11-eventmgr
Version: 1.0
Release: alt1

Summary: Simple PKCS#11 event manager for GNOME
Group: Graphical desktop/GNOME
License: GPL

Source: %name-%version.tar

# Automatically added by buildreq on Wed Sep 09 2009
BuildRequires: libGConf-devel libdbus-glib-devel libgtk+2-devel libp11-devel

%description
Simple PKCS#11 event manager for GNOME.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*

%changelog
* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0-alt1
- Initial build

