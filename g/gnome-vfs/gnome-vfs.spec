# Defaults

# Avahi supersedes howl.
%def_enable avahi
%def_disable howl

# Choose one
%def_enable openssl
%def_disable gnutls

# Choose one
%def_disable fam
%def_enable gamin

# Optional components
%def_disable hal
%def_enable samba
%def_disable ipv6
%def_disable afs
# This one doesn't work (at all), as for 2.13.4
%def_disable cdda

# Enable gnome-vfs-daemon
%def_enable daemon

%def_disable static
%def_disable gtk_doc
%set_automake_version 1.11

%define ver_major 2.24
%define oldname gnome-vfs2

Name: gnome-vfs
Version: %ver_major.4
Release: alt11
Epoch: 1

Summary: The GNOME virtual file-system libraries
Group: System/Libraries
License: LGPL
Url: ftp://ftp.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
Patch: gnome-vfs-2.24.4-enable-deprecated.patch

Patch2: gnome-vfs-2.24.1-gnutls.patch

Patch3: gnome-vfs-2.9.90-modules-conf.patch

# remove gnome-mime-data dependency
Patch4: gnome-vfs-2.24.1-disable-gnome-mime-data.patch

# CVE-2009-2473 neon, gnome-vfs2 embedded neon: billion laughs DoS attack
# https://bugzilla.redhat.com/show_bug.cgi?id=518215
Patch5: gnome-vfs-2.24.3-CVE-2009-2473.patch

# RH bug #197868
Patch6: gnome-vfs-2.15.91-mailto-command.patch

# (fc) 2.8.2-1mdk handle about: url (Fedora)
Patch8: gnome-vfs-2.8.2-schema_about_for_upstream.patch
# (fc) 2.8.3-5mdk support pamconsole mount option (Fedora)
Patch10: gnome-vfs-2.24.1-console-mount-opt.patch
# (fc) 2.17.91-2mdv replace references to gnomemeeting with ekiga
Patch11: gnome-vfs-2.17.91-fixh323.patch
# (fc) 2.17.91-3mdv allow OnlyShowIn=KDE .desktop to be used when running under KDE (Mdv bug #26999)
Patch12: gnome-vfs-2.17.91-onlyshow.patch
# (fc) 2.18.0.1-2mdv fix crash when fstab is being edited (Ubuntu) (GNOME bug #300547)
Patch13: gnome-vfs-2.20.0-fstab-edit-crash.patch
# (fc) 2.18.0.1-2mdv fix uuid and label mount point duplication (initial idea from Ubuntu bug #57701) (Mdv bug #32792)
Patch14: gnome-vfs-2.20.0-uuid-label-mount.patch
# (fc) 2.18.0.1-2mdv resolve mount point fstab symlinks (Ubuntu)
Patch15: gnome-vfs-2.20.0-resolve-fstab-symlinks.patch
Patch16: gnome-vfs-2.24.4-alt-link.patch

Patch17: 0002-dont-use-smbc_remove_unused_server.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=333041
# https://bugzilla.redhat.com/show_bug.cgi?id=33524
Patch300: gnome-vfs-2.20.0-ignore-certain-mountpoints.patch

# backported from upstream
# gnome-vfs-daemon exits on dbus, and constantly restarted causing dbus/hal to hog CPU
# https://bugzilla.redhat.com/show_bug.cgi?id=486286
Patch404: gnome-vfs-2.24.xx-utf8-mounts.patch

Obsoletes: %oldname-extras < 2.14.2
Provides: %oldname-extras = %version-%release
Obsoletes: %oldname < 2.14.2
Provides: %oldname = %version-%release
Conflicts: libgnome < 2.5.2

# From configure.in
%define dbus_glib_ver 0.60
%define GConf_ver 1.1.1
%define glib_ver 2.9.3
%define libxml2_ver 2.6.0
%define avahi_ver 0.6
%define howl_ver 0.9.6
%define hal_ver 0.5.7
%define gtk_doc_ver 1.0

%define shared_mime_info_ver 0.15

PreReq: GConf >= %GConf_ver
Requires: shared-mime-info >= %shared_mime_info_ver
%{?_enable_gamin:Requires: gamin libgamin-fam}

