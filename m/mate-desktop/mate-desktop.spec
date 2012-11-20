# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xrandr)
# END SourceDeps(oneline)
Group: System/Libraries
%define _libexecdir %_prefix/libexec
Summary:	Shared code for mate-panel, mate-session, mate-file-manager, etc
Name:		mate-desktop
Version:	1.5.3
Release:	alt2_5
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Source1:        user-dirs-update-mate.desktop

License:	GPLv2+ and LGPLv2+ and MIT

BuildRequires:	mate-common
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	desktop-file-utils

Requires:	lib%{name} = %{version}-%{release}
Requires:	altlinux-freedesktop-menu-common
Requires:	pygtk2
Requires:       xdg-user-dirs-gtk
Source44: import.info
Patch33: mate-desktop-1.5.0-alt-settings.patch

%description
The mate-desktop package contains an internal library
(libmatedesktop) used to implement some portions of the MATE
desktop, and also some data files and other shared components of the
MATE user environment.

%package -n libmate-desktop
Summary:	Shared libraries for libmate-desktop
License:	LGPLv2+
Group:		System/Libraries

%description -n libmate-desktop
Shared libraries for libmate-desktop

%package devel
Summary:	Libraries and headers for libmate-desktop
License:	LGPLv2+
Group:		Development/C
Requires:	libmate-desktop = %{version}-%{release}

%description devel
Libraries and header files for the MATE-internal private library
libmatedesktop.

%prep
%setup -q
%patch33 -p1
NOCONFIGURE=1 ./autogen.sh


%build

%configure --disable-libtool-lock				\
	--disable-scrollkeeper					\
	--disable-static					\
	--with-pnp-ids-path="%{_datadir}/hwdatabase/pnp.ids"	\
	--enable-unique						\
	--enable-gnucat						\
	--enable-gtk-doc                                        \
        --with-omf-dir=%{_datadir}/omf/mate-desktop

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
find %{buildroot}  -name '*.la' -exec rm -f {} ';'


desktop-file-install \
	--remove-category="MATE"					\
	--add-category="X-Mate"						\
	--delete-original						\
	--dir=%{buildroot}%{_datadir}/applications			\
%{buildroot}%{_datadir}/applications/mate-about.desktop

install -D -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/xdg/autostart/user-dirs-update-mate.desktop

%find_lang %{name} --with-gnome

mkdir -p %buildroot%{_datadir}/mate-about


%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/mate-about
%{_sysconfdir}/xdg/autostart/user-dirs-update-mate.desktop
%{_datadir}/applications/mate-about.desktop
%{_datadir}/mate/help/*/*/*.xml
%{_datadir}/omf/mate-desktop/
%{_datadir}/mate-about/
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml
%{_mandir}/man1/mate-about.1*
%{_datadir}/pixmaps/gnu-cat*

%files -n libmate-desktop
%{_libdir}/libmate-desktop-2.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/mate-desktop/
%{_libdir}/libmate-desktop-2.so
%{_libdir}/pkgconfig/mate-desktop-2.0.pc
%{_includedir}/mate-desktop-2.0/


%changelog
* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt2_5
- dropped transaction hack

* Sat Nov 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_5
- added mate-desktop-1.5.0-alt-settings.patch - font settings

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_4
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.1-alt1_5.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_5
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

