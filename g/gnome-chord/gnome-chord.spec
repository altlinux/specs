%define oname gnome-guitar_cs

Name: gnome-chord
Version: 0.8.1
Release: alt3

Summary: Chord and scale database

License: GPL3
Group: Video

Url: http://gnome-chord.sourceforge.net/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%oname-%version.tar

Patch: %name-pkglib.patch

BuildPreReq(pre): rpm-build-gnome libGConf-devel

# Automatically added by buildreq on Tue Jul 14 2009
BuildRequires: GConf libgnome-sharp-devel mono-mcs

# (due mono-cairo.pc)
BuildPreReq: mono-devel

%description
Chord and scale database.

%prep
%setup -n %oname-%version
%patch -p2

%build
%autoreconf
%configure --disable-static
%make_build
echo >gconftool
chmod a+rx gconftool

%install
PATH=`pwd`:$PATH %makeinstall_std
%__subst "s|@expanded_libdir@|%_libdir|g" %buildroot%_bindir/*
rm -f %buildroot%_pkgconfigdir/*

%files
%gconf_schemasdir/*.schemas
%_bindir/gnome-chord
%_bindir/gnome-scale
%_libdir/gnome-guitar_cs/
%_desktopdir/*

%changelog
* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt3
- cleanup spec, fix build

* Wed Feb 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt2.1
- rebuild with new mono-2.10

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt2
- update buildreqs

* Mon Jul 13 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Mon Dec 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt2
- rebuild

* Mon May 19 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- initial build for ALT Linux Sisyphus

