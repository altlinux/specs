# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xrandr)
# END SourceDeps(oneline)
Group: System/Libraries
%define _libexecdir %_prefix/libexec
%define fedora 21
Summary:        Shared code for mate-panel, mate-session, mate-file-manager, etc
Name:           mate-desktop
License:        GPLv2+ and LGPLv2+ and MIT
Version:        1.8.0
Release:        alt2_0
Source0:        http://pub.mate-desktop.org/releases/1.8/%{name}-1.8.0.tar.xz
URL:            http://mate-desktop.org

# fix fedora backgrounds and
# workaround for x-caja-desktop window issue
Source1:        mate-fedora.gschema.override
Source2:        gnu-cat.gif
Source3:        gnu-cat_navideno_v3.png
Source4:        mate-fedora-f20.gschema.override
Source5:        mate-fedora-f21.gschema.override

#enable gnucat
%if 0%{?fedora} > 20
Patch0:         mate-desktop_enable_gnucat-f21.patch
%else
Patch0:         mate-desktop_enable_gnucat.patch
%endif


BuildRequires:  libdconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mate-common
BuildRequires:  libstartup-notification-devel
BuildRequires:  libunique-devel
%if 0%{?fedora} > 20
BuildRequires:  itstool
%else
BuildRequires:  mate-doc-utils
%endif

Requires: lib%{name} = %{version}-%{release}
Requires: altlinux-freedesktop-menu-common
Requires: pygtk2
Requires: xdg-user-dirs-gtk
Requires: mate-control-center-filesystem
Requires: mate-panel

Obsoletes: libmate
Obsoletes: libmate-devel
Obsoletes: libmatecanvas
Obsoletes: libmatecanvas-devel
Obsoletes: libmatecomponent
Obsoletes: libmatecomponent-devel
Obsoletes: libmatecomponentui
Obsoletes: libmatecomponentui-devel
Obsoletes: libmateui
Obsoletes: libmateui-devel
Obsoletes: mate-conf
Obsoletes: mate-conf-devel
Obsoletes: mate-conf-editor
Obsoletes: mate-conf-gtk
Obsoletes: mate-mime-data
Obsoletes: mate-mime-data-devel
Obsoletes: mate-vfs
Obsoletes: mate-vfs-devel
Obsoletes: mate-vfs-smb
# switch to gnome-keyring > f19
%if 0%{?fedora} > 19
Obsoletes: libmatekeyring
Obsoletes: libmatekeyring-devel
Obsoletes: mate-keyring
Obsoletes: mate-keyring-pam
Obsoletes: mate-keyring-devel
%endif
# temporarily solution for f20 until mate-bluetooth
# is ported to bluez5
%if 0%{?fedora} > 19
Obsoletes: mate-bluetooth < 1:1.6.0-6
Obsoletes: mate-bluetooth-libs < 1:1.6.0-6
Obsoletes: mate-bluetooth-devel < 1:1.6.0-6
%endif
%if 0%{?fedora} > 20
Obsoletes: libmatewnck
Obsoletes: libmatewnck-devel
%endif
Source44: import.info
Patch33: mate-desktop-1.5.0-alt-settings.patch
Patch34: mate-desktop-1.5.5-alt-default_background_path.patch


%description
The mate-desktop package contains an internal library
(libmatedesktop) used to implement some portions of the MATE
desktop, and also some data files and other shared components of the
MATE user environment.

%package -n libmate-desktop
Group: System/Libraries
Summary:   Shared libraries for libmate-desktop
License:   LGPLv2+

%description -n libmate-desktop
Shared libraries for libmate-desktop

%package devel
Group: Development/C
Summary:    Libraries and headers for libmate-desktop
License:    LGPLv2+
Requires:   libmate-desktop = %{version}-%{release}

%description devel
Libraries and header files for the MATE-internal private library
libmatedesktop.

