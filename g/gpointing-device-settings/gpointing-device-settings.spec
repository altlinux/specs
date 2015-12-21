%set_automake_version 1.11

Name:     gpointing-device-settings
Version:  1.5.1
Release:  alt5
Summary:  Configuration tool for pointing devices

Group:    System/Configuration/Hardware
License:  LGPLv3+
Url:      https://wiki.gnome.org/Attic/GPointingDeviceSettings
# VCS:    git://git.gnome.org/gpointing-device-settings
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Source1:  gpointing-device-settings.desktop
Source2:  touchpad.png

BuildRequires: gettext, intltool
BuildRequires: libGConf-devel
BuildRequires: GConf
BuildRequires: libXi-devel
BuildRequires: gtk2-devel
BuildRequires: desktop-file-utils
BuildRequires: gnome-settings-daemon-devel

Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun):GConf2

# Obsoletes gsynaptics, to be removed in F14
Obsoletes: gsynaptics < 0.9.17
Provides: gsynaptics = %version-%release

# https://bugzilla.gnome.org/show_bug.cgi?id=631068
Patch1: gpds-1.5.1-fix_build_with_gtk22.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=637351
Patch2: gpds-1.5.1-fix-build_with_newer_gsd.patch

Patch3: gpds-1.5.1-ignore-quilt-pc.patch
Patch4: gpds-1.5.1-gsd-crash.patch

%description
GUI tool for setting pointing device such as TrackPoint or Touchpad. It
allows configuring of various drivers parameters on the fly.
It is a successor of GSynaptics.

%package devel
Summary: Development files for %name
Group: System/Configuration/Hardware
Requires: %name = %version-%release
Requires: gtk2-devel, libGConf-devel, libXi-devel
Requires: pkgconfig

%description devel
Development headers and libraries for %name.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
./autogen.sh
%autoreconf
%configure \
        --disable-static \
        --disable-schemas-install \
        --disable-dependency-tracking

# https://fedoraproject.org/wiki/Packaging:Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std

%find_lang %name

# Remove useless files
find %buildroot -name '*.la' -delete

desktop-file-install                                    \
--dir=%buildroot%_desktopdir         \
%SOURCE1

install -D %SOURCE2 %buildroot%_pixmapsdir/touchpad.png

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
%_sysconfdir/gconf/schemas/gpointing-device-settings_gnome_settings_daemon.schemas >/dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
%_sysconfdir/gconf/schemas/gpointing-device-settings_gnome_settings_daemon.schemas >/dev/null || :

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
%_sysconfdir/gconf/schemas/gpointing-device-settings_gnome_settings_daemon.schemas >/dev/null || :
fi

%files -f %name.lang
%doc NEWS TODO MAINTAINERS COPYING
%_sysconfdir/gconf/schemas/*
%_bindir/gpointing-device-settings
%_libdir/gnome-settings-daemon-2.0/*
%_libdir/gpointing-device-settings/
%_datadir/gpointing-device-settings/
%_desktopdir/*
%_pixmapsdir/touchpad.png
%_libdir/*.so.*
%_man1dir/gpointing-device-settings.1.*

%files devel
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt5
- Fix project url and source code repository
- Remove strict extension for man pages

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt4.1
- Fixed build

* Mon May 06 2013 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt4
- Restore in Sisyphus (ALT #28927)
- Build with new GConf and gnome-settings-daemon
- Add patches from Debian and Gentoo

* Mon Jun 27 2011 Alexandra Panyukova <mex3@altlinux.ru> 1.5.1-alt2.M60P.1
- adding some russian localization

* Fri Jun 24 2011 Alexandra Panyukova <mex3@altlinux.ru> 1.5.1-alt1.M60P.1
- build for p6

* Thu Jun 23 2011 Alexandra Panyukova <mex3@altlinux.ru> 1.5.1-alt1
- build for altlinux

* Fri Dec 10 2010 Gianluca Sforna <giallu@gmail.com> - 1.5.1-3
- Fix build against GTK+ 2.22
- Fix build against newer gnome-settings-daemon

* Mon May 17 2010 Gianluca Sforna <giallu gmail com> - 1.5.1-2
- add patch from upstream for #592786

* Wed Apr 14 2010 Gianluca Sforna <giallu gmail com> - 1.5.1-1
- new upstream release
- drop upstreamed patches

* Mon Sep 28 2009 Gianluca Sforna <giallu gmail com> - 1.3.1-5
- Add patch from upstream

* Wed Sep 23 2009 Gianluca Sforna <giallu gmail com> - 1.3.1-4
- fix .desktop validation issues
- add missing icon from gsynaptics

* Sun Sep 20 2009 Gianluca Sforna <giallu gmail com> - 1.3.1-3
- Don't split libgdps until translations are split as well
- Fix .pc library name
- Fix GConf scriptlets according to guidelines snippets
- Fix obsoletes
- Add .desktop file

* Tue Jul 21 2009 Gianluca Sforna <giallu gmail com> - 1.3.1-2
- Require gnome-settings-daemon
- Fix Source0 URL
- Obsoletes gsynaptics

* Wed Jul  1 2009 Gianluca Sforna <giallu gmail com> - 1.3.1-1
- Initial package