# From configure.in
BuildPreReq: gnome-common rpm-build-gnome
BuildPreReq: intltool >= 0.35.0
BuildPreReq: GConf >= %GConf_ver libGConf-devel >= %GConf_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: bzlib-devel libkrb5-devel
BuildPreReq: gtk-doc >= %gtk_doc_ver
%{?_enable_cdda:BuildPreReq: libcdparanoia-devel}
%{?_enable_samba:BuildPreReq: libsmbclient-devel}
%{?_enable_openssl:BuildPreReq: libssl-devel}
%{?_enable_gnutls:BuildPreReq: libgnutls-devel >= 1.0.0 libtasn1-devel libgcrypt-devel}
%{?_enable_howl:BuildPreReq: libhowl-devel >= %howl_ver}
%if_enabled avahi
BuildPreReq: libavahi-devel >= %avahi_ver
BuildPreReq: libavahi-glib-devel >= %avahi_ver
%endif
%if_enabled hal
BuildPreReq: libhal-devel >= %hal_ver
%endif
BuildPreReq: libdbus-glib-devel
# For direct inotify support
BuildPreReq: glibc-kernheaders
%{?_enable_fam:BuildPreReq: libfam-devel}
%{?_enable_gamin:BuildPreReq: gamin-devel}
BuildPreReq: openssh-clients gcc-c++  libattr-devel libacl-devel libcom_err-devel zlib-devel perl-XML-Parser

%description
GNOME VFS is the GNOME virtual file system. It is the foundation of the
Nautilus file manager. It provides a modular architecture and ships with
several modules that implement support for file systems, http, ftp and others.
It provides a URI-based API, a backend supporting asynchronous file operations,
a MIME type manipulation library and other features.

%package module-sftp
Summary: SSH/SFTP access module for GNOME VFS.
Group: System/Libraries
Requires: %name = %EVR
Requires: openssh-clients

%description module-sftp
GNOME VFS is the GNOME virtual file system. It is the foundation of the
Nautilus file manager. It provides a modular architecture and ships with
several modules that implement support for file systems, http, ftp and others.
It provides a URI-based API, a backend supporting asynchronous file operations,
a MIME type manipulation library and other features.

This package contains a GNOME VFS module for access to network resources
using SFTP (FTP over SSH) protocol. With this module, you can open URIs
that begin with ssh: and sftp: prefixes.

%package module-smb
Summary: Samba access module for GNOME VFS.
Group: System/Libraries
Requires: %name = %EVR

%description module-smb
GNOME VFS is the GNOME virtual file system. It is the foundation of the
Nautilus file manager. It provides a modular architecture and ships with
several modules that implement support for file systems, http, ftp and others.
It provides a URI-based API, a backend supporting asynchronous file operations,
a MIME type manipulation library and other features.

This package contains a GNOME VFS module for access to network resources
using SMB protocol (also known as "Windows shares"). With this module,
you can open URIs that begin with smb: prefix. Install it if you use
GNOME and there's a Windows machine with shared resources in your
network.

%package devel
Summary: Libraries and include files for developing GNOME VFS applications
Group: Development/GNOME and GTK+
Requires: %name = %EVR
Obsoletes: %oldname-devel < 2.14.2
Provides: %oldname-devel = %version-%release

%description devel
This package provides the necessary development libraries for writing
GNOME VFS modules and applications that use the GNOME VFS APIs.

%package devel-doc
Summary: Development documentation for GNOME VFS.
Group: Development/C
Conflicts: %name-devel < %EVR
Obsoletes: %oldname-devel-doc < 2.14.2
Provides: %oldname-devel-doc = %version-%release
Requires: gtk-doc
BuildArch: noarch

%description devel-doc
GNOME VFS is the GNOME virtual file system. It is the foundation of the
Nautilus file manager. It provides a modular architecture and ships with
several modules that implement support for file systems, http, ftp and others.
It provides a URI-based API, a backend supporting asynchronous file operations,
a MIME type manipulation library and other features.

This package contains development documentation for GNOME VFS.

