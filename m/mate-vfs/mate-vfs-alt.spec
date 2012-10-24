# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/krb5-config /usr/bin/mateconftool-2 /usr/bin/perl5 /usr/bin/ssh bzlib-devel libattr-devel libgamin-devel libgcrypt-devel libgnutls-devel perl(diagnostics.pm) pkgconfig(avahi-client) pkgconfig(hal) pkgconfig(mate-mime-data-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define fedora 18
%define po_package mate-vfs-2.0

# don't use HAL from F-16 on
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%bcond_with hal
%else
%bcond_without hal
%endif

Summary: 	The MATE virtual file-system libraries
Name: 		mate-vfs
Version: 	1.4.0
Release: 	alt3_1.1
License: 	LGPLv2+ and GPLv2+
		# the daemon and the library are LGPLv2+
		# the modules are LGPLv2+ and GPLv2+
Group: 		System/Libraries
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
URL: 		http://mate-desktop.org
Requires(post): mate-conf
Requires(pre):  mate-conf
Requires(preun): mate-conf
BuildRequires: mate-conf-devel
BuildRequires: libxml2-devel zlib-devel
BuildRequires: glib2-devel
BuildRequires: popt bzip2-devel mate-corba-devel openjade
BuildRequires: automake
BuildRequires: libtool
BuildRequires: intltool
BuildRequires: autoconf
BuildRequires: gtk-doc
BuildRequires: perl-XML-Parser
BuildRequires: libsmbclient-devel
BuildRequires: libssl-devel gamin-devel
BuildRequires: libkrb5-devel
BuildRequires: libavahi-glib-devel
%if %{with hal}
BuildRequires: hal-devel
%endif
BuildRequires: libdbus-devel
BuildRequires: libdbus-glib-devel
BuildRequires: gettext
BuildRequires: libacl-devel
BuildRequires: libselinux-devel
BuildRequires: libkeyutils-devel
BuildRequires: cdparanoia-devel
BuildRequires: mate-common

# For gvfs-open
Requires: gvfs

Patch3: gnome-vfs-2.9.90-modules-conf.patch

# remove gnome-mime-data dependency
Patch4: gnome-vfs-2.24.1-disable-gnome-mime-data.patch

# CVE-2009-2473 neon, gnome-vfs2 embedded neon: billion laughs DoS attack
# https://bugzilla.redhat.com/show_bug.cgi?id=518215
Patch5: gnome-vfs-2.24.3-CVE-2009-2473.patch

# send to upstream
Patch101:	gnome-vfs-2.8.2-schema_about_for_upstream.patch

# Default
Patch104:	gnome-vfs-2.8.2-browser_default.patch

# Applied upstream.
# Patch201: gnome-vfs-2.8.1-console-mount-opt.patch

# RH bug #197868
Patch6: gnome-vfs-2.15.91-mailto-command.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=333041
# https://bugzilla.redhat.com/show_bug.cgi?id=335241
Patch300: gnome-vfs-2.20.0-ignore-certain-mountpoints.patch


# backported from upstream

# gnome-vfs-daemon exits on dbus, and constantly restarted causing dbus/hal to hog CPU
# https://bugzilla.redhat.com/show_bug.cgi?id=486286
Patch404: gnome-vfs-2.24.xx-utf8-mounts.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=435653
Patch405: 0001-Add-default-media-application-schema.patch
Patch33: mate-vfs-1.4.0-alt-link.patch
Requires: gvfs-backends
Patch34: gnome-vfs-2.17.91-fixh323.patch
Patch35: gnome-vfs-2.17.91-onlyshow.patch
Patch36: gnome-vfs-2.20.0-fstab-edit-crash.patch
Patch37: gnome-vfs-2.20.0-resolve-fstab-symlinks.patch
Patch38: gnome-vfs-2.20.0-uuid-label-mount.patch
Patch39: gnome-vfs-2.24.1-console-mount-opt.patch



%description
MATE VFS is the MATE virtual file system. It is the foundation of
the Caja file manager. It provides a modular architecture and
ships with several modules that implement support for file systems,
http, ftp, and others. It provides a URI-based API, backend
supporting asynchronous file operations, a MIME type manipulation
library, and other features.

%package devel
Summary: Libraries and include files for developing MATE VFS applications
Group: Development/C
Requires:   %{name} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for writing
MATE VFS modules and applications that use the MATE VFS APIs.

%package smb
Summary: Windows fileshare support for gnome-vfs
Group: System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires: libsmbclient
Requires: gvfs-backend-smb

%description smb
This package provides support for reading and writing files on windows
shares (SMB) to applications using MATE VFS.

%prep
%setup -q -n mate-vfs-%{version}
%patch33 -p1
NOCONFIGURE=1 ./autogen.sh

%patch3 -p1 -b .modules-conf
%patch4 -p1 -b .mime-data
%patch5 -p1 -b .CVE-2009-2473

%patch6 -p1 -b .mailto-command

# send to upstream
%patch101 -p1 -b .schema_about

%patch104 -p1 -b .browser_default

%patch300 -p1 -b .ignore-certain-mount-points

%patch404 -p1 -b .utf8-mounts

%patch405 -p1 -b .default-media

# for patch 10 and 4
autoheader
autoconf
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1

%build
if pkg-config openssl ; then
	CPPFLAGS=`pkg-config --cflags openssl`; export CPPFLAGS
	LDFLAGS=`pkg-config --libs-only-L openssl`; export LDFLAGS
fi

%configure \
	--enable-daemon \
	--enable-cdda \
	CPPFLAGS="-I/usr/include/cdda" \
	--disable-static \
%if %{with hal}
    --enable-hal
%endif


sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

#find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang mate-vfs


%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/system_http_proxy.schemas \
	%{_sysconfdir}/mateconf/schemas/system_dns_sd.schemas \
	%{_sysconfdir}/mateconf/schemas/system_smb.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_url_handlers.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_default_applications.schemas \
	> /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/system_http_proxy.schemas \
	%{_sysconfdir}/mateconf/schemas/system_dns_sd.schemas \
	%{_sysconfdir}/mateconf/schemas/system_smb.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_url_handlers.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_default_applications.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/system_http_proxy.schemas \
	%{_sysconfdir}/mateconf/schemas/system_dns_sd.schemas \
	%{_sysconfdir}/mateconf/schemas/system_smb.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_url_handlers.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_default_applications.schemas \
	> /dev/null || :
fi
%files -f mate-vfs.lang
%doc AUTHORS COPYING COPYING.LIB NEWS README
%dir %{_sysconfdir}/mate-vfs-2.0
%dir %{_sysconfdir}/mate-vfs-2.0/modules
%config %{_sysconfdir}/mate-vfs-2.0/modules/*.conf
%exclude %{_sysconfdir}/mate-vfs-2.0/modules/smb-module.conf
%{_bindir}/*
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_libdir}/*.so.*
%exclude %{_libdir}/mate-vfs-2.0/modules/libsmb.so
%{_libdir}/mate-vfs-2.0/modules
%dir %{_libdir}/mate-vfs-2.0
%{_sysconfdir}/mateconf/schemas/*
%{_datadir}/dbus-1/services/mate-vfs-daemon.service

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/mate-vfs-2.0/include
%{_includedir}/*
%{_datadir}/gtk-doc/html/mate-vfs-2.0

%files smb
%{_libdir}/mate-vfs-2.0/modules/libsmb.so
%config %{_sysconfdir}/mate-vfs-2.0/modules/smb-module.conf

%changelog
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

