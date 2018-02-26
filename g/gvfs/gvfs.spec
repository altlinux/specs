%define ver_major 1.12
%def_enable http
%def_enable avahi
%def_enable cdda
%def_enable fuse
%def_disable hal
%def_enable obexftp
%def_enable gphoto2
%def_enable keyring
%def_enable samba
%def_enable archive
%def_disable gdu
%def_enable afc
%def_enable afp
%def_enable udisks2
%def_enable bluray
%def_disable gtk_doc

Name: gvfs
Version: %ver_major.3
Release: alt1

Summary: The GNOME virtual filesystem libraries
License: %lgpl2plus
Group: System/Libraries
URL: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch: gvfs-1.11.3-alt-gettext.patch
Patch1: gvfs-1.0.1-archive-integration.patch
Patch3: gvfs-1.6.2-libgvfsdaemon+headers_install.patch

%{?_enable_gdu:Obsoletes: gnome-mount <= 0.8}
%{?_enable_gdu:Obsoletes: gnome-mount-nautilus-properties <= 0.8}

# From configure.in
%define intltool_ver 0.35.0
%define glib_ver 2.31.0
%define libsoup_ver 2.26.0
%define avahi_ver 0.6
%define libcdio_paranoia_ver 0.78.2
%define hal_ver 0.5.10
%define bluez_ver 4.0
%define gdu_ver 3.3.91

%{?_enable_hal:Requires: gnome-mount}
%{?_enable_gdu:Requires: gnome-disk-utility >= %gdu_ver}
%{?_enable_udisks2:Requires: udisks2}

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.in
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: gtk-doc
BuildPreReq: openssh-clients
# hotplug backend
BuildRequires: libgudev-devel
# required if autoreconf used
BuildRequires: libgcrypt-devel
%{?_enable_http:BuildPreReq: libsoup-gnome-devel >= %libsoup_ver libxml2-devel}
%{?_enable_avahi:BuildPreReq: libavahi-glib-devel >= %avahi_ver libavahi-devel >= %avahi_ver}
%{?_enable_cdda:BuildPreReq: libcdio-devel >= %libcdio_paranoia_ver}
%{?_enable_fuse:BuildPreReq: libfuse-devel}
%{?_enable_hal:BuildPreReq: libhal-devel >= %hal_ver}
%{?_enable_obexftp:BuildPreReq: libbluez-devel >= %bluez_ver libdbus-glib-devel libexpat-devel}
%{?_enable_gphoto2:BuildPreReq: libgphoto2-devel}
%{?_enable_keyring:BuildPreReq: libgnome-keyring-devel}
%{?_enable_samba:BuildPreReq: libsmbclient-devel}
%{?_enable_archive:BuildPreReq: libarchive-devel}
%{?_enable_gdu:BuildPreReq: libgdu-devel >= %gdu_ver libgudev-devel}
%{?_enable_afc:BuildPreReq: libimobiledevice-devel >= 1.1.3}
%{?_enable_afp:BuildPreReq: libgcrypt-devel}
%{?_enable_udisks2:BuildPreReq: libudisks2-devel}
%{?_enable_bluray:BuildPreReq: libbluray-devel}

BuildPreReq: desktop-file-utils
BuildRequires: gcc-c++ perl-XML-Parser

%package devel
Summary: Libraries and include files for developing gvfs applications
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%package -n fuse-gvfs
Summary: gvfs fuse gateway
Group: System/Kernel and hardware
Requires: %name = %version-%release
Requires: %{get_dep fuse}

%package backend-smb
Summary: Samba backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-obexftp
Summary: Obexftp backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-dnssd
Summary: Dnssd(avahi) backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-cdda
Summary: Music CD-ROM backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-afc
Summary: i{Phone,Pod} backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-afp
Summary: Apple Filing Protocol backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backends
Summary: All backends for gvfs
Group: System/Libraries
BuildArch: noarch
Requires: gvfs gvfs-backend-smb gvfs-backend-dnssd
%{?_enable_cdda:Requires: gvfs-backend-cdda}
%{?_enable_obexftp:Requires: gvfs-backend-obexftp}
%{?_enable_afc:Requires: gvfs-backend-afc}
%{?_enable_afp:Requires: gvfs-backend-afp}

%package utils
Summary: Command line applications for gvfs.
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%package -n bash-completion-gvfs
Summary: Bash completion for gvfs utils
Group: Development/Other
BuildArch: noarch
Requires: bash-completion
Requires: gvfs-utils

%description
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via dbus. It also contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It also
supports exposing the gvfs mounts to non-gio applications using fuse.

