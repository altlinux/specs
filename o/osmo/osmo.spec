%def_enable printing
%def_enable backup
%def_without libsyncml

Name: osmo
Version: 0.2.10
Release: alt4

Summary: Personal organizer
License: GPLv2+
Group: Office
Url: http://clayo.org/osmo/
Source: http://downloads.sourceforge.net/%name-pim/%name-%version.tar.gz

Patch: %name-0.2.8-alt-configure.patch
Patch1: osmo-0.2.10-libnotify-0.7.0.patch

BuildRequires: libgtk+2-devel libgtkspell-devel libxml2-devel
BuildRequires: libnotify-devel libical-devel libgtkhtml2-devel
%{?_with_libsyncml:BuildRequires: libsyncml-devel}
%{?_enable_backup:BuildRequires: libgringotts-devel libtar-devel}

%description
Osmo is a handy personal organizer which includes calendar, tasks manager and
address book modules. It was designed to be a small, easy to use and good
looking PIM tool to help to manage personal information. In current state the
organizer is quite convenient in use - for example, user can perform nearly
all operations using keyboard. Also, a lot of parameters are configurable to
meet user preferences.

%prep
%setup -q
%patch
%patch1 -p1

%build
export CFLAGS="$CFLAGS -I%_includedir/libical"
%autoreconf
%configure \
	%{?_enable_backup:--enable-backup=yes} \
	%{?_enable_printing:--enable-printing} \
	%{subst_with libsyncml}

%make_build

%install
mkdir -p %buildroot%_datadir/icons/hicolor/{48x48,scalable}/apps

%make DESTDIR=%buildroot install

# move icon
mv %buildroot%_datadir/pixmaps/%name.png \
  %buildroot%_datadir/icons/hicolor/48x48/apps/

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/%name.*
%_man1dir/*
%dir %_datadir/sounds/%name
%_datadir/sounds/%name/alarm.wav
%doc AUTHORS ChangeLog README README.syncml TRANSLATORS

%changelog
* Tue Jun 07 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt4
- fixed for libnotify-0.7

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt3
- built with backup support using libtar and libgringotts (closes #23649)

* Sat May 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt2
- fixed build against new broken libical

* Thu Apr 01 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- 0.2.10
- updated buildreqs

* Sat Feb 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- first build for Sisyphus

