# BEGIN SourceDeps(oneline):
BuildRequires: libX11-devel libXrender-devel libfribidi-devel xorg-xproto-devel
# END SourceDeps(oneline)
Name:           jwm
Version:        2.1.0
Release:        alt1_4
Summary:        Joe's Window Manager

Group:          Graphical desktop/Other
License:        GPLv2+
URL:            http://joewing.net/programs/jwm
Source0:        http://joewing.net/programs/jwm/releases/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-nostrip.patch
Patch1:         %{name}-timestamps.patch
Patch2:         %{name}-destdir.patch

BuildRequires:  libXext-devel libXmu-devel libXinerama-devel
BuildRequires:  libXpm-devel libjpeg-devel libpng-devel
BuildRequires:  libXft-devel fribidi-devel libfreetype-devel
Requires:       xterm
Source44: import.info
Patch33: jwm-alt-add-sigchld-sigign.patch
Patch34: jwm-alt-fix-build-warning.patch
Patch35: jwm-alt-config-file.patch
Patch36: jwm-alt-dead-windows-in-taskbar.patch
Source45: jwm.method
Source46: jwm.wmsession
Source47: jwm-conf.tar
Source48: startjwm

%description
JWM is a window manager for the X11 Window System. JWM is written in C and uses
only Xlib at a minimum. The following libraries can also be used if available:

* libXext for the shape extension
* libXext for the render extension
* libXmu for drawing rounded windows (shape extension also needed)
* libXinerama for Xinerama support
* libXpm for XPM backgrounds and icons
* libjpeg for JPEG backgrounds and icons
* libpng for PNG backgrounds and icons
* libxft for antialiased and true type fonts
* libfribidi for right-to-left language support

JWM supports MWM and Extended Window Manager Hints (EWMH).

%prep
%setup -q

# Do not strip binary file
%patch0 -p0 -b .orig

# Preserve timestamps in installation
%patch1 -p0 -b .orig

# Enable the use of DESTDIR
%patch2 -p0 -b .orig
%patch33 -p2
%patch34 -p2
%patch35 -p1
%patch36 -p2

%build
# -Werror
CFLAGS="$CFLAGS -O3 -Wall"
%autoreconf
%configure \
        --enable-debug \
        --enable-shade \
        --sysconfdir=%_sysconfdir/X11/jwm 
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/xsessions
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/

tar -xC %buildroot/%_sysconfdir/X11/jwm -f %SOURCE47
rm -f -- %buildroot/%_sysconfdir/X11/jwm/system.jwmrc

# install -m755 %SOURCE48 %buildroot/%_bindir/
install -D -m644 %SOURCE46 %buildroot/%_sysconfdir/X11/wmsession.d/jwm
install -D -m 755 %{SOURCE45} %buildroot%_sysconfdir/menu-methods/jwm

%files
%doc LICENSE README todo.txt
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/X11/jwm/*
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}.*
%config %_sysconfdir/menu-methods/jwm
%config %_sysconfdir/X11/wmsession.d/jwm

%changelog
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