%if_enabled static
%package devel-static
Summary: Static libraries for developing GNOME VFS applications
Group: Development/GNOME and GTK+
Requires: %name-devel = %EVR
Obsoletes: %oldname-devel-static < 2.14.2
Provides: %oldname-devel-static = %version-%release

%description devel-static
This package provides the necessary static development libraries
for writing GNOME VFS modules and applications that use the GNOME VFS APIs.
%endif

%package utils
Summary: Command line applications for GNOME VFS.
Group: Development/GNOME and GTK+
Requires: %name = %EVR
Obsoletes: %oldname-utils < 2.14.2
Provides: %oldname-utils = %version-%release

%description utils
This package contains command line tools for GNOME VFS.

%define _gtk_docdir %_datadir/gtk-doc/html
%define vfsmodulesdir %_libdir/%name-2.0/modules

%prep
%setup -q
%patch -p1
%patch2 -p1

%patch3 -p1 -b .modules-conf
%patch4 -p1 -b .mime-data
%patch5 -p1 -b .CVE-2009-2473
%patch6 -p1 -b .mailto-command
%patch8 -p1 -b .about
%patch10 -p1 -b .pamconsole
%patch11 -p1 -b .fixh323
%patch12 -p1 -b .onlyshow
%patch13 -p1 -b .fstab-edit-crash
%patch14 -p1 -b .uuid-label-mount
%patch15 -p1 -b .resolve-fstab-symlinks
%patch16 -p1
%patch17 -p1

# send to upstream
%patch300 -p1 -b .ignore-certain-mount-points
%patch404 -p1 -b .utf8-mounts

