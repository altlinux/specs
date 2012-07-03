%define oname synce-gvfs
%define _libexecdir %_prefix/libexec/gvfs

Name: gvfs-backend-synce
Version: 0.4
Release: alt1
Summary: Synce(Access Windows Mobile device) backend for gvfs
Group: System/Libraries
Packager: Mobile Development Team <mobile@packages.altlinux.org>
License: GPLv2
Url: http://www.synce.org
Source: %oname-%version.alt.tar.bz2

BuildPreReq: intltool >= 0.35.0
BuildPreReq: glib2-devel >= 2.18
BuildPreReq: libgio-devel
BuildPreReq: libdbus-devel
BuildPreReq: librapi-devel >= 0.12
BuildPreReq: gvfs-devel >= 1.0.1-alt3
BuildPreReq: shared-mime-info

%description
This package contains the synce backend for gvfs.
Synce-gvfs is part of the SynCE project. GVFS is the GNOME virtual file
system - an infrastructure for accessing various things as if they were
simply a local filesystem. This GVFS backend lets you access the
contents of Windows Mobile-based mobile devices via GVFS - just browse
to synce:/// in Nautilus or any other GVFS-compliant application.

%prep
%setup -q -n %oname-%version.alt

%build
%autoreconf
%configure --disable-static --disable-update-mime-database
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS ChangeLog COPYING README
%_libexecdir/gvfsd-synce
%_datadir/gvfs/mounts/synce.mount
%_iconsdir/gnome/*/apps/synce-gvfs.png
%_xdgmimedir/packages/*

%changelog
* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4

* Tue Nov 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- 0.3

* Tue Mar 03 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- update to 0.2.2

* Tue Oct 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build for ALTLinux

