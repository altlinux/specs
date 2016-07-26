# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bbrun /usr/bin/firefox /usr/bin/gencat /usr/bin/gnome-terminal /usr/bin/gvim gcc-c++ imake libX11-devel xorg-cf-files
# END SourceDeps(oneline)
Summary: The bastard son of Blackbox, a small and fast Window Manager
Name: hackedbox
Version: 0.8.5
Release: alt1_17
# Most of the sources are MIT-licensed from blackbox, but a (very) small
# portion is GPLv2+, so that is the resulting license
License: GPLv2+
Group: Graphical desktop/Other
URL: http://scrudgeware.org/projects/Hackedbox
Source0: http://scrudgeware.org/downloads/hackedbox/hackedbox-%{version}.tar.gz
Source1: hackedbox.desktop
Patch0: hackedbox-0.8.5-noblackbox.patch
Patch1: hackedbox-0.8.5-gcc43.patch
BuildRequires: libXt-devel, libXext-devel
# We heavily patch *.in files...
BuildRequires: autoconf-common, automake-common, libtool-common
Source44: import.info
Source45: hackedbox.alternatives
Source46: hackedbox.menu
Source47: hackedbox.png
Source48: hackedbox.menu-method
Source49: hackedbox.wmsession

%description
Hackedbox is a stripped down version of Blackbox - The X11 Window Manager.
The toolbar and Slit have been removed. The goal of Hackedbox is to be a
small "feature-set" window manager, with no bloat. There are no plans to
add any functionality, only bugfixes and speed enhancements whenever possible.


%prep
%setup -q
%patch0 -p1 -b .noblackbox
%patch1 -p1 -b .gcc43
# Remove included binary files! and *.mk supposed to be built from *.mk.in
%{__rm} -f util/bsetroot util/bsetroot.o
%{__rm} -f util/bgmenu.mk
# Rename files, completes the noblackbox patch (avoids bloating the patch)
%{__mv} util/bsetbg util/hsetbg
%{__mv} util/bgmenu.mk.in util/hgmenu.mk.in


%build
sh bootstrap
#autoreconf -i -f
%configure \
        --enable-shared \
        --disable-static \
        --sysconfdir=%_sysconfdir/X11/%name \
        --enable-nls 
%make_build DEFAULT_MENU=%_sysconfdir/X11/%name/%name-menu


%install
%{__make} install DESTDIR=%{buildroot}

# Install GDM session file
%{__mkdir_p} %{buildroot}/etc/X11/gdm/Sessions
%{__cat} > %{buildroot}/etc/X11/gdm/Sessions/Hackedbox << EOF
#!/bin/sh
exec /etc/X11/xdm/Xsession hackedbox
EOF

# Replace the /usr/local stuff
%{__perl} -pi -e 's|/local||g' %{buildroot}%{_datadir}/hackedbox/menu

# Install the desktop entry
%{__install} -D -p -m 644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/hackedbox.desktop
# ALT specific
install -pD -m755 %SOURCE48 %buildroot%_sysconfdir/menu-methods/%name
install -pD -m644 %SOURCE46 %buildroot%_menudir/%name
install -pD -m644 %SOURCE47 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -pD -m644 %SOURCE49 %buildroot%_sysconfdir/X11/wmsession.d/07%name
install -pD -m644 %SOURCE45 %buildroot%_altdir/%name

install -pD -m644 /dev/null %buildroot%_sysconfdir/X11/%name/%name-menu

# conflicts
rm -f %buildroot/etc/X11/gdm/Sessions/Hackedbox 



%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/hackedbox
%{_bindir}/hsetbg
%{_bindir}/hsetroot
%{_bindir}/inithack
%dir %{_datadir}/hackedbox/
%config(noreplace) %{_datadir}/hackedbox/hgmenu.mk
%config(noreplace) %{_datadir}/hackedbox/menu
%{_datadir}/hackedbox/backgrounds
%{_datadir}/hackedbox/nls
%{_datadir}/hackedbox/styles
%{_datadir}/xsessions/hackedbox.desktop
%{_mandir}/man1/*
# ALT specific
%_menudir/*
%config(noreplace) %_sysconfdir/menu-methods/*
%config %_sysconfdir/X11/wmsession.d/*
%dir %_sysconfdir/X11/%name
%ghost %_sysconfdir/X11/%name/%name-menu
%_altdir/%name
%_iconsdir/hicolor/64x64/apps/%name.png



%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_13
- update to new release by fcimport

* Thu Aug 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_12
- fc import. moved to autoimports

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_11
- update to new release by fcimport

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_10
- initial fc import

