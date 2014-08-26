# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize gcc-c++ glib2-devel pkgconfig(check) pkgconfig(gconf-2.0) pkgconfig(gdk-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%add_findreq_skiplist %_libexecdir/xinputinfo.sh
%add_findreq_skiplist /etc/X11/xinit/xinitrc.d/50-xinput.sh
Name:		imsettings
Version:	1.6.7
Release:	alt2
License:	LGPLv2+
URL:		https://tagoh.bitbucket.org/%{name}/
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildRequires:	desktop-file-utils
BuildRequires:	intltool gettext
BuildRequires:	libtool automake autoconf
BuildRequires:	glib2 >= 2.32.0 gobject-introspection-devel libgtk+3-devel >= 3.3.3
BuildRequires:	libnotify-devel
BuildRequires:	libX11-devel libgxim-devel >= 0.5.0
%if !0%{?rhel}
BuildRequires:	libxfconf-devel
%endif
Source0:	https://bitbucket.org/tagoh/%{name}/downloads/%{name}-%{version}.tar.bz2
## Fedora specific: run IM for certain languages only
Patch0:		%{name}-constraint-of-language.patch
## Fedora specific: Disable XIM support
Patch1:		%{name}-disable-xim.patch
## Fedora specific: Enable xcompose for certain languages
Patch2:		%{name}-xinput-xcompose.patch
## Fedora specific: Force enable the IM management on imsettings for Cinnamon
Patch3:		%{name}-force-enable-for-cinnamon.patch

Summary:	Delivery framework for general Input Method configuration
Group:		File tools
Requires:	xinit >= 1.0.2-22.fc8
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-desktop-module%{?_isa} = %{version}-%{release}
Requires(post):	/bin/dbus-send alternatives
Requires(postun):	/bin/dbus-send alternatives
Source44: import.info

%description
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the core DBus services and some utilities.

%package	libs
Summary:	Libraries for imsettings
Group:		Development/C

%description	libs
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the shared library for imsettings.

%package	devel
Summary:	Development files for imsettings
Group:		Development/C
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the development files to make any
applications with imsettings.

%package	xim
Summary:	XIM support on imsettings
Group:		File tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser

%description	xim
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working with XIM.

%package	gsettings
Summary:	GSettings support on imsettings
Group:		File tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	dconf
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}
Provides:	%{name}-gnome = %{version}-%{release}
Obsoletes:	%{name}-gnome < 1.5.1-3

%description	gsettings
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on
GNOME and Cinnamon which requires GSettings in their
own XSETTINGS daemons.

%package	qt
Summary:	Qt support on imsettings
Group:		File tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	qt
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Qt
applications.

%if !0%{?rhel}
%package	xfce
Summary:	Xfce support on imsettings
Group:		File tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser-xfce
Requires:	xfce4-settings >= 4.5.99.1-2
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	xfce
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Xfce.  

%package	lxde
Summary:	LXDE support on imsettings
Group:		File tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	lxde-settings-daemon
# Hack for upgrades: see https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	lxde-lxsession
Requires:	/usr/bin/lxsession
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	lxde
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on LXDE.

%package	mate
Summary:	MATE support on imsettings
Group:		File tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
# need to keep more deps for similar reason to https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	mate-settings-daemon >= 1.5.0
Requires:	mate-session-manager
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	mate
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on MATE.

%package	cinnamon
Summary:	Cinnamon support on imsettings
Group:		File tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
# need to keep more deps for similar reason to https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	cinnamon
Requires:	cinnamon-session
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	cinnamon
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Cinnamon.
%endif

%prep
%setup -q
%patch0 -p1 -b .0-lang
%patch1 -p1 -b .1-xim
%patch2 -p1 -b .2-xcompose
%patch3 -p1 -b .3-force-cinnamon

%build
%configure	\
	--with-xinputsh=50-xinput.sh \
	--disable-static \
	--disable-schemas-install

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

# change the file attributes
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/imsettings-target-checker.sh
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/xinputinfo.sh
chmod 0755 $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh

# clean up the unnecessary files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/libimsettings-{gconf,mateconf}.so
%if 0%{?rhel}
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/libimsettings-{lxde,xfce,mate-gsettings}.so
%endif

desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/imsettings-start.desktop

%find_lang %{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_imsettings<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_sysconfdir}/X11/xinit/xinput.d/none.conf	10
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_imsettings<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_sysconfdir}/X11/xinit/xinput.d/xcompose.conf	20
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_imsettings<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_sysconfdir}/X11/xinit/xinput.d/xim.conf	30
EOF


#%%check
## Disable it because it requires DBus session
# make check

%post
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig > /dev/null 2>&1 || :

%postun
if [ "$1" = 0 ]; then
	:
	dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig > /dev/null 2>&1 || :
fi

%files	-f %{name}.lang
%_altdir/xinputrc_imsettings
%_altdir/xinputrc_imsettings
%_altdir/xinputrc_imsettings
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_libdir}/imsettings
%{_bindir}/imsettings-info
%{_bindir}/imsettings-list
%{_bindir}/imsettings-reload
%{_bindir}/imsettings-switch
%{_libexecdir}/imsettings-check
%{_libexecdir}/imsettings-daemon
%{_libexecdir}/xinputinfo.sh
%{_libexecdir}/imsettings-functions
%{_libexecdir}/imsettings-target-checker.sh
%{_datadir}/dbus-1/services/*.service
%{_datadir}/pixmaps/*.png
%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh
%{_sysconfdir}/X11/xinit/xinput.d
%{_sysconfdir}/xdg/autostart/imsettings-start.desktop
%{_mandir}/man1/imsettings-*.1*

%files	libs
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libimsettings.so.*

%files	devel
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/imsettings
%{_libdir}/libimsettings.so
%{_libdir}/pkgconfig/imsettings.pc
%{_libdir}/girepository-*/IMSettings-*.typelib
%{_datadir}/gir-*/IMSettings-*.gir
%{_datadir}/gtk-doc/html/imsettings

%files	xim
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/imsettings-xim
%{_libdir}/imsettings/libimsettings-xim.so

%files	gsettings
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-gsettings.so

%files	qt
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-qt.so

%if !0%{?rhel}
%files	xfce
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-xfce.so

%files	lxde
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-lxde.so

%files	mate
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-mate-gsettings.so

%files cinnamon
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-cinnamon-gsettings.so
%endif


%changelog
* Tue Aug 26 2014 Ilya Mashkin <oddity@altlinux.ru> 1.6.7-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1_3
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1_2
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_1
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- update to new release by fcimport

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- update to new release by fcimport

* Tue Feb 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- update to new release by fcimport

* Tue Feb 12 2013 Cronbuild Service <cronbuild@altlinux.org> 1.5.1-alt2_2
- rebuild to get rid of unmets

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- initial fc import

