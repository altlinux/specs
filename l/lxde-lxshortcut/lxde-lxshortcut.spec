%define upstreamname lxshortcut
Name: lxde-%upstreamname
Version: 0.1.2
Release: alt2

Summary: LXShortcut is a small program used to edit application shortcuts created with freedesktop.org Desktop Entry spec.
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Source: %upstreamname-%version.tar.gz

# Automatically added by buildreq on Fri Jul 18 2008
BuildRequires: libvte-devel perl-XML-Parser cvs intltool libgtk+2-devel

%description
%summary

%prep
%setup -n %upstreamname-%version

%build
autoreconf -fisv
%configure
touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README
%_bindir/*
%_datadir/%upstreamname

%changelog
* Mon Jun 11 2012 Radik Usupov <radik@altlinux.org> 0.1.2-alt2
- new upstream snapshot

* Tue Aug 30 2011 Radik Usupov <radik@altlinux.org> 0.1.2-alt1
- new upstream version

* Mon May 03 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.1-alt1
- new upstream version

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