%prep
%setup -q
%patch0 -p1 -b .gnucat
cp %SOURCE2 mate-about/gnu-cat.gif
cp %SOURCE3 mate-about/gnu-cat_navideno_v3.png

# needed for gnucat patch
%patch33 -p1
%patch34 -p1
autoreconf -fi

%build
%if 0%{?fedora} > 20
%configure                                                 \
     --enable-desktop-docs                                 \
     --disable-schemas-compile                             \
     --with-gtk=2.0                                        \
     --with-x                                              \
     --disable-static                                      \
     --enable-unique                                       \
     --enable-mpaste                                       \
     --with-pnp-ids-path="%{_datadir}/hwdatabase/pnp.ids"      \
     --enable-gtk-doc-html
%else
%configure \
     --disable-scrollkeeper                                \
     --disable-schemas-compile                             \
     --with-gtk=2.0                                        \
     --with-x                                              \
     --disable-static                                      \
     --enable-unique                                       \
     --with-pnp-ids-path="%{_datadir}/hwdatabase/pnp.ids"      \
     --with-omf-dir=%{_datadir}/omf/mate-desktop           \
     --enable-gnucat
%endif

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'


desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-about.desktop

%if 0%{?fedora} > 20
desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-user-guide.desktop
%endif

%if 0%{?fedora} > 19
%if 0%{?fedora} > 20
install -D -m 0644 %SOURCE5 %{buildroot}%{_datadir}/glib-2.0/schemas/mate-fedora.gschema.override
%else
install -D -m 0644 %SOURCE4 %{buildroot}%{_datadir}/glib-2.0/schemas/mate-fedora.gschema.override
%endif
%else
install -D -m 0644 %SOURCE1 %{buildroot}%{_datadir}/glib-2.0/schemas/mate-fedora.gschema.override
%endif

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/mate-desktop.convert

%if 0%{?fedora} > 20
# remove conflicting files with gnome
rm -fr %{buildroot}%{_datadir}/help/*/fdl
rm -fr %{buildroot}%{_datadir}/help/*/gpl
rm -fr %{buildroot}%{_datadir}/help/*/lgpl
%endif

%find_lang %{name} --with-gnome --all-name

mkdir -p %buildroot%{_datadir}/mate-about


%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%if 0%{?fedora} > 20
%{_bindir}/mate-about
%{_bindir}/mate-gsettings-toggle
%{_bindir}/mpaste
%{_datadir}/applications/mate-about.desktop
%{_datadir}/applications/mate-user-guide.desktop
%{_datadir}/mate-about
%{_datadir}/glib-2.0/schemas/mate-fedora.gschema.override
%{_mandir}/man1/*
%{_datadir}/pixmaps/gnu-cat.gif
%{_datadir}/pixmaps/gnu-cat_navideno_v3.png
%{_datadir}/help/*/mate-user-guide
%else
%{_bindir}/mate-about
%{_bindir}/mate-gsettings-toggle
%{_datadir}/applications/mate-about.desktop
%{_datadir}/mate
%{_datadir}/omf/mate-desktop
%{_datadir}/mate-about
%{_datadir}/glib-2.0/schemas/mate-fedora.gschema.override
%{_mandir}/man1/*
%{_datadir}/pixmaps/gnu-cat.gif
%{_datadir}/pixmaps/gnu-cat_navideno_v3.png
%endif

%files -n libmate-desktop -f %{name}.lang
%{_libdir}/libmate-desktop-2.so.*
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml

%files devel
%{_libdir}/libmate-desktop-2.so
%{_libdir}/pkgconfig/mate-desktop-2.0.pc
%{_includedir}/mate-desktop-2.0
%doc %{_datadir}/gtk-doc/html/mate-desktop


%changelog
* Tue Mar 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_0
- intermediat build

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_11
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_10
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_6
- new fc release

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- sync with new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.8-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.7-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1_1
- new fc release

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt2_1
- fixed default background

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

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

