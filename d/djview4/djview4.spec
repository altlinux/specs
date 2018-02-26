%def_disable static
%define qtdir %_libdir/qt4

Summary: DjVu viewers, encoders and utilities (QT4 based version)
Name: djview4
Version: 4.5
Release: alt1.1
License: GPL
Group: Publishing
Source: %name-%version.tar.bz2
Url: http://djvulibre.djvuzone.org/

Packager: Evgeny Sinelnikov <sin@altlinux.ru>

# Automatically added by buildreq on Wed Oct 10 2007
BuildRequires: gcc-c++ libXext-devel libjpeg-devel libqt4-devel libqt4-network xdg-utils xorg-cf-files
BuildRequires: libdjvu-devel >= 3.5.18

# added by hands
BuildRequires: browser-plugins-npapi-devel

%description
This package contains the djview4 viewer and browser plugin.
This new viewer relies on the DjVulibre library and the Qt4 toolkit.

Highlights:
- entirely based on the public djvulibre api.
- entirely written in portable Qt4.
- has been reported to work with Qt/Mac.
- should work with Qt/Windows as well.
- continuous scrolling of pages
- side-by-side display of pages
- ability to specify a url to the djview command
- all plugin and cgi options available from the command line
- all silly annotations implemented
- display thumbnails as a grid
- display outlines
- page names supported (see djvused command set-page-title)
- metadata dialog (see djvused command set-meta)
- implemented as reusable Qt widgets

%package -n mozilla-plugin-djvu4
Summary: DjVu NPAPI plugin (QT4 based version)
Group: Networking/WWW
Requires: browser-plugins-npapi 
Conflicts: mozilla-plugin-djvu < 4.1
Obsoletes: mozilla-plugin-djvu < 4.1

%description -n mozilla-plugin-djvu4
Under Unix/X11, djview4 can be used as a browser plugin
by means of the small shared library named nsdejavu.so.
The djview3 distributed with djvulibre uses the same approach.

%prep
%setup -q -n %name-%version

%build
# hack for NPAPI location
%__subst 's,-rpath ${plugindir},-rpath %browser_plugins_path,' nsdejavu/Makefile.in
%__subst 's,^plugindir[[:space:]]*=.*,plugindir = %buildroot%browser_plugins_path,' nsdejavu/Makefile.in

export QTDIR=%qtdir
export PATH=$QTDIR/bin:$PATH
%configure %{subst_enable static} PTHREAD_LIBS="-lpthread"
%make #NO SMP

%install
%makeinstall

#install-gnome: FORCE
%__install -pD -m 644 desktopfiles/hi32-djview4.png %buildroot%_niconsdir/djvulibre-djview4.png
%__install -pD -m 644 desktopfiles/djvulibre-djview4.desktop %buildroot%_desktopdir/djvulibre-djview4.desktop

#hack for djvu-viewer compatibility
rm -f %buildroot%_bindir/djview
rm -f %buildroot%_mandir/man1/djview.1

%find_lang %name

%files
%_bindir/djview*
%_mandir/man?/djview*
%_desktopdir/*.desktop
%_datadir/djvu/%name/
%_niconsdir/*

%files -n mozilla-plugin-djvu4
%browser_plugins_path/*.so*
%_mandir/man?/nsdejavu*

%changelog
* Wed Sep 30 2009 Alexey Gladkov <legion@altlinux.ru> 4.5-alt1.1
- NMU: Rebuilt with browser-plugins-npapi.

* Sun Jun 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.5-alt1
- Update to new release

* Mon Nov 24 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.4-alt1
- Update to new release

* Sun Jan 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.3-alt1
- Update to new release

* Wed Oct 10 2007 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.2-alt1
- Initial release
