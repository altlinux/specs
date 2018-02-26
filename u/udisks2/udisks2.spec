%define _name udisks
%define api_ver 2.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%def_enable introspection

Name: %{_name}2
Version: 1.98.0
Release: alt1

Summary: Disk Management Service (Second Edition)
License: GPLv2+
Group: System/Libraries
Url: http://www.freedesktop.org/wiki/Software/%_name

Source: http://udisks.freedesktop.org/releases/%_name-%version.tar.bz2
# while glibc-kernheaders is outdated (#26907)
Patch: %_name-1.91.0-alt-LOOP_CTL_GET_FREE.hack
Patch1: %_name-1.92.0-alt-udiskd_dir.patch

Requires: lib%name = %version-%release

%define glib_ver 2.31.13
%define gi_ver 1.30.0
%define polkit_ver 0.101
%define udev_ver 147
%define libatasmart_ver 0.17
%define dbus_ver 1.4.0

BuildRequires: intltool gtk-doc gnome-common
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libpolkit-devel >= %polkit_ver
BuildRequires: libatasmart-devel >= %libatasmart_ver
BuildRequires: libudev-devel libgudev-devel >= %udev_ver
BuildRequires: libacl-devel systemd-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver}

Requires: /lib/udev/rules.d /usr/sbin/cryptsetup mdadm
Requires: dbus >= %dbus_ver ntfsprogs parted gdisk acl

%description
The udisks project provides a daemon, tools and libraries to access
and manipulate disks and storage devices.

%package -n lib%name
Summary: Dynamic library to access the udisks daemon (Second Edition)
Group: System/Libraries

%description -n lib%name
The udisks project provides a daemon, tools and libraries to access
and manipulate disks and storage devices.

This package contains the dynamic %name library, which provides
access to the udisks daemon.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the development files for the library lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
Conflicts: %name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for lib%name.


%prep
%setup -n %_name-%version
%patch
%patch1

%build
%autoreconf
# needed for O_CLOEXEC from bits/fcntl.h
%add_optflags -D_GNU_SOURCE
%configure --disable-static \
	--enable-gtk-doc

%make

%install
%makeinstall_std

mkdir -p %buildroot%_localstatedir/run/%name
touch %buildroot%_localstatedir/lib/%name/mtab

%find_lang %name

%check
%make check

%files -f %name.lang
%_sbindir/umount.%name
%_bindir/udisksctl
/lib/udev/rules.d/80-%name.rules
%dir %_libexecdir/%name
%_libexecdir/%name/udisksd
%_datadir/polkit-1/actions/org.freedesktop.%name.policy
%_datadir/dbus-1/system-services/org.freedesktop.UDisks2.service
%_sysconfdir/dbus-1/system.d/org.freedesktop.UDisks2.conf
%_sysconfdir/bash_completion.d/udisksctl-bash-completion.sh
%_mandir/man1/*
%_mandir/man8/*
%attr(0700,root,root) %dir %_localstatedir/lib/%name
%ghost %_localstatedir/lib/%name/mtab
%attr(0700,root,root) %dir %_localstatedir/run/%name
%config %systemd_unitdir/udisks2.service
%doc README AUTHORS NEWS HACKING

%files -n libudisks2
%_libdir/libudisks2.so.*

%files -n libudisks2-devel
%_libdir/lib%name.so
%_includedir/%name/
%_libdir/pkgconfig/%name.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/udisks2/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/UDisks-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/UDisks-%api_ver.gir
%endif

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.98.0-alt1
- 1.98.0

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.97.0-alt1
- 1.97.0

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.96.0-alt1
- 1.96.0

* Wed Apr 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.94.0-alt1.1
- 1.94.0 release

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.94.0-alt1
- 1.94.0 snapshot (ALT #27198)

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.93.0-alt2
- fixed udisksdprivdir accordingly with %%_libexecdir

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.93.0-alt1
- 1.93.0

* Wed Feb 29 2012 Yuri N. Sedunov <aris@altlinux.org> 1.92.0-alt1
- 1.92.0

* Wed Feb 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.91.0-alt1
- first build for Sisyphus
