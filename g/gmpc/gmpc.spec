%def_enable sm
%def_enable mmkeys
%def_enable configdir
%def_disable libspiff
%def_enable debug

%define Name GMPC
Name: gmpc
Version: 0.18.0
Release: alt2.1
Summary: A frontend for the mpd (Music Player Daemon)
License: %gpl2plus
Group: Sound
Url: http://%{name}wiki.sarine.nl/index.php/%Name
Source: http://download.sarine.nl/Programs/%name/%version/%name-%version.tar
Patch: %name-%version-%release.patch
Patch1: gmpc-0.18.0-alt-glib2.patch
Patch2: gmpc-0.18.0-alt-DSO.patch
Packager: Alexey Rusakov <ktirf@altlinux.org>

BuildRequires(pre): rpm-build-licenses rpm-build-gmpc

# From configure.in
BuildRequires: intltool >= 0.21
BuildRequires: zlib-devel
%{?_enable_libspiff:BuildRequires: libspiff-devel}
BuildRequires: glib2-devel >= 2.10
BuildRequires: libgtk+2-devel >= 2.12
BuildRequires: libmpd-devel >= 0.17.1
BuildRequires: libglade-devel libsoup-devel
BuildRequires: libsexy-devel
%{?_enable_sm:BuildRequires: libSM-devel}
BuildRequires: gob2 >= 2.0.0
BuildRequires: libcurl-devel

%description
%Name is a frontend for the mpd (Music Player Daemon). It's focused on
being fast and easy to use, while making optimal use of all the
functions in mpd.


%package devel
Summary: Development environment for %name.
Group: Development/C

%description devel
This package contains the header files and libraries for building program which
use %name (e.g. plugins for %name).


%prep
%setup
%patch -p1
%patch1 -p0
%patch2 -p0


%build
%autoreconf
%configure \
    %{subst_enable libspiff} \
    %{subst_enable configdir} \
    --enable-system-libsexy \
    %{subst_enable sm} \
    %{subst_enable mmkeys} \
    --with-gnu-ld
%make_build
bzip2 --best --keep --force ChangeLog


%install
%make_install DESTDIR=%buildroot install
install -d -m 0755 %buildroot%gmpc_plugin_libdir
%find_lang %name


%files -f %name.lang
%doc AUTHORS ChangeLog.*
%dir %_libdir/%name
%dir %gmpc_plugin_libdir
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*

%files devel
%_pkgconfigdir/*
%_includedir/%name

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18.0-alt2.1
- Fixed build

* Mon Mar 16 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt2
- use system libsexy instead of a bundled one
- use rpm-build-gmpc for the GMPC plugins directory macro
- updated buildreqs

* Thu Mar 12 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- 0.18.0
- new Packager
- more fixes to %name.desktop according to repocop report
- updated buildreqs

* Thu Jan 08 2009 Led <led@altlinux.ru> 0.17.0-alt1
- 0.17.0
- cleaned up spec

* Wed Nov 12 2008 Led <led@altlinux.ru> 0.16.1-alt3
- check only 2 nums in LIBMPD_VERSION

* Wed Nov 05 2008 Led <led@altlinux.ru> 0.16.1-alt2
- fixed %name.desktop

* Sat Oct 04 2008 Led <led@altlinux.ru> 0.16.1-alt1
- 0.16.1
- fixed Summary and %%description
- cleaned up spec
- fixed License
- removed %name-alt-plugin-path-fix.patch
- added %name-0.16.1-alt.patch
- added post scripts

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1.1
- fix path to plugins.

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1
- new version;
- split package to %name and %name-devel;
- use "~/.config" for config files.

* Sun Jun 10 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15.1-alt1
- new version 0.15.1 (with rpmrb script)

* Tue Jun 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15.0-alt1
- new version (0.15.0)
- updated dependencies.
- removed Debian menu support.
- added explicit configure script switches.
- updated Url and Source links.

* Mon Sep 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.13.0-alt1
- 0.13.0.

* Thu Feb 10 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.11.2-alt1
- initial build.