This package contains the gvfs server,libgvfscommon library, gio modules and
backends for gvfs: archive, burn, computer, dav, ftp,
gphoto2, http, localtest, network, sftp and trash.

%description devel
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via dbus. It also contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It also
supports exposing the gvfs mounts to non-gio applications using fuse.

This package contains the libgvfscommon development files.

%description -n fuse-gvfs
fuse-gvfs is a bridge between the gvfs filesystem design and fuse, a
program to mount user-space filesystems.

%description backend-smb
This package contains the smb and smb-browse backends for gvfs.

%description backend-obexftp
This package contains the obexftp backend for gvfs.

%description backend-dnssd
This package contains the dnssd backend for gvfs.

%description backend-cdda
This package contains the cdda backend for gvfs.

%description backend-afc
This package contains a backend for gvfs, providing access to Apple's
iPhone, and iPod Touch devices.

%description backend-afp
This package contains a backend for gvfs, providing access to Apple
Mac OS X filesystem by AFP (Apple Filing Protocol) network protocol.


%description backends
This virtual package contains the all backends for gvfs.

%description utils
This package contains command line tools for gvfs.

%description -n bash-completion-gvfs
Bash completion for gvfs.


%define _libexecdir %_prefix/libexec/%name

%prep
%setup
%patch -p1
%patch1 -p1 -b .archive-integration
%patch3 -p1 -b .headers-install