%build
mkdir -p %buildroot%_datadir/dbus-1/services/
gtkdocize --copy
%autoreconf
export LIBS="$LIBS `%_bindir/libgcrypt-config --libs`"
%configure \
        %{subst_enable static} \
        %{subst_enable howl} \
        %{subst_enable avahi} \
        %{subst_enable hal} \
        %{subst_enable cdda} \
        %{subst_enable samba} \
        --with-samba-includes=$(pkg-config --variable=includedir smbclient) \
        %{subst_enable openssl} \
        %{subst_enable gnutls} \
        %{subst_enable fam} \
        %{?_enable_gamin:--enable-fam} \
        %{subst_enable daemon} \
        --enable-ipv6 \
	--disable-selinux \
        --disable-schemas-install \
        %{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std
subst '/^\(ssh\|sftp\).*$/d' %buildroot%_sysconfdir/%name-2.0/modules/default-modules.conf
cat <<EOF >%buildroot%_sysconfdir/%name-2.0/modules/sftp-module.conf
ssh: sftp
sftp: sftp
EOF
chmod 644 %buildroot%_sysconfdir/%name-2.0/modules/sftp-module.conf

bzip2 -9fk ChangeLog

%find_lang --with-gnome %name-2.0
# system_smb.schemas is not included in this list, because SMB module is
# packaged separately.
%define schemas desktop_default_applications desktop_gnome_url_handlers system_http_proxy system_dns_sd

%post
%gconf2_install %schemas

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %schemas
fi

%post module-smb
%gconf2_install system_smb

%preun module-smb
if [ $1 = 0 ]; then
%gconf2_uninstall system_smb
fi

%files -f %name-2.0.lang
%_libdir/*.so.*
%dir %_libdir/%name-2.0
%dir %vfsmodulesdir
%vfsmodulesdir/libvfs-test.so
%vfsmodulesdir/libcomputer.so
%vfsmodulesdir/libfile.so
%vfsmodulesdir/libtar.so
%vfsmodulesdir/libgzip.so
%vfsmodulesdir/libbzip2.so
%vfsmodulesdir/libnetwork.so
%vfsmodulesdir/libhttp.so
%vfsmodulesdir/libftp.so
%vfsmodulesdir/libdns-sd.so
%vfsmodulesdir/libnntp.so
%_libexecdir/gnome-vfs-daemon
%_datadir/dbus-1/services/gnome-vfs-daemon.service
%dir %_sysconfdir/gnome-vfs-2.0
%dir %_sysconfdir/gnome-vfs-2.0/modules
%config %_sysconfdir/gnome-vfs-2.0/modules/default-modules.conf
%config %_sysconfdir/gnome-vfs-2.0/modules/ssl-modules.conf
%config %gconf_schemasdir/*
%exclude %gconf_schemasdir/system_smb.schemas
%doc AUTHORS ChangeLog.* NEWS README

%files module-sftp
%vfsmodulesdir/libsftp.so
%config %_sysconfdir/gnome-vfs-2.0/modules/sftp-module.conf

%files module-smb
%vfsmodulesdir/libsmb.so
%config %_sysconfdir/gnome-vfs-2.0/modules/smb-module.conf
%config %gconf_schemasdir/system_smb.schemas

%files devel
%_includedir/*
%dir %_libdir/%name-2.0/include
%_libdir/%name-2.0/include/*
%_libdir/*.so
%_pkgconfigdir/*
%doc HACKING TODO

%files devel-doc
%_gtk_docdir/*

%if_enabled static
%files devel-static
%vfsmodulesdir/*.a
%_libdir/*.a
%endif

%files utils
%_bindir/*

%exclude %vfsmodulesdir/*.la

%changelog
* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt11
- disabled doc regeneration

* Mon Dec 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt10
- rebuilt with openssl instead gnutls

* Mon Nov 03 2014 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt9
- fixed build

* Mon Apr 07 2014 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt8
- fixed build with gnome-common-3.12

* Wed Nov 06 2013 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt7
- use automake_1.11

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt6
- fixed build with glib-2.36

* Fri Feb 15 2013 Alexey Shabalin <shaba@altlinux.ru> 1:2.24.4-alt5
- rebuild with new libsmbclient
- don't use the anymore the smbc_remove_unused_server (patch17)

* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt4
- fixed build

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt3
- updated buildreqs

* Fri Dec 17 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt2
- really dropped gnome-mime-data dependence

* Sun Oct 24 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.4-alt1
- 2.24.4

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.24.3-alt2
- fixed CVE-2009-2473
- drop hal and gnome-mime-data dependencies

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.3-alt1
- 2.24.3

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.2-alt1
- 2.24.2
- removed upstreamed gnome-vfs2-smb-bufsize.patch

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 1:2.24.1-alt2
- add patches8-16 from mandriva
- rebuild with latest gnutls

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.24.1-alt1
- 2.24.1

* Wed Jan 07 2009 Alexey Shabalin <shaba@altlinux.ru> 1:2.24.0-alt1.1
- rebuild with gnutls-2.6
- removed obsolete *ldconfig from %%post{,un}

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.24.0-alt1
- 2.24.0
- build devel-doc as noarch

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.22.0-alt1
- 2.22.0

* Tue Mar 04 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.21.90-alt1
- 2.21.90
- fix mailto command for evolution (RH #197868)
- fix a small memory leak (GNOME #427958)
- Don't show /var/log/audit and /var/tmp on the desktop (RH #333041,#335241)
- disabled patch0
- disabled patch1 (use DBUS_SERVICE_DIR as option for make install)

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.20.1-alt1
- 2.20.1

* Thu Oct 11 2007 Igor Zubkov <icesik@altlinux.org> 1:2.20.0-alt1
- 2.18.1 -> 2.20.0

* Wed Oct 10 2007 Alexey Rusakov <ktirf@altlinux.org> 1:2.18.1-alt2
- added Serial in order to fix upgrades from systems with GNOME 1.4

* Wed Jun 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- updated dependencies.
- updated files list, use more macros

* Thu Jan 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt3
- fixed ssh and sftp lines removal in default-modules.conf

* Thu Jan 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt2
- SMB and SSH/SFTP modules have moved to separate subpackages (Bug 10600).

* Mon Dec 25 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version (2.16.3)

* Mon Dec 25 2006 Igor Zubkov <icesik@altlinux.org> 2.16.1-alt1.1
- NMU
- rebuild with new dbus

* Thu Oct 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version 2.16.1 (with rpmrb script)

* Thu Sep 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- updated dependencies; added direct inotify support
- removed last bonobo remains

* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version 2.15.91
- spec updates due to transition from Bonobo to DBus.

* Thu Aug 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version 2.15.90.
- re-enabled building with Samba

* Tue Jun 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt3
- introduced 'samba' switch and temporarily disabled it due to a broken
  libsmbclient.
- minor fixes in dependencies.

* Thu Jun 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt2
- fixed missing Obsoletes/Provides for subpackages.

* Wed May 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version
- removed '2' from the package name.
- spec cleanup

* Mon Mar 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)

* Mon Jan 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt1
- new version
- updated dependencies
- added many new switches, including gnutls (obsoletes openssl), avahi
  (obsoletes howl, Bug #8802) and gamin (obsoletes fam), all three are on by default.

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Tue Nov 01 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt3
- Fixed dependencies of the -devel subpackage.

* Mon Oct 17 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- Added system_storage to the list of installed schemas (thanks to syatskevich@).
- Rewritten schemas wildcard in %%files to be more robust.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sat Oct 01 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt2
- Added fam to the list of requirements.

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt2
- 2.11.92
- Removed excess buildreqs.
- Removed a patch for hal-0.5, as it's been merged into upstream.

* Fri Jul 15 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt2
- adopted for hal-0.5.

* Sun Jun 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1.1
- rebuild against new howl (1.0.0).

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Thu Mar 03 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.93-alt1
- 2.9.93.

* Tue Mar 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92

* Thu Feb 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91
- requires hal if enabled.

* Sat Jan 29 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90

* Mon Jan 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.8.3-alt2
- rebuild with HAL support.
- development documentation moved to devel-doc subpackage.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.3-alt1
- 2.8.3

* Tue Oct 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2
- Howl support enabled.

* Tue Sep 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Sat Aug 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Mon Jul 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1.4
- fix gnomevfs-ls output.

* Mon Jul 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1.3
- subfs support (close #4578).

* Tue May 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1.2
- rebuild with new openssl.

* Mon May 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1.1
- rebuild with new samba.

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1
- 2.6.1.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.8-alt1
- 2.5.8

* Wed Feb 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.7-alt1
-2.5.7

* Sat Jan 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Wed Jan 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt2
- do not package .la files.
- do not build devel-static subpackage by default.

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Tue Jun 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Tue Jun 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Tue May 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2
- utils package.

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Mar 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.4-alt1
- 2.2.4

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Wed Feb 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Mon Feb 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.91-alt1
- 2.1.91

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Mon Dec 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3.1-alt1
- 2.1.3.1

* Wed Nov 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt2
- Removed dependence on mawk.

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sun Sep 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1
- 2.0.4
- some fixes.

* Wed Jun 12 2002 Igor Androsov <blake@altlinux.ru> 2.0.0-alt1
- New version
- Added gconf/schemas/*

* Fri Jun 07 2002 Igor Androsov <blake@altlinux.ru> 1.9.17-alt1
- New Version
- Fix Group (Thanks Yuri Sedunov)

* Tue Jun 04 2002 Igor Androsov <blake@altlinux.ru> 1.9.15-alt2
- Moved *.la from static to devel package

* Tue Jun 04 2002 Igor Androsov <blake@altlinux.ru> 1.9.15-alt1
- Initial build for AltLinux

* Thu May 16 2002 Igor Androsov <blace@mail.ru> 1.9.15-blk0.3
- added to static package .la

* Tue May 14 2002 Igor Androsov <blace@mail.ru> 1.9.15-blk0.2
- Sincing with CVS
- Minor Changes .spec

* Thu May 09 2002 Igor Androsov <blace@mail.ru> 1.9.15-blk0.1
- New version from CVS

* Thu May 09 2002 Igor Androsov <blace@mail.ru> 1.9.14-blk0.1
- New sources from CVS
- Changes for AltLinux
- Static libraries moved to -devel-static

* Sun Dec 15 2001 Ross Golder <ross@golder.org>
- fixed broken Name:

* Sun Oct 21 2001 Gregory Leblanc <gleblanc@linuxweasel.com>
- some messing around with Requires: and BuildRequires
- cleaned up %files quite a bit (still not quite as good as it could be)
- removed a bunch of unnecessary %%defines
