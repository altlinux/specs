%define ver_major 3.4

Name: evolution-mapi
Version: %ver_major.3
Release: alt1
Group: Networking/Mail
Summary: Evolution extension for MS Exchange 2007 servers
License: LGPLv2+
Url: http://www.gnome.org/projects/evolution-mapi/

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar
Patch: %name-%version-%release.patch

%define ver_base 3.4
%define evo_ver_base %ver_base

%define evolution_ver 3.4.0
# from configure.in.
%define eds_ver 3.4.0
%define libmapi_version 1.0

Requires: evolution >= %evolution_ver
Requires: evolution-data-server >= %eds_ver

BuildPreReq: gnome-common rpm-build-gnome
BuildPreReq: evolution-data-server-devel >= %eds_ver
BuildPreReq: evolution-devel >= %evolution_ver
BuildPreReq: intltool >= 0.35.5
BuildRequires: libtalloc-devel
BuildRequires: openchange-devel >= %libmapi_version
BuildRequires: samba4-devel
BuildRequires: gcc-c++ gtk-doc

%description
This package allows Evolution to interact with MS Exchange 2007 servers.

%package devel
Summary: Development files for building against %name
Group: Development/C
Requires: %name = %version-%release
Requires: evolution-data-server-devel >= %eds_ver
Requires: evolution-devel >= %evolution_ver
Requires: openchange-devel >= %libmapi_version

%description devel
Development files needed for building things which link against %name.

%prep
%setup
%patch -p1

%build
# Add stricter build settings here as the source code gets cleaned up.
# We want to make sure things like compiler warnings and avoiding deprecated
# functions in the GNOME/GTK+ libraries stay fixed.
#
# Please file a bug report at bugzilla.gnome.org if these settings break
# compilation, and encourage the upstream developers to use them.

#%%if %%strict_build_settings
#CFLAGS="$CFLAGS \
#	-DG_DISABLE_DEPRECATED=1 \
#	-DPANGO_DISABLE_DEPRECATED=1 \
#	-DGDK_PIXBUF_DISABLE_DEPRECATED=1 \
#	-DGDK_DISABLE_DEPRECATED=1 \
#	-DGTK_DISABLE_DEPRECATED=1 \
#	-DEDS_DISABLE_DEPRECATED=1 \
#	-Wdeclaration-after-statement \
#	-Werror-implicit-function-declaration"
#%%endif
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name '*.la' -exec rm {} \;

%find_lang %name


# COPYING has the wrong license.  Do not include it until fixed.

%files -f %name.lang
%doc AUTHORS ChangeLog INSTALL README
%_libdir/*.so.*
%_libdir/evolution/%evo_ver_base/plugins/*
%_libdir/evolution-data-server/camel-providers/*
%_libdir/evolution-data-server/addressbook-backends/*.so
%_libdir/evolution-data-server/calendar-backends/*.so
%_datadir/evolution-data-server-%evo_ver_base/mapi

%files devel
%_includedir/evolution-data-server-%evo_ver_base/mapi
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jun 18 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.3-alt1
- 3.4.3

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1
- 3.4.2

* Mon Apr 02 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Thu Aug 25 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Thu May 12 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Mon Apr 18 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Mon Apr 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.32.2-alt1
- 0.32.2

* Mon Aug 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.30.3-alt1
- initial build for ALT Linux Sisyphus