%build
%autoreconf
%configure \
        %{subst_enable http} \
        %{subst_enable avahi} \
        %{subst_enable cdda} \
        %{subst_enable fuse} \
        %{subst_enable hal} \
        %{subst_enable obexftp} \
        %{subst_enable gphoto2} \
        %{subst_enable keyring} \
        %{subst_enable samba} \
        %{subst_enable archive} \
        %{subst_enable afc} \
        %{subst_enable afp} \
        %{subst_enable gdu} \
        %{subst_enable udisks2} \
        %{subst_enable bluray} \
        %{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

mkdir -p %buildroot%_sysconfdir/bash_completion.d/
mv -f %buildroot%_sysconfdir/profile.d/gvfs-bash-completion.sh %buildroot%_sysconfdir/bash_completion.d/%name

%check
%make check

%post
killall -USR1 gvfsd >&/dev/null || :

%files -f %name.lang
%doc AUTHORS NEWS README monitor/udisks2/what-is-shown.txt
# lib
%_libdir/libgvfs*.so.*
%dir %_libexecdir
# daemon
%_libexecdir/gvfsd
%config %_datadir/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
# monitors
%_libexecdir/gvfs-gphoto2-volume-monitor
%{?_enable_hal:%_libexecdir/gvfs-hal-volume-monitor}
%{?_enable_gdu:%_libexecdir/gvfs-gdu-volume-monitor}
%{?_enable_udisks2:%_libexecdir/gvfs-udisks2-volume-monitor}

%_datadir/dbus-1/services/*
# gio modules
%_libdir/gio/modules/*.so
# default backends
%_libexecdir/gvfsd-*

%dir %_datadir/%name
%dir %_datadir/%name/remote-volume-monitors
%_datadir/%name/remote-volume-monitors/gphoto2.monitor
%{?_enable_hal:%_datadir/%name/remote-volume-monitors/hal.monitor}
%{?_enable_gdu:%_datadir/%name/remote-volume-monitors/gdu.monitor}
%{?_enable_udisks2:%_datadir/%name/remote-volume-monitors/udisks2.monitor}
%_datadir/%name/mounts
%_datadir/applications/mount-archive.desktop

# in another packages
%if_enabled samba
    %exclude %_libexecdir/gvfsd-smb
    %exclude %_libexecdir/gvfsd-smb-browse
    %exclude %_datadir/%name/mounts/smb.mount
    %exclude %_datadir/%name/mounts/smb-browse.mount
%endif

%{?_enable_cdda:%exclude %_libexecdir/gvfsd-cdda}

%if_enabled obexftp
    %exclude %_libexecdir/gvfsd-obexftp
    %exclude %_datadir/%name/mounts/obexftp.mount
%endif

%if_enabled afc
    %exclude %_libexecdir/gvfsd-afc
    %exclude %_datadir/%name/mounts/afc.mount
%endif

%if_enabled afp
    %exclude %_libexecdir/gvfsd-afp
    %exclude %_libexecdir/gvfsd-afp-browse
    %exclude %_datadir/%name/mounts/afp.mount
    %exclude %_datadir/%name/mounts/afp-browse.mount
%endif

%{?_enable_cdda:%exclude %_datadir/%name/mounts/cdda.mount}
    %exclude %_libexecdir/gvfsd-dnssd
    %exclude %_datadir/%name/mounts/dns-sd.mount

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
#%%_datadir/gtk-doc/html/*

%files -n fuse-gvfs
%_libexecdir/gvfs-fuse-daemon

%files backend-smb
%_libexecdir/gvfsd-smb
%_libexecdir/gvfsd-smb-browse
%_datadir/%name/mounts/smb.mount
%_datadir/%name/mounts/smb-browse.mount
%config %_datadir/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
%_datadir/GConf/gsettings/gvfs-smb.convert

%if_enabled obexftp
%files backend-obexftp
%_libexecdir/gvfsd-obexftp
%_datadir/%name/mounts/obexftp.mount
%endif

%files backend-dnssd
%_libexecdir/gvfsd-dnssd
%_datadir/%name/mounts/dns-sd.mount
%config %_datadir/glib-2.0/schemas/org.gnome.system.dns_sd.gschema.xml
%_datadir/GConf/gsettings/gvfs-dns-sd.convert

%if_enabled cdda
%files backend-cdda
%_libexecdir/gvfsd-cdda
%_datadir/%name/mounts/cdda.mount
%endif

%if_enabled afc
%files backend-afc
%_libexecdir/gvfsd-afc
%_libexecdir/gvfs-afc-volume-monitor
%_datadir/%name/mounts/afc.mount
%_datadir/%name/remote-volume-monitors/afc.monitor
%endif

%if_enabled afp
%files backend-afp
%_libexecdir/gvfsd-afp
%_libexecdir/gvfsd-afp-browse
%_datadir/%name/mounts/afp.mount
%_datadir/%name/mounts/afp-browse.mount
%endif

%files backends

%files utils
%_bindir/*

%files -n bash-completion-gvfs
%_sysconfdir/bash_completion.d/%name

%exclude %_libdir/gio/modules/*.la

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3 release

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt0.1
- 1.12.3 snapshot (01161473e)

* Wed May 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt2
- rebuild against libimobiledevice-1.1.3
- fixed build of afp backend

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Sep 06 2011 Yuri N. Sedunov <aris@altlinux.org> 1.9.5-alt1
- 1.9.5
- new -backend-afp subpackage

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7
- remove upstreamed patches

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt3
- fixed build against newer libgio
- fixed GNOME bug #633330

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt2
- libbluez4-devel/libbluez-devel

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2
- AFC backend temporarily disabled (not ready for libiphone-0.9.6)

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Thu Dec 03 2009 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1
- new afc backend

* Mon Nov 30 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2
- removed upstreamed patches

* Wed Nov 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt3
- obsoletes gnome-mount{,-nautilus-properties} if enabled gdu
- some upstream patches

* Thu Nov 05 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt2
- rebuild against new libcdio

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- g-d-u support disabled for Sisyphus

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5

* Thu Aug 20 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt2
- g-d-u support enabled

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- 1.3.4
- updated buildreqs

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Apr 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- removed strange dependency on glib2-devel

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Apr 02 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Mar 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Feb 04 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5
- removed upstreamed patch
- enabled obexftp plugin

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4
- updated buildreqs
- temporarily disabled obexftp plugin, requires bluez >= 4.0

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3
- remove obsolete %%post{,un} scripts

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Oct 14 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt3
- remove support synce
- install common, daemon headers. build libgvfsdaemon.so (patch3)

* Mon Oct 13 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt2
- add synce-gvfs-0.1 backend as patch2 from http://sourceforge.net/projects/synce/

* Sat Sep 27 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- new version
- removed gvfs-ftp-read-directory-2.patch and
  gvfs-0.2.4-trash-automount.patch (fixed in upstream)
- updated archive-integration.patch
- updated buildreqs
- updated %%files
- don't rebuild documentation

* Thu Jun 26 2008 Alexey Shabalin <shaba@altlinux.ru> 0.99.1-alt1
- 0.99.1
- enable archive integration (patch1)
- fix GNOME bugs #522933, #525779 (patch2, patch3)
- add update_desktopdb in post-scripts

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Wed Apr 09 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3
- changed libexec dir to %_prefix/libexec/%name

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt2
- fix exclude files (change libdir to libexecdir)

* Thu Mar 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- 0.2.1
- split the package into backends, utils
- move gvfs-bash-completion.sh from /etc/profile.d to /etc/bash_completion.d/,
  and individual package. (#15068)

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt2
- add require gnome-mount

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt1.1
- remove require gnome-mount

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt1
- redesigned spec

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt0.2
- update BuildRequires

* Thu Mar 13 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.2.0.1-alt0.1
- 0.2.0.1
- requires improvement

* Wed Mar 12 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.2.0-alt0.1
- 0.2.0
