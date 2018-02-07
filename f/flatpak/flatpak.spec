%define _userunitdir /usr/lib/systemd/user

Name: flatpak
Version: 0.10.3
Release: alt1

Summary: Application deployment framework for desktop apps

Group: Development/Tools
License: LGPLv2+
Url: http://flatpak.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://github.com/flatpak/flatpak/releases/download/%version/%name-%version.tar.xz
# Until https://github.com/flatpak/flatpak/pull/225 is merged and a new release
# made.
Patch: flatpak-0.6.8-add-flatpak-metadata-xml.patch

BuildRequires: rpm-macros-intro-conflicts libelf-devel gtk-doc gobject-introspection-devel

BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libarchive) >= 2.8.0
# we have no pc file
#BuildRequires: pkgconfig(libelf) >= 0.8.12
BuildRequires: pkgconfig(libgsystem) >= 2015.1
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(ostree-1) >= 2017.8
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(xau)
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: intltool
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: libdwarf-devel
BuildRequires: libgpgme-devel
BuildRequires: udev-rules
BuildRequires: %_bindir/bwrap
BuildRequires: %_bindir/xmlto
BuildRequires: %_bindir/xsltproc

BuildRequires: bubblewrap >= 0.1.5

BuildRequires: /proc

# Crashes with older kernels (the bug being introduced in 4.0.2), without the
# upstream fixes in this version.
#Requires: kernel >= 4.0.4-202

# Needed for the document portal.
Requires: %_bindir/fusermount

Requires: %_bindir/bwrap

%description
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package builder
Summary: Build helper for %name
Group: Development/Tools
License: LGPLv2+
Requires: %name%{?_isa} = %version-%release
Requires: %_bindir/bzr
Requires: %_bindir/git
Requires: %_bindir/patch
Requires: %_bindir/strip
Requires: /bin/tar
Requires: %_bindir/unzip

%description builder
flatpak-builder is a tool that makes it easy to build applications and their
dependencies by automating the configure && make && make install steps.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
License: LGPLv2+
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the pkg-config file and development headers for %name.

%package -n lib%name
Summary: Libraries for %name
Group: Development/Other
License: LGPLv2+
Requires: %_bindir/bwrap

%description -n lib%name
This package contains libflatpak.

%prep
%setup
#patch0 -p1

%build
# workaround for collision with new copy_file_range glibc function. remove it when it's no longer needed.
%add_optflags -DHAVE_DECL_COPY_FILE_RANGE
# User namespace support is sufficient.
%configure --with-dwarf-header=%_includedir/libdwarf --with-priv-mode=none \
           --with-system-bubblewrap --enable-docbook-docs \
           --with-systemdsystemunitdir=%_unitdir --with-systemduserunitdir=%_userunitdir
%make_build V=1

%install
%makeinstall_std
# The system repo is not installed by the flatpak build system.
install -d %buildroot%_localstatedir/lib/flatpak
rm -f %buildroot%_libdir/libflatpak.la
rm -rf %buildroot%_docdir/%name/
%find_lang %name

%post
# Create an (empty) system-wide repo.
%_bindir/flatpak remote-list --system

%files -f %name.lang
%doc COPYING NEWS README.md
%_bindir/flatpak
%_datadir/bash-completion
%_datadir/dbus-1/services/org.freedesktop.Flatpak.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%_datadir/dbus-1/services/org.freedesktop.portal.Documents.service
%_datadir/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
# Co-own directory.
%_datadir/gdm/env.d
%_datadir/%name
%_datadir/polkit-1/actions/org.freedesktop.Flatpak.policy
%_datadir/polkit-1/rules.d/org.freedesktop.Flatpak.rules
%_libexecdir/flatpak-dbus-proxy
%_libexecdir/flatpak-session-helper
%_libexecdir/flatpak-system-helper
%_libexecdir/xdg-document-portal
%_libexecdir/xdg-permission-store
%dir %_localstatedir/lib/flatpak
%_man1dir/%{name}*.1*
#exclude %_man1dir/flatpak-builder.*
%_sysconfdir/dbus-1/system.d/org.freedesktop.Flatpak.SystemHelper.conf
%_sysconfdir/profile.d/flatpak.sh
%_unitdir/flatpak-system-helper.service
%_userunitdir/flatpak-session-helper.service
%_userunitdir/xdg-document-portal.service
%_userunitdir/xdg-permission-store.service
# Co-own directory.
%_userunitdir/dbus.service.d
%_man5dir/*

%files builder
#_bindir/flatpak-builder
%_bindir/flatpak-bisect
#_man1dir/flatpak-builder.*

%files -n lib%name-devel
%_datadir/gir-1.0/Flatpak-1.0.gir
%_datadir/gtk-doc/
%_includedir/%name/
%_libdir/libflatpak.so
%_pkgconfigdir/%name.pc
%_datadir/dbus-1/interfaces/org.freedesktop.Flatpak.xml
%_datadir/dbus-1/interfaces/org.freedesktop.portal.Documents.xml
%_datadir/dbus-1/interfaces/org.freedesktop.impl.portal.PermissionStore.xml

%files -n lib%name
%doc COPYING
%_libdir/girepository-1.0/Flatpak-1.0.typelib
%_libdir/libflatpak.so.*

%changelog
* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.3-alt1
- Updated to upstream version 0.10.3.

* Tue Dec 26 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2.1-alt2
- move dbus-1/interfaces to libflatpak-devel

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2.1-alt1
- new version 0.10.2.1 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- new version 0.10.2 (with rpmrb script)

* Sat Nov 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.99-alt1
- new version 0.9.99 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.98.2-alt1
- new version 0.9.98.2 (with rpmrb script)

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- new version 0.9.11 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version (0.9.7) with rpmgs script

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.11-alt1
- new version 0.6.11 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.8-alt1
- initial build for ALT Linux Sisyphus

* Mon Aug 01 2016 David King <amigadave@amigadave.com> - 0.6.8-1
- Update to 0.6.8 (#1361823)

* Thu Jul 21 2016 David King <amigadave@amigadave.com> - 0.6.7-2
- Use system bubblewrap

* Fri Jul 01 2016 David King <amigadave@amigadave.com> - 0.6.7-1
- Update to 0.6.7

* Thu Jun 23 2016 David King <amigadave@amigadave.com> - 0.6.6-1
- Update to 0.6.6

* Fri Jun 10 2016 David King <amigadave@amigadave.com> - 0.6.5-1
- Update to 0.6.5

* Wed Jun 01 2016 David King <amigadave@amigadave.com> - 0.6.4-1
- Update to 0.6.4

* Tue May 31 2016 David King <amigadave@amigadave.com> - 0.6.3-1
- Update to 0.6.3
- Move bwrap to main package

* Tue May 24 2016 David King <amigadave@amigadave.com> - 0.6.2-1
- Rename from xdg-app to flatpak (#1337434)
