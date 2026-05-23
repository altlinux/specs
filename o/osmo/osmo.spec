%def_enable snapshot
%def_enable printing
%def_enable backup
%define ver_micro %nil

Name: osmo
Version: 0.4.4
Release: alt2

Summary: Personal organizer
License: GPL-2.0-or-later
Group: Office
Url: https://sourceforge.net/projects/osmo-pim

%if_disabled snapshot
Source: https://downloads.sourceforge.net/%name-pim/%name-%version%ver_micro.tar.gz
%else
Source: %name-%version%ver_micro.tar
%endif
Patch1: %name-0.4.4-alt-incompatible-pointer-types.patch

Vcs: https://git.code.sf.net/p/osmo-pim/osmo.git

%define gtk_ver 3.24.0
%define webkit_ver 2.8

BuildRequires: libgtk+3-devel >= %gtk_ver libgspell-devel libxml2-devel
BuildRequires: libnotify-devel libical-devel libicu-devel
BuildRequires: pkgconfig(webkit2gtk-4.1) >= %webkit_ver
%{?_enable_backup:BuildRequires: libgringotts-devel libarchive-devel}

%description
Osmo is a handy personal organizer which includes calendar, tasks manager and
address book modules. It was designed to be a small, easy to use and good
looking PIM tool to help to manage personal information. In current state the
organizer is quite convenient in use - for example, user can perform nearly
all operations using keyboard. Also, a lot of parameters are configurable to
meet user preferences.

%prep
%setup -n %name-%version%ver_micro
%patch1 -b .ipt

%build
%autoreconf
%configure \
    %{?_enable_backup:--enable-backup=yes} \
    %{?_enable_printing:--enable-printing}
%nil
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_man1dir/*
%dir %_datadir/sounds/%name
%_datadir/sounds/%name/alarm.wav
%_pixmapsdir/*.png
%doc AUTHORS ChangeLog README TRANSLATORS

%changelog
* Sat May 23 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt2
- update to last commit (RELEASE_0_4_2-53-g125cfe6)
- fixed build with gcc-15

* Mon Jul 13 2020 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt3
- rebuilt against libgspell-1.so.2

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt2
- rebuilt against libical.so.3

* Wed Nov 29 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Apr 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt2
- updated to 0.4.0-1

* Sun Apr 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt1
- 0.2.14

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt1
- 0.2.12

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt6
- explicitly link against libm

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt5
- rebuilt against libical.so.1
- use automake-1.11

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

