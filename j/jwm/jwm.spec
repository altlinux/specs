Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: libX11-devel libXext-devel xorg-proto-devel
# END SourceDeps(oneline)
%define fedora 34
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jwm
Version:        2.3.7
Release:        alt2_11
Summary:        Joe's Window Manager

License:        GPLv2+
URL:            http://joewing.net/projects/jwm/
Source0:        %{url}/releases/%{name}-%{version}.tar.xz
Source1:        %{name}.desktop

BuildRequires:  gcc
BuildRequires:  pkgconfig(libpng)
%if 0%{?fedora} > 24
BuildRequires:  pkgconfig(libjpeg)
%else
BuildRequires:  libjpeg-devel
%endif
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  libXpm libXpm-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXinerama-devel
BuildRequires:  gettext gettext-tools
Requires:     /usr/bin/xterm
Source44: import.info
Patch33: jwm-2.3.7-alt-config-file.patch
Source45: jwm.method
Source46: jwm.wmsession
Source47: jwm-conf.tar
Source48: jwm.svg
Source49: startjwm
#Recommends:     /usr/bin/xlock

%description
JWM is a window manager for the X11 Window System. It's written in C and uses
only Xlib at a minimum. The following libraries can also be used if available:

* cairo and librsvg2 for SVG icons and backgrounds.
* fribidi for bi-directional text support.
* libjpeg for JPEG icons and backgrounds.
* libpng for PNG icons and backgrounds.
* libXext for the shape extension.
* libXrender for the render extension.
* libXmu for rounded corners.
* libXft for anti-aliased and true type fonts.
* libXinerama for multiple head support.
* libXpm for XPM icons and backgrounds.

JWM supports MWM and Extended Window Manager Hints (EWMH).

Note that Fedora package is built with all supported features enabled.

%prep
%setup -q


# Preserve timestamps in installation
sed -i -e 's|install -m|install -pm|g' Makefile.in
%patch33 -p1

%build
# -Werror
CFLAGS="$CFLAGS -O3 -Wall"
%autoreconf
%configure \
        --enable-debug \
        --enable-shade \
        --sysconfdir=%_sysconfdir/X11/jwm 
%make_build

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/xsessions
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/

%find_lang %{name}

tar -xC %buildroot/%_sysconfdir/X11/jwm -f %SOURCE47
rm -f -- %buildroot/%_sysconfdir/X11/jwm/system.jwmrc

# install -m755 %SOURCE49 %buildroot%_bindir/
install -D -m644 %SOURCE46 %buildroot%_sysconfdir/X11/wmsession.d/15jwm
install -D -m644 %SOURCE48 %buildroot%_iconsdir/hicolor/scalable/apps/jwm.svg
install -D -m 755 %{SOURCE45} %buildroot%_sysconfdir/menu-methods/jwm

%files -f %{name}.lang
%doc --no-dereference LICENSE
%doc ChangeLog README.md
%doc %{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/X11/jwm/*
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/%{name}/
%_iconsdir/hicolor/scalable/apps/jwm.svg
%config %_sysconfdir/menu-methods/jwm
%config %_sysconfdir/X11/wmsession.d/15jwm

%changelog
* Fri Nov 12 2021 Igor Vlasenko <viy@altlinux.org> 2.3.7-alt2_11
- added priority to wmsession file name

* Wed Nov 03 2021 Igor Vlasenko <viy@altlinux.org> 2.3.7-alt1_11
- WM policy 2.0: added svg. fixed desktop

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_5
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_4
- resurrected as fc import

* Fri Mar 12 2010 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt5.20100305
- Fix dead windows in taskbar.

* Fri Mar 05 2010 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt4.20100305
- New snapshot.

* Mon May 25 2009 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt4.20090330
- Fix build.

* Mon Mar 30 2009 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt3.20090330
- New snapshot.
- Add menu method.
- Rewrite alt-config-file.patch.

* Fri Feb 27 2009 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt3.20080901
- Add system defaults.
- Add read system and user config.
- Move and split system config to /etc/X11/jwm.

* Sat Jan 10 2009 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt2.20080901
- Bugfix build.

* Mon Sep 01 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt1.20080901
- New snapshot.

* Tue Mar 11 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt1
- First build for sisyphus.
