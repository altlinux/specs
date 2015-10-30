# vim: set ft=spec: -*- rpm-spec -*-

Name: gnome-pkcs11-eventmgr
Version: 1.0
Release: alt1.qa2

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
* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 1.0-alt1.qa2
- NMU: rebuilt against recent libp11

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0-alt1
- Initial build

