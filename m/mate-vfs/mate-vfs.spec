# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/krb5-config /usr/bin/mateconftool-2 /usr/bin/perl5 /usr/bin/ssh bzlib-devel libattr-devel libgamin-devel libgcrypt-devel libgnutls-devel perl(diagnostics.pm) pkgconfig(avahi-client) pkgconfig(glib-2.0) pkgconfig(gmodule-no-export-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(hal) pkgconfig(mate-mime-data-2.0) zlib-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
%global po_package mate-vfs-2.0

Summary:			The MATE virtual file-system libraries
Name:				mate-vfs
Version:			1.4.0
Release:			alt3_14
License:			LGPLv2+ and GPLv2+
					# the daemon and the library are LGPLv2+
					# the modules are LGPLv2+ and GPLv2+
Group:				System/Libraries
Source0:			http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
URL:				http://mate-desktop.org


BuildRequires:		mate-conf-devel
BuildRequires:		bzip2-devel
BuildRequires:		libsmbclient-devel
BuildRequires:		libssl-devel
BuildRequires:		gamin-devel
BuildRequires:		libkrb5-devel
BuildRequires:		libavahi-glib-devel
BuildRequires:		libdbus-glib-devel
BuildRequires:		libacl-devel
BuildRequires:		libselinux-devel
BuildRequires:		libkeyutils-devel
BuildRequires:		mate-mime-data-devel
BuildRequires:		mate-common
BuildRequires:		libxml2-devel


Requires(post):		mate-conf
Requires(pre):		mate-conf
Requires(preun):	mate-conf

# For gvfs-open
Requires:	gvfs

Patch0:		mate-vfs-1.4.0-modules-conf.patch

# Default
Patch1:		mate-vfs-1.4.0-browser_default.patch

# RH bug #197868
Patch2:		mate-vfs-1.4.0-mailto-command.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=333041
# https://bugzilla.redhat.com/show_bug.cgi?id=335241
Patch3:		mate-vfs-1.4.0-ignore-certain-mountpoints.patch

# gnome-vfs-daemon exits on dbus, and constantly restarted causing dbus/hal to hog CPU
# https://bugzilla.redhat.com/show_bug.cgi?id=486286
Patch4:		mate-vfs-1.4.0-utf8-mounts.patch
Source44: import.info
Patch33: mate-vfs-1.4.0-alt-link.patch
Requires: gvfs-backends
Patch34: gnome-vfs-2.17.91-fixh323.patch
Patch35: gnome-vfs-2.17.91-onlyshow.patch
Patch36: gnome-vfs-2.20.0-fstab-edit-crash.patch
Patch37: gnome-vfs-2.20.0-resolve-fstab-symlinks.patch
Patch38: gnome-vfs-2.20.0-uuid-label-mount.patch
Patch39: gnome-vfs-2.24.1-console-mount-opt.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=435653
Patch40: 0001-Add-default-media-application-schema.patch
Patch41: gnome-vfs-2.8.2-schema_about_for_upstream.patch
# remove gnome-mime-data dependency
Patch42: gnome-vfs-2.24.1-disable-gnome-mime-data.patch
# CVE-2009-2473 neon, gnome-vfs2 embedded neon: billion laughs DoS attack
# https://bugzilla.redhat.com/show_bug.cgi?id=518215
Patch43: gnome-vfs-2.24.3-CVE-2009-2473.patch

%description
MATE VFS is the MATE virtual file system. It is the foundation of
the Caja file manager. It provides a modular architecture and
ships with several modules that implement support for file systems,
http, ftp, and others. It provides a URI-based API, back end
supporting asynchronous file operations, a MIME type manipulation
library, and other features.

%package devel
Summary: Libraries and include files for developing MATE VFS applications
Group: Development/C
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for writing
MATE VFS modules and applications that use the MATE VFS APIs.

%package smb
Summary: Windows file share support for mate-vfs
Group: System/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires: gvfs-backend-smb

%description smb
This package provides support for reading and writing files on windows
shares (SMB) to applications using MATE VFS.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .modules-conf
%patch1 -p1 -b .mailto-command
%patch2 -p1 -b .browser_default
%patch3 -p1 -b .ignore-certain-mount-points
%patch4 -p1 -b .utf8-mounts

%patch33 -p1
NOCONFIGURE=1 ./autogen.sh
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1

%build
if pkg-config openssl ; then
	CPPFLAGS=`pkg-config --cflags openssl`; export CPPFLAGS
	LDFLAGS=`pkg-config --libs-only-L openssl`; export LDFLAGS
fi

export CPPFLAGS="-I/usr/include/cdda"

%configure \
	--enable-daemon \
	--disable-static \
        --with-samba-includes=$(pkg-config --variable=includedir smbclient)


sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new && \
touch -r AUTHORS AUTHORS.new && \
mv AUTHORS.new AUTHORS

make %{?_smp_mflags}


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}


%post
%mateconf_schema_upgrade system_http_proxy system_dns_sd system_smb desktop_mate_url_handlers desktop_default_applications

%pre
%mateconf_schema_prepare system_http_proxy system_dns_sd system_smb desktop_mate_url_handlers desktop_default_applications

%preun
%mateconf_schema_remove system_http_proxy system_dns_sd system_smb desktop_mate_url_handlers desktop_default_applications

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.LIB NEWS README
%dir %{_sysconfdir}/mate-vfs-2.0
%dir %{_sysconfdir}/mate-vfs-2.0/modules
%config(noreplace) %{_sysconfdir}/mate-vfs-2.0/modules/*.conf
%exclude %{_sysconfdir}/mate-vfs-2.0/modules/smb-module.conf
%{_bindir}/*
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_libdir}/*.so.*
%exclude %{_libdir}/mate-vfs-2.0/modules/libsmb.so
# these .so-files are plugins for mate-vfs
%{_libdir}/mate-vfs-2.0/modules
%dir %{_libdir}/mate-vfs-2.0
%config(noreplace) %{_sysconfdir}/mateconf/schemas/*
%{_datadir}/dbus-1/services/mate-vfs-daemon.service

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/mate-vfs-2.0/include
%{_includedir}/*
%{_datadir}/gtk-doc/html/mate-vfs-2.0/*

%files smb
%{_libdir}/mate-vfs-2.0/modules/libsmb.so
%config(noreplace) %{_sysconfdir}/mate-vfs-2.0/modules/smb-module.conf

%changelog
* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_14
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3_1.1
- Build for Sisyphus

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- adapted alt patches

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- added gvfs-backend dependencies

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- converted by srpmconvert script

