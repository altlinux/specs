# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-compile-schemas /usr/bin/msgfmt pkgconfig(glib-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec

Summary:  MATE Keyboard LED indicator 
Name:     mate-applet-lockkeys
Version:  0.2.4
Release:  alt1_0
Group:    File tools
License:  GPLv2+
URL:      http://www.zavedil.com/mate-lock-keys-applet/
Source:   http://www.zavedil.com/wp-content/uploads/2013/02/%{name}-%{version}.tar.gz

BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: mate-panel-devel
BuildRequires: popt-devel

Requires: mate-panel
Source44: import.info

%description
Keyboard LED indicator applet for the MATE desktop environment.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/gschemas.compiled
rm -f $RPM_BUILD_ROOT%{_docdir}/mate-applet-lockkeys/*

%find_lang %{name}

%post
/bin/touch --no-create %{_datadir}/icons &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons &>/dev/null
fi

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog COPYING README TODO
%{_libexecdir}/lockkeys_applet
%{_datadir}/pixmaps/*.xpm
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/applet_lockkeys.png
%{_datadir}/mate-panel/applets/org.mate.applets.LockkeysApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.LockkeysApplet.service
%{_datadir}/mate-2.0/ui/lockkeys-applet-menu.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.LockkeysApplet.gschema.xml


%changelog
* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_0
- new version

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_3
- new fc release

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_2
- new fc release

